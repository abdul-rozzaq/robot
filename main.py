import os

from helper.set_token import set_token
from helper.download_data import download_house_list
from helper.filter import filter_data
from helper.download_members_data import download_members_data
from helper.filter_members import filter_members

doc = """
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

name = input('Enter name of village: >> ')

print(doc)

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
                #(open('delete-people.py').read())
            case 8:
                ...
                #(open('delete-family.py').read())
            case 9:
                ...
                #(open('delete-houses.py').read())
            case 0:
                print('Exit')
            case -1:
                os.system('cls')
                print(doc)


if __name__ == '__main__':
    main()

    
