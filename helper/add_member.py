from alive_progress import alive_bar

from helper.log import Logger
from robot import *

from robot.models.citizen import Citizen
from robot.models.house import House

import json, random
from requests.exceptions import ConnectTimeout


def add_member(name):
        
    def check_person(pinpp, document):
        return Request(name).post('https://mahalla.ijro.uz/api/citizen/get-citizen-info', body={"pinpp": pinpp, "passport_series": document})

    def check_children(seria, number):
        return Request(name).post('https://mahalla.ijro.uz/api/citizen/get-birth-certificate', body={
            "cert_number": str(seria),
            "cert_series": str(number),
        })

    def get_families(house_id):
        return Request(name).post('https://mahalla.ijro.uz/api/family/list', body={"house_id": house_id})

    def extract(document):
        letters = ''.join([char for char in document if char.isalpha()])
        numbers = ''.join([char for char in document if char.isdigit()])
            
        if letters == "IFR":
            letters = "I-FR"
        elif letters == "IIIFR":
            letters = "III-FR"
            
        return letters, numbers
        
        
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
        
        
        return Request(name).post('https://mahalla.ijro.uz/api/family-member/create-v2', body=data)


        
    with open(f'db/data-{name}.json', 'r', encoding='UTF-8') as file:
        houses = [House.from_dict(dat) for dat in json.loads(file.read())['response']]
        
    with open(f'json_data/{name}.json', 'r', encoding='UTF-8') as file:
        raw_users = json.loads(file.read())    

    
    index = 823
    offset = 0
    
    with alive_bar(len(raw_users) - index) as bar:
        while index < len(raw_users):
            
            if index + offset >= len(houses):
                offset -= len(houses)
                

            house = houses[index + offset]
            pinpp, document = raw_users[index]


            try:
                if document[0] == 'A':
                    person = check_person(pinpp, document)
                    families = get_families(house.id)
                else:
                    person = check_children(*extract(document))
            except ConnectTimeout:  
                continue

            if person.status_code == 201 and families.status_code == 201:
                
                families_list = [Family.from_dict(dat) for dat in families.json()['response'] if dat['owner'] != None]
                
                if len(families_list) != 0 and 'response' in person.json():
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
                    
            index += 1
            bar()

def main():
    add_member('chumbogish')


if __name__ == '__main__':
    main()
    
    
    