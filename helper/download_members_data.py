from alive_progress import alive_bar

import math
from robot import Request
import json


def download_members_data(name: str):
    members = []

    members_count = 0
    offset = 0

    req = lambda offset: Request(name).post('https://mahalla.ijro.uz/api/family-member/v2/list', body={
        "limit": 100,
        "offset": offset
    }).json()
    
    page_1 = req(offset)
    
    members.extend(page_1['response']['list'])
    
    members_count = int(page_1['response']['total'])

    pages_count = math.ceil(members_count / 100)

    with alive_bar(pages_count - 1) as bar:    
        for i in range(1, pages_count):
            page = req(100 * (offset + i))
            members.extend(page['response']['list'])

            bar()
    
    print(len(members), 'members downloaded successfully')

    with open(f'members/data-{name}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(members, indent=4, ensure_ascii=False))

    

