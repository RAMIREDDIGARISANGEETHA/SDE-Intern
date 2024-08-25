'''Task-03

# Implement a Simple Contact Management System

Develop a program that allows users to store and manage contact information.
The program should provide options to add a new contact by entering their name, phone number, and email address.
It should also allow users to view their contact list, edit existing contacts, and delete contacts if needed.
The program should store the contacts in memory or in a file for persistent storage.'''

contact={}
def display_contact():
    print("Name\t\tcontact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice=int(input("1.Add new contact:\n 2. Search contact:\n 3.Display Contact:\n 4.Edit Contact:\n 5.Delete Contact:\n 6.Exit:\n Enter your choice:"))
    if choice ==1:
        name = input("enter the contact name:")
        number=input("enter the phone number:")
        print("Successfully added..!!")
        contact[name]=number
    elif choice==2:
        name1=input("enter the contact name:")
        if name1 in contact:
            print("Here we go..!!")
            print(name1,"'s cotact number is",contact[name1])
        else:
            print("Name is not found in contact book")
    elif choice==3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice==4:
        edit_contact=input("Enter the contact to be edited:")
        if edit_contact in contact:
            phone=input("enter the mobile number")
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif choice==5:
        del_contact=input("Enter the contact to be deleted:")
        if del_contact in contact:
            confirm=input("Do you want to delete this contact y/n?")
            if confirm =='y' or confirm=='Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
        break
    