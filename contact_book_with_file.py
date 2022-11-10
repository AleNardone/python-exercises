import fileinput

def menu():
    print("****** MENU ******\n")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show All Contacts")
    print("4. Modify Contact")
    print("5. Remove Contact")
    print("6. Exit")
    choice=int(input("\nWhat do you want to do? "))

    if choice == 1:
        addContact()

    elif choice == 2:
        searchContact()

    elif choice == 3:
        allContacts()

    elif choice == 4:
        modifyContact()

    elif choice == 5:
        removeContact()

    elif choice == 6:
        exit(0)

    else:
        print("Invalid choice... Try again.")
        menu()
        
l_fname=[]
l_lname=[]
l_phone=[]
l_email=[]
num_contacts = 100
current_contact = 0


def addContact():           
       current_contact = 0
        
       if current_contact == 0:
            userData()
                  
       elif current_contact > 0:
            userData()

       current_contact += 1

       if current_contact <= num_contacts:
           another = input("\nAdd another contact? (Y/N) ")
           if another == 'Y' or another == 'y':
              addContact()                        
           else:
              save_file()
              menu()
       else:
            print('Your contact book is full... You have to remove a contact')
            removeContact()

def userData():
    print("Add New Contact: ")

    fname = str(input("First Name: "))
    l_fname.append(fname)

    lname = str(input("Last Name: "))
    l_lname.append(lname)

    phone = str(input("Phone Number: "))
    l_phone.append(phone)

    mail = str(input("Email: "))
    l_email.append(mail)

 

            
def searchContact():
    print("Search for a contact by: ")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email")
    print("5. Go back to main menu")
    choice= int(input("\nWhich is your choice: "))

    if choice == 1:
        fname = str(input("Write the first name: "))
        with open('contactbook.txt', 'r') as file:
            read_it = file.read()
            found = False
            for line in read_it.splitlines():
                if fname in line:
                    print(line)
                    found = True
                    
            if found == True:
                input('Press any key to continue...')
                menu()
            else:
                print("Invalid choice... Try again.")
                searchContact()

    elif choice == 2:
        lname = str(input("Write the last name: "))
        with open('contactbook.txt', 'r') as file:
            read_it = file.read()
            found = False
            for line in read_it.splitlines():
                if lname in line:
                    print(line)
                    found = True
                    
            if found == True:
                input('Press any key to continue...')
                menu()
            else:
                print("Invalid choice... Try again.")
                searchContact()

    elif choice == 3:
        phone = str(input("Write the phone number: "))
        with open('contactbook.txt', 'r') as file:
            read_it = file.read()
            found = False
            for line in read_it.splitlines():
                if phone in line:
                    print(line)
                    found = True
                    
            if found == True:
                input('Press any key to continue...')
                menu()
            else:
                print("Invalid choice... Try again.")
                searchContact()

    elif choice == 4:
        mail = str(input("Write the last name: "))
        with open('contactbook.txt', 'r') as file:
            read_it = file.read()
            found = False
            for line in read_it.splitlines():
                if mail in line:
                    print(line)
                    found = True
                    
            if found == True:
                input('Press any key to continue...')
                menu()
            else:
                print("Invalid choice... Try again.")
                searchContact()
    
    elif choice == 5:
        menu()

    else:
        print("Invalid choice... Try again.")
        searchContact()


def allContacts():    
    with open("contactbook.txt") as f:
       content = f.read()
       print(content)
    input("Press enter to continue...")
    menu()


def modifyContact():
    print('What do you want to modify?')
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email")
    print("5. Go back to main menu")
    choice= int(input("\nWhich is your choice: "))

    if choice == 1:
                modifyline = []
                fname = input('Write the first name of the contact you want to replace? ')
                fname_contact = input('Write the new first name: ')
                found = False
                with open('contactbook.txt', 'r') as file:
                        read_it = file.read().splitlines()
                for line in read_it:
                        modifyline.append(line)
                
                for line in modifyline:
                    if fname in line:
                        replace = [items.replace(fname, fname_contact) for items in modifyline]
                        found = True         
        
                with open("contactbook.txt", "w") as file:
                    for i in range(len(replace)):
                        file.write(f'\n{replace[i]}')
                file.close()
        

                if found == True:
                    print('Press any key to continue...')
                    menu()
                else:
                    print('Data not found... Try again')
                    modifyContact()                     


    elif choice == 2:
                modifyline = []
                lname = input('Write the last name of the contact you want to replace? ')
                lname_contact = input('Write the new last name: ')
                found = False
                with open('contactbook.txt', 'r') as file:
                        read_it = file.read().splitlines()
                for line in read_it:
                        modifyline.append(line)
                
                for line in modifyline:
                    if lname in line:
                        replace = [items.replace(lname, lname_contact) for items in modifyline]
                        found = True         
        
                with open("contactbook.txt", "w") as file:
                    for i in range(len(replace)):
                        file.write(f'\n{replace[i]}')
                file.close()
        

                if found == True:
                    print('Press any key to continue...')
                    menu()
                else:
                    print('Data not found... Try again')
                    modifyContact() 

    elif choice == 3:
                modifyline = []
                phone = input('Write the phone number of the contact you want to replace? ')
                phone_contact = input('Write the new phone number: ')
                found = False
                with open('contactbook.txt', 'r') as file:
                        read_it = file.read().splitlines()
                for line in read_it:
                        modifyline.append(line)
                
                for line in modifyline:
                    if phone in line:
                        replace = [items.replace(phone, phone_contact) for items in modifyline]
                        found = True         
        
                with open("contactbook.txt", "w") as file:
                    for i in range(len(replace)):
                        file.write(f'\n{replace[i]}')
                file.close()
        

                if found == True:
                    print('Press any key to continue...')
                    menu()
                else:
                    print('Data not found... Try again')
                    modifyContact() 

    elif choice == 4:
                modifyline = []
                mail = input('Write the email of the contact you want to replace? ')
                mail_contact = input('Write the new email: ')
                found = False
                with open('contactbook.txt', 'r') as file:
                        read_it = file.read().splitlines()
                for line in read_it:
                        modifyline.append(line)
                
                for line in modifyline:
                    if mail in line:
                        replace = [items.replace(mail, mail_contact) for items in modifyline]
                        found = True         
        
                with open("contactbook.txt", "w") as file:
                    for i in range(len(replace)):
                        file.write(f'\n{replace[i]}')
                file.close()
        

                if found == True:
                    print('Press any key to continue...')
                    menu()
                else:
                    print('Data not found... Try again')
                    modifyContact() 

    elif choice == 5:
        menu()

    else:
        print('Invalid choice... Choose one from above')
        modifyContact()

def removeContact():
    f = open('contactbook.txt', 'r')
    print("Search for a contact by: ")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email")
    print("5. Go back to main menu")
    choice = int(input("Which is your choice: "))

    if choice == 1:
        removelines = []
        found = False
        fname = str(input("Write the first name: "))
        with open('contactbook.txt', 'r') as file:
            read_it = file.read()
            for line in read_it.splitlines():
                removelines.append(line)

            for line in removelines:
                if fname in line:
                    removelines.remove(line)
                    found = True         
        
        with open("contactbook.txt", "w") as file:
            for i in range(len(removelines)):
                file.write(f'\n{removelines[i]}')
        file.close()
        

        if found == True:
            print('Press any key to continue...')
            menu()
        else:
            print('Data not found... Try again')
            removeContact()


    elif choice == 2:
        removelines = []
        found = False
        lname = str(input("Write the first name: "))
        with open('contactbook.txt', 'r') as file:
            read_it = file.read()
            for line in read_it.splitlines():
                removelines.append(line)

            for line in removelines:
                if lname in line:
                    removelines.remove(line)
                    found = True         
        
        with open("contactbook.txt", "w") as file:
            for i in range(len(removelines)):
                file.write(f'\n{removelines[i]}')
        file.close()
        

        if found == True:
            print('Press any key to continue...')
            menu()
        else:
            print('Data not found... Try again')
            removeContact()


    elif choice == 3:
        removelines = []
        found = False
        phone = str(input("Write the first name: "))
        with open('contactbook.txt', 'r+') as file:
            read_it = file.read()
            for line in read_it.splitlines():
                removelines.append(line)

            for line in removelines:
                if phone in line:
                    removelines.remove(line)
                    found = True         
        
        with open("contactbook.txt", "w") as file:
            for i in range(len(removelines)):
                file.write(f'\n{removelines[i]}')
        file.close()
        

        if found == True:
            print('Press any key to continue...')
            menu()
        else:
            print('Data not found... Try again')
            removeContact()


    elif choice == 4:
        removelines = []
        found = False
        mail = str(input("Write the first name: "))
        with open('contactbook.txt', 'r+') as file:
            read_it = file.read()
            for line in read_it.splitlines():
                removelines.append(line)

            for line in removelines:
                if mail in line:
                    removelines.remove(line)
                    found = True         
        
        with open("contactbook.txt", "w") as file:
            for i in range(len(removelines)):
                file.write(f'\n{removelines[i]}')
        file.close()
        

        if found == True:
            print('Press any key to continue...')
            menu()
        else:
            print('Data not found... Try again')
            removeContact()


    elif choice == 5:
            menu()

    else:
        print('Invalid choice... Choose one from above')
        removeContact()

    

def save_file():
     with open("contactbook.txt", "w") as f:
         f.write("***** ALL CONTACTS *****")
         f.write("\nFirst Name\t\tLast Name\t\tPhone Number\t\t\t\tEmail\t\t\t")
         for i in range(len(l_fname)):
            f.write(f"\n{l_fname[i]}\t\t\t{l_lname[i]}\t\t\t{l_phone[i]}\t\t\t{l_email[i]}")
     f.close()

if __name__ == "__main__":
    menu()
    save_file()

