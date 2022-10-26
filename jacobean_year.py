import datetime
import random

def menu():
    print("***** JACOBEAN YEAR *****")
    print("Jacobean Year is a Holy year,\nthat means that Saint James Day\n(25th July), falls on Sunday.")
    print("Want to know just the year you enter or random Jacobean Years?")
    print("1. Enter a year")
    print("2. Random Jacobean Years")
    print("3. Exit")
    choice = int(input("Which is your choice? "))

    if choice == 1:
        jacobeanYear()
    elif choice == 2:
        nextJacobeanYears()
    elif choice == 3:
        exit(0)
    else:
        print("Wrong choice")
        menu()

def jacobeanYear():
    user_year = int(input("\nDo you wanna know when is the next Jacobean Year? Enter a year: "))
    
    date = datetime.datetime(user_year, 7, 25).strftime('%A')
    if date == 'Sunday':
        print("Jacobean Year! Let's do the Camino de Santiago!")
        exit(0)
    else:
        print("\nTry another year")
        jacobeanYear()


def nextJacobeanYears():
    years = []
    i = 0

    print("\nThis are the next Jacobean Years")
    while i <= 100:
        year = random.randint(2023,2091)
        date = datetime.datetime(year, 7, 25).strftime('%A') 
        if date == 'Sunday':
            years.append(year)
        i+=1
    else:
        print(sorted(years))

if __name__ == '__main__':
    menu()