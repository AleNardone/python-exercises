from random import randint

number = randint(0,51) #Random number between 0 and 50
chances=5 #Chances to guess the name
count=0 

guess = int(input("Guess the number I thinking between 0 and 50: " ))

while count < chances: 
        
    if guess == number:
       print(f"CONGRATS! You guessed the number in {count} tries") 
       break
    if guess < number:
       print("Your number is too low. Guess higher!")
       guess = int(input("Try again: "))
    if guess > number:
       print("Your number is too high. Guess lower!")
       guess = int(input("Try again: "))

    count+=1 #Every time you try to guess the name, the count variable is going to increase

if count == chances:
    print("GAME OVER")
    print("The number that I was thinking was %d" % number)
    print("Better luck next time!")
