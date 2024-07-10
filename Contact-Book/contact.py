import sys 
import csv
import os

contacts = {}

def load_contact():
    if os.path.exists('./contacts.csv'):
        with open('./contacts.csv', 'r') as file:
            reader = csv.reader(file)
            for contact in reader:
                if contact:
                    contacts[contact[0]] = contact[1]
                    
def save_contact():
    with open('./contacts.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        for name, ph_no in contacts.items():
            writer.writerow([name, ph_no])

def add_contact():
    name = input('Contact Name: ').title()
    ph_no = int(input('Contact Number: '))
    contacts[name] = ph_no
    print('Contact Added Successfully')
    save_contact()
    main()
    
def search_contact():
    search = input('Contact Name to search: ')
    if search in contacts:
        print(f'{search}: {contacts[search]}')
        delete = input('Do you want to delete this contact? (y/n): ').lower()
        if delete == 'y':
            delete_contact()
        else:
            main()
    else:
        print('No Such Contact Found')
    
def delete_contact():
    name = input('Contact Name to delete: ').title()
    if name in contacts:
        del contacts[name]
        save_contact()
        print('Contact Saved Successfully')
        main()
    else:
        print('No Such Contact Found.')
     
    
def exit_from_app():
    if not contacts:
        print('There is no Contacts to be saved..Bye!')
        sys.exit()
    else:
        print('All contacts Saved successfully..Bye...!')
        save_contact()
        sys.exit()
   
def display_menu():
    print('\nContact-Book Menu: ') 
    print('1. Add contact')
    print('2. Search Contact') 
    print('3. Delete Contact')
    print('4. Exit from Book')
    
def main():
    try:
        load_contact()
        display_menu()
        choice = int(input('\nMake your choice: '))
        if choice == 1:
            add_contact()
        elif choice == 2:
            search_contact()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            exit_from_app()
        else:
            print('Error: Make Sure Your Choice is in the given list.')
    except ValueError:
        print('Error: Please Enter only number...\n')
        main()
    
    
if __name__ == '__main__':
    main()  