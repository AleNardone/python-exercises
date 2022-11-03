class Account:

    def __init__(self):
        self.balance=0
        self.name= ''
       
    def welcome(self):
        self.name = input('Welcome to your Bank Account. Please Enter your name : ')

    def currentBalance(self):
        print(f'\nYour Current Balance : {self.balance}')

    def deposit(self):
        amount=int(input('Enter the amount to deposit:'))
        print(f"\nYou deposit {amount}")
        self.balance+=amount
        print(f'{self.name}, your New Balance: {self.balance}')

        
    def withdraw(self):
        amount=int(input('Enter the amount to withdraw:'))
        print(f"\nYou deposit {amount}")
        if(amount>self.balance):
            print('Not enough money in your account')
            print('Enter another amount...')
        else:
            self.balance-=amount
            print(f'{self.name}, your Remaining Balance: {self.balance}')
        

if __name__ == '__main__':
    account = Account()
    account.welcome()

    while True:
        print("\nWhat do you want to do? ")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Current Balance")
        print("4. Exit")
        choice = int(input(">> "))

        if choice == 1:
            account.withdraw()
        elif choice == 2:
            account.deposit()
        elif choice == 3:
            account.currentBalance()
        elif choice == 4:
            exit(0)
        else:
            print("Invalid choice...")
