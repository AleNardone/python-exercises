import random

def menu():
    print("\n***** MENU *****")
    print("1. GAME")
    print("2. EXIT")
    choice = int(input("Choice: "))

    if choice == 1:
        game()
    elif choice == 2:
        exit(0)
    else:
        print("\nInvalid choice... Try again")
        menu()


def game():
    actions = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(actions)
    user = str(input("Rock, Paper, Scissors: "))
    print("\nUser | {} *** Computer | {}\n".format(user.capitalize(), computer))
    
    while True:
        if user == 'Rock' or user == 'rock':
            if computer == 'Rock':
                print("Tie!")
            elif computer == 'Paper':
                print("Computer wins this round...")
            elif computer == 'Scissors':
                print("You win this round!!!")
            else:
                print("Wrong choice... Try again!")

        elif user == 'Paper' or user == 'paper':
            if computer == 'Paper':
                print("Tie!")
            elif computer == 'Scissors':
                print("Computer wins this round...")
            elif computer == 'Rock':
                print("You win this round!!!")
            else:
                print("Wrong choice... Try again!")

        elif user == 'Scissors' or user == 'scissors':
            if computer == 'Scissors':
                print("Tie!")
            elif computer == 'Rock':
                print("Computer wins this round...")
            elif computer == 'Paper':
                print("You win this round!!!")
            else:
                print("Wrong choice... Try again!")

        play_again = str(input("\nPlay again? (y/n): \n"))
        if play_again == 'y' or play_again == 'Y':
            menu()
            


if __name__ ==  '__main__':
    menu()