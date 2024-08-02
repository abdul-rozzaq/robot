
from robot import Request
import json


def download_house_list(name: str):

    data = Request(name).post('https://mahalla.ijro.uz/api/house/list', body={
        "page": "limit",
        "offset": 1
    })

    print(data.text)

    with open(f'db/data-{name}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data.json(), indent=4, ensure_ascii=False))

    print(name, len(data.json()['response']))


