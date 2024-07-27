from alive_progress import alive_bar

from robot import *

from robot.models.citizen import Citizen
from robot.models.house import House

import json, random
from requests.exceptions import ConnectTimeout


def add(street_id, citizen_id, pinpp, citizen_birthday, citizen_fullname, house_id, family_id):
    data = {
        "street_id": street_id,
        "citizen_id": citizen_id,
        "pinpp": pinpp,
        "citizen": {
            "birth_date": citizen_birthday,
            "full_name": citizen_fullname
        },
        "house": {
            "id": house_id
        },
        "family": {
            "id": family_id
        },
        "family_member": {
            "type": random.randint(1, 15)
        }
    }
    
    
    return Request.post('https://mahalla.ijro.uz/api/family-member/create-v2', body=data)

def check_person(pinpp, document):
    return Request.post('https://mahalla.ijro.uz/api/citizen/get-citizen-info', body={"pinpp": pinpp, "passport_series": document})

def get_families(house_id):
    return Request.post('https://mahalla.ijro.uz/api/family/list', body={"house_id": house_id})

def add_member(name):
        
    with open(f'db/data-{name}.json', 'r', encoding='UTF-8') as file:
        houses = [House.from_dict(dat) for dat in json.loads(file.read())['response']]
        
    with open(f'ready/{name}.json', 'r', encoding='UTF-8') as file:
        raw_users = json.loads(file.read())

    index = 0
    step = 0

    current = int(input('Enter the current count: '))
    stop = int(input('Enter the stop count: '))

    total_iterations = stop - current - 1

    with alive_bar(total_iterations + 1) as bar:
        while step <= total_iterations:
            house = houses[index]
            pinpp, document = raw_users[index]

            try:
                person = check_person(pinpp, document)
                families = get_families(house.id)
            except ConnectTimeout:
                continue

            if person.status_code == 201 and families.status_code == 201:
                
                families_list = [Family.from_dict(dat) for dat in families.json()['response'] if dat['owner'] != None]
                
                if len(families_list) != 0:
                    citizen = Citizen.from_dict(person.json()['response'])

                    fam = families_list[0]

                    resp = add(
                        street_id=house.street_id,
                        citizen_id=citizen.id,
                        citizen_birthday=citizen.user_info.birth_date,
                        citizen_fullname=citizen.user_info.full_name,
                        family_id=fam.id,
                        house_id=house.id,
                        pinpp=citizen.pinpp
                    )
                    
                    if resp.status_code != 400:
                        step += 1
                        
                        if index > 270:
                            index = 0
                            
                            random.shuffle(houses)
                            random.shuffle(raw_users)
                        else:
                            index += 1
                            
                        bar()                


def main():
    add_member('chumbogish')


if __name__ == '__main__':
    main()
    
    
    