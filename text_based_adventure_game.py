import os
import time

teddy=0

required=("\nUse only A or B") #Options available

def intro():
    print("****** WELCOME TO THE ADVENTURE GAME *****")
    print("Let's have some fun!")
    time.sleep(3)
    print("First...")
    name= input("What is your name? ")
    print("Ok {}... We are ready... LET'S BEGIN!".format(name))
    time.sleep(1)
    os.system("cls")

    print("""You wake up in your bedroom in the middle of the night... You hear a strange noise outside the house.
When you decided to see what was going on, you saw a gaint monster coming to your house""")
    time.sleep(1)
    print("OH NO! You have two choices... A. You stay in your room or B. You go out of your room.")
    choice= input("A or B: ").upper()

    if choice == 'A':
        print("You should have gone out of your room... Th monster came to your room... You died!")
        os.system("cls")
        print("GAME OVER!")
        exit(0)
    elif choice == 'B':
        exit_room()
    else:
        print(required)
        intro()

def exit_room():
    print("Good choice! Let's continue...")
    os.system("cls")
    time.sleep(1)
    print("You are walking down the hallway when you see a teddy bear.")
    print("What do you do? A. You pick it up or B. You leave it there")
    choice=input("A or B: ").upper()

    if choice=='A':
        teddy=1
    else:
        teddy=0

    print("You run and hide behind a big sofa")
    os.system("cls")
    
    if teddy==1:
        print("Suddendly the teddy bear start to talk to you... What's going on?")
        time.sleep(3)
        print("He started to tell you a secret that can help you beat the monster!")
        beat_monster()
    elif teddy<1:
        print("You should have picked the teddy bear... The monster found you... You died!")
        os.system("cls")
        print("GAME OVER!")
        exit(0)
    else:
        print(required)
        exit_room()
    
def beat_monster():
    print("You decided to trust the teddy and fight the monster... You are so brave!")
    time.sleep(3)
    print("You go out and walk in front of the monster and throw to his direction a magical potion. But... did it hit him or not?")
    choice=input("A or B: ")

    if choice=='A':
        print("It hits the monster and suddendly he started to fell asleep")
        print("NOW IT'S YOUR CHANCE!")
        time.sleep(5)
        print("You could run away from the monster! ")
        print("YOU WON!")
        exit(0)
    elif choice=='B':
        print("OH NO! You throw the potion over the monster's head...")
        print("The monster came in your direction... You died!")
        os.system("cls")
        print("GAME OVER!")
        exit(0)
    else:
        print(required)
        beat_monster()

intro()



