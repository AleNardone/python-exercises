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
    user = str(input("\nRock, Paper, Scissors: "))
    print("\nUSER *** COMPUTER\n")
    options(computer, user)
    
    user_score = 0
    computer_score = 0
    rounds = 1

    while rounds < 3:
        if user == 'Rock' or user == 'rock':
            if computer == 'Rock':
                print("Tie!")
            elif computer == 'Paper':
                print("Computer wins this round...")
                computer_score += 1
            elif computer == 'Scissors':
                print("You win this round!!!")
                user_score += 1
            else:
                print("Wrong choice... Try again!")
                game()

        elif user == 'Paper' or user == 'paper':
            if computer == 'Paper':
                print("Tie!")
            elif computer == 'Scissors':
                print("Computer wins this round...")
                computer_score += 1
            elif computer == 'Rock':
                print("You win this round!!!")
                user_score += 1
            else:
                print("Wrong choice... Try again!")
                game()

        elif user == 'Scissors' or user == 'scissors':
            if computer == 'Scissors':
                print("Tie!")
            elif computer == 'Rock':
                print("Computer wins this round...")
                computer_score += 1
            elif computer == 'Paper':
                print("You win this round!!!")
                user_score += 1
            else:
                print("Wrong choice... Try again!")
                game()
        
        rounds += 1
        computer = random.choice(actions)
        user = str(input("\nRock, Paper, Scissors: "))
        print("\nUSER *** COMPUTER\n")
        options(computer, user)
                
    else:
            print(f"\nUSER SCORE: {user_score}")
            print(f"COMPUTER SCORE: {computer_score}")
            if user_score > computer_score:
                print("You win!!!")
                play_again = str(input("\nPlay again? (y/n): \n"))
                if play_again == 'y' or play_again == 'Y':
                    menu()
                else:
                    exit(0)
            elif user_score < computer_score:
                print("The computer wins...")
                play_again = str(input("\nPlay again? (y/n): \n"))
                if play_again == 'y' or play_again == 'Y':
                    menu()
                else:
                    exit(0)
            else:
                print("It's a tie!")
                play_again = str(input("\nPlay again? (y/n): \n"))
                if play_again == 'y' or play_again == 'Y':
                    menu()
                else:
                    exit(0)
    
def options(computer, user):
    if (user == "Rock" or user == "rock"):           
          print("\nUser: {}\n".format(user.capitalize()))
          print("    _______")
          print("---'  _____)")
          print("     (_____)")
          print("     (_____)")
          print("     (_____)")
          print("---.__(____)")

          if(computer == "Rock" or computer =="rock"):
              print("\nComputer: {}\n".format(computer))
              print("    _______")
              print("---'  _____)")
              print("     (_____)")
              print("     (_____)")
              print("     (_____)")
              print("---.__(____)")

          elif (computer == "Paper" or computer =="paper"):
             print("\nComputer: {}\n".format(computer))
             print("    _____)___")
             print("---'_________)")
             print("      ________)")
             print("     ________)")
             print("     ________)")
             print("---._______)")

          elif (computer == "Scissors" or computer =="scissors"):
             print("\nComputer: {}\n".format(computer))
             print("    _______")
             print("---'   ____)____")
             print("          ______)")
             print("      __________)")
             print("      (____)")
             print(" ---._(___)")

    if (user == "Paper" or user == "paper"):       
             print("\nUser: {}\n".format(user.capitalize()))
             print("    _____)___")
             print("---'_________)")
             print("      ________)")
             print("     ________)")
             print("     ________)")
             print("---._______)")

             if(computer == "Rock" or computer =="rock"):
                  print("\nComputer: {}\n".format(computer))
                  print("    _______")
                  print("---'  _____)")
                  print("     (_____)")
                  print("     (_____)")
                  print("     (_____)")
                  print("---.__(____)")

             elif (computer == "Paper" or computer =="paper"):
                 print("\nComputer: {}\n".format(computer))
                 print("    _____)___")
                 print("---'_________)")
                 print("      ________)")
                 print("     ________)")
                 print("     ________)")
                 print("---._______)")

             elif (computer == "Scissors" or computer =="scissors"):
                 print("\nComputer: {}\n".format(computer))
                 print("    _______")
                 print("---'   ____)____")
                 print("          ______)")
                 print("      __________)")
                 print("      (____)")
                 print(" ---._(___)")



    if (user == "Scissors" or user == "scissors"):
             print("\nUser: {}\n".format(user.capitalize()))
             print("    _______")
             print("---'   ____)____")
             print("          ______)")
             print("      __________)")
             print("      (____)")
             print(" ---.__(___)")

             if(computer == "Rock" or computer =="rock"):
                  print("\nComputer: {}\n".format(computer))
                  print("    _______")
                  print("---'  _____)")
                  print("     (_____)")
                  print("     (_____)")
                  print("     (_____)")
                  print("---.__(____)")

             elif (computer == "Paper" or computer =="paper"):
                 print("\nComputer: {}\n".format(computer))
                 print("    _____)___")
                 print("---'_________)")
                 print("      ________)")
                 print("     ________)")
                 print("     ________)")
                 print("---._______)")

             elif (computer == "Scissors" or computer =="scissors"):
                 print("\nComputer: {}\n".format(computer))
                 print("    _______")
                 print("---'   ____)____")
                 print("          ______)")
                 print("      __________)")
                 print("      (____)")
                 print(" ---._(___)")
    


if __name__ ==  '__main__':
    menu()