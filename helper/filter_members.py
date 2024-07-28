import json


# from download_members_data import download_members_data

def filter_members(name):
    with open(f'members/data-{name}.json', 'r', encoding='utf-8') as file:
        pinfls = [x['pinfl'] for x in json.loads(file.read())]

    with open(f'json_data/{name}.json', 'r', encoding='utf-8') as file:
        new_members = json.load(file)

    members = [member for member in new_members if member[0] not in pinfls]

    with open(f'ready/data-{name}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(members, indent=4, ensure_ascii=False))

    print(len(members), 'members')

    return members
