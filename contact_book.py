f = open("contactbook.txt", "a+")

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
num_contacts = 3


def addContact():
       current_contact = 0           
       while current_contact < num_contacts:     
            print("Add New Contact: ")

            fname = str(input("First Name: "))
            l_fname.append(fname)

            lname = str(input("Last Name: "))
            l_lname.append(lname)

            phone = str(input("Phone Number: "))
            l_phone.append(phone)

            mail = str(input("Email: "))
            l_email.append(mail)

            current_contact += 1

            another = input("\nAdd another contact? (Y/N) ")
            if another == 'Y' or another == 'y':
                addContact()                        
            else:
                save_file()
                menu()
       
       else:     
          menu()

            
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
        if fname in l_fname:
            index = l_fname.index(fname)
            lname = l_lname[index]
            phone = l_phone[index]
            mail = l_email[index]
            print(f"First Name: {fname}, Last Name: {lname}, Phone Number: {phone}, Email: {mail}")
            input("Press enter to continue...")
            menu()
        else:
            print("Invalid choice... Try again.")
            searchContact()

    elif choice == 2:
        lname = str(input("Write the last name: "))
        if lname in l_lname:
            index = l_lname.index(lname)
            fname = l_fname[index]
            phone = l_phone[index]
            mail = l_email[index]
            print(f"First Name: {fname}, Last Name: {lname}, Phone Number: {phone}, Email: {mail}")
            input("Press enter to continue...")
            menu()
        else:
            print("Invalid choice... Try again.")
            searchContact()

    elif choice == 3:
        phone = str(input("Write the phone number: "))
        if phone in l_phone:
            index = l_phone.index(phone)
            fname = l_fname[index]
            lname = l_lname[index]
            mail = l_email[index]
            print(f"First Name: {fname}, Last Name: {lname}, Phone Number: {phone}, Email: {mail}")
            input("Press enter to continue...")
            menu()
        else:
            print("Invalid choice... Try again.")
            searchContact()

    elif choice == 4:
        phone = str(input("Write the email: "))
        if mail in l_email:
            index = l_email.index(mail)
            fname = l_fname[index]
            lname = l_lname[index]
            phone = l_phone[index]
            print(f"First Name: {fname}, Last Name: {lname}, Phone Number: {phone}, Email: {mail}")
            input("Press enter to continue...")
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
    #print("***** ALL CONTACTS *****")
    #print("\nNumber\t\tFirst Name\t\tLast Name\t\tPhone Number\t\t\t\tEmail\t\t\t")
    #for i in range(num_contacts): 
    #    print(f"{i+1}\t\t{l_fname[i]}\t\t\t{l_lname[i]}\t\t\t{l_phone[i]}\t\t\t{l_email[i]}")    
    #input("\nPress enter to continue...")
    #menu()

    with open("contactbook.txt") as f:
       content = f.read()
       print(content)
    input("Press enter to continue...")
    menu()


def modifyContact():
    print("Search for a contact by: ")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email")
    print("5. Go back to main menu")
    choice= int(input("\nWhich is your choice: "))

    for index in range(num_contacts):
        if choice == 1:
            fname = str(input("Write the first name: "))
            if fname in l_fname:
                index = l_fname.index(fname)
                lname = l_lname[index]
                phone = l_phone[index]
                mail = l_email[index]
                print("What do you want to modify: ")
                print("1. First Name: ")
                print("2. Last Name: ")
                print("3. Phone Number: ")
                print("4. Email: ")
                print("5. Go back to Main Menu")
                m_choice=int(input("Choice: "))

                if m_choice == 1:
                   new_fname=str(input("New First Name: "))
                   l_fname[l_fname.index(fname)] = new_fname
                   save_file()
                   menu()
               
                elif m_choice == 2:
                    new_lname=str(input("New Last Name: "))
                    l_lname[l_lname.index(lname)] = new_lname
                    save_file()
                    menu()
                
                elif m_choice == 3:
                    new_phone=int(input("New Phone Number: "))
                    l_phone[l_phone.index(phone)] = new_phone 
                    save_file()
                    menu()

                elif m_choice == 4:
                    new_mail=str(input("New Email: "))
                    l_email[l_email.index(mail)] = new_mail
                    save_file()
                    menu()

                elif m_choice == 5:
                    menu()

                else:
                    print("Invalid choice... Try again.")
                    modifyContact()
                

        elif choice == 2:
            lname = str(input("Write the last name: "))
            if lname in l_lname:
                index = l_lname.index(lname)
                fname = l_fname[index]
                phone = l_phone[index]
                mail = l_email[index]
                print("What do you want to modify: ")
                print("1. First Name: ")
                print("2. Last Name: ")
                print("3. Phone Number: ")
                print("4. Email: ")
                print("5. Go back to Main Menu")
                m_choice=int(input("Choice: "))

                if m_choice == 1:
                   new_fname=str(input("New First Name: "))
                   l_fname[l_fname.index(fname)] = new_fname
                   save_file()
                   menu()
               
                elif m_choice == 2:
                    new_lname=str(input("New Last Name: "))
                    l_lname[l_lname.index(lname)] = new_lname 
                    save_file()
                    menu()
                
                elif m_choice == 3:
                    new_phone=int(input("New Phone Number: "))
                    l_phone[l_phone.index(phone)] = new_phone 
                    save_file()
                    menu()

                elif m_choice == 4:
                    new_mail=str(input("New Email: "))
                    l_email[l_email.index(mail)] = new_mail 
                    save_file()
                    menu()

                elif m_choice == 5:
                    menu()

                else:
                    print("Invalid choice... Try again.")
                    modifyContact()

        elif choice == 3:
            phone = str(input("Write the Phone Number: "))
            if phone in l_phone:
                index = l_phone.index(phone)
                fname = l_fname[index]
                lname = l_lname[index]
                mail = l_email[index]
                print("What do you want to modify: ")
                print("1. First Name: ")
                print("2. Last Name: ")
                print("3. Phone Number: ")
                print("4. Email: ")
                print("5. Go back to Main Menu")
                m_choice=int(input("Choice: "))

                if m_choice == 1:
                   new_fname=str(input("New First Name: "))
                   l_fname[l_fname.index(fname)] = new_fname
                   save_file()
                   menu()
               
                elif m_choice == 2:
                    new_lname=str(input("New Last Name: "))
                    l_lname[l_lname.index(lname)] = new_lname  
                    save_file()
                    menu()
                
                elif m_choice == 3:
                    new_phone=int(input("New Phone Number: "))
                    l_phone[l_phone.index(phone)] = new_phone 
                    save_file()
                    menu()

                elif m_choice == 4:
                    new_mail=str(input("New Email: "))
                    l_email[l_email.index(mail)] = new_mail  
                    save_file()
                    menu()

                elif m_choice == 5:
                    menu()

                else:
                    print("Invalid choice... Try again.")
                    modifyContact()

        elif choice == 4:
            mail = str(input("Write email: "))
            if mail in l_email:
                index = l_email.index(mail)
                fname = l_fname[index]
                lname = l_lname[index]
                phone = l_phone[index]
                print("What do you want to modify: ")
                print("1. First Name: ")
                print("2. Last Name: ")
                print("3. Phone Number: ")
                print("4. Email: ")
                print("5. Go back to Main Menu")
                m_choice=int(input("Choice: "))

                if m_choice == 1:
                   new_fname=str(input("New First Name: "))
                   l_fname[l_fname.index(fname)] = new_fname
                   save_file()
                   menu()
               
                elif m_choice == 2:
                    new_lname=str(input("New Last Name: "))
                    l_lname[l_lname.index(lname)] = new_lname  
                    save_file()
                    menu()
                
                elif m_choice == 3:
                    new_phone=int(input("New Phone Number: "))
                    l_phone[l_phone.index(phone)] = new_phone 
                    save_file()
                    menu()

                elif m_choice == 4:
                    new_mail=str(input("New Email: "))
                    l_email[l_email.index(mail)] = new_mail 
                    save_file()
                    menu()

                elif m_choice == 5:
                    menu()

                else:
                    print("Invalid choice... Try again.")
                    modifyContact()



def removeContact():
    print("Search for a contact by: ")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email")
    print("5. Go back to main menu")
    choice= int(input("\nWhich is your choice: "))

    for index in range(num_contacts):
        if choice == 1:
            fname = str(input("Write the first name: "))
            if fname in l_fname:
                index = l_fname.index(fname)
                lname = l_lname[index]
                phone = l_phone[index]
                mail = l_email[index]
                l_fname.pop(index)
                l_lname.pop(index)
                l_phone.pop(index)
                l_email.pop(index)
                addContact()

        elif choice == 2:
            lname = str(input("Write the last name: "))
            if lname in l_lname:
                index = l_lname.index(lname)
                fname = l_fname[index]
                phone = l_phone[index]
                mail = l_email[index]
                l_fname.pop(index)
                l_lname.pop(index)
                l_phone.pop(index)
                l_email.pop(index)
                addContact()

        elif choice == 3:
            phone = str(input("Write the Phone Number: "))
            if phone in l_phone:
                index = l_phone.index(phone)
                fname = l_fname[index]
                lname = l_lname[index]
                mail = l_email[index]
                l_fname.pop(index)
                l_lname.pop(index)
                l_phone.pop(index)
                l_email.pop(index)
                addContact()

        elif choice == 4:
           mail = str(input("Write Email: "))
           if mail in l_email:
                index = l_email.index(mail)
                fname = l_fname[index]
                lname = l_lname[index]
                phone = l_phone[index]
                l_fname.pop(index)
                l_lname.pop(index)
                l_phone.pop(index)
                l_email.pop(index)
                addContact()

        elif choice == 5:
            menu()

    

def save_file():
     with open("contactbook.txt", "w") as f:
         f.write("***** ALL CONTACTS *****")
         f.write("\nNumber\t\tFirst Name\t\tLast Name\t\tPhone Number\t\t\t\tEmail\t\t\t")
         for i in range(num_contacts):
            f.write(f"\n{i+1}\t\t{l_fname[i]}\t\t\t{l_lname[i]}\t\t\t{l_phone[i]}\t\t\t{l_email[i]}")
     f.close()

if __name__ == "__main__":
    menu()
    save_file()
