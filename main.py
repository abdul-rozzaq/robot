import os

from helper import clear_logs
from helper.set_token import set_token
from helper.download_data import download_house_list
from helper.filter import filter_data
from helper.download_members_data import download_members_data
from helper.filter_members import filter_members

doc = """
Selected village: {}

1.  Set Token
2.  Download data
3.  Download members data
4.  Prepare excell data
5.  Filter prepared data    
6.  Add people
7.  Add family
8.  Add houses
9.  Delete families
10. Delete houses
11. Delete people
"""

files = list(map(lambda x: x.split('.')[0], os.listdir('text_data')))

for index in range(1, len(files) + 1):
    file = files[index - 1]

    print(f'{index}. {file}')

name = files[int(input('Choose the village >> ')) - 1]

clear_logs()

print(doc.format(name))


def main():
    while True:
        ex = int(input('>> '))

        match ex:
            case 1:
                set_token(name)
            case 2:
                download_house_list(name)
            case 3:
                download_members_data(name)
            case 4:
                filter_data(name)
            case 5:
                filter_members(name)
            case 6:
                ...
            case 7:
                ...
                # (open('delete-people.py').read())
            case 8:
                ...
                # (open('delete-family.py').read())
            case 9:
                ...
                # (open('delete-houses.py').read())
            case 0:
                print('Exit')

                break
            case -1:
                clear_logs()
                print(doc.format(name))


if __name__ == '__main__':
    main()
