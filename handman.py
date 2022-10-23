import random
from wordshangman import words
import string




def getRandomWord(words):
    # Return a random word
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)

    return word.upper()         

def guessingWord():
    tries=7
    print("LET'S START")
    print(f"You have {tries} tries to guess the word")
    print("\n")

    word= getRandomWord(words)
    word_letters= set(word) #letters in the word
    alphabet= set(string.ascii_uppercase) #letter of the alphabet
    used_letters = set() #letters used by the user and have guessed

    while len(word_letters) > 0 and tries > 0:
        #letters used by the user
        print(f"You have {tries} tries left and used this letters: ",' '.join(used_letters))
        
        #current word
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_guess= input("Guess a letter: ").upper() #Ask the user for a letter
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)

            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print("")
            elif user_guess not in word_letters:
                if tries==0:
                        print('         _____ ')
                        print('         |   | ')
                        print('         O   | ')
                        print('        /|\  | ')
                        print('        / \  | ')
                        print('             | ')
                        print('     ________|_')
                
                if tries==1:
                        print('         _____ ')
                        print('         |   | ')
                        print('         O   | ')
                        print('        /|\  | ')
                        print('        / \  | ')
                        print('             | ')
                        print('     ________|_')
                
                if tries==2:
                        print('         _____ ')
                        print('         |   | ')
                        print('         O   | ')
                        print('        /|\  | ')
                        print('        /    | ')
                        print('             | ')
                        print('     ________|_')
                
                if tries==3:
                        print('         _____ ')
                        print('         |   | ')
                        print('         O   | ')
                        print('        /|\  | ')
                        print('             | ')
                        print('             | ')
                        print('     ________|_')
                
                if tries==4:
                        print('         _____ ')
                        print('         |   | ')
                        print('         O   | ')
                        print('         |   | ')
                        print('             | ')
                        print('             | ')
                        print('     ________|_')
                
                if tries==5:
                        print('         _____ ')
                        print('         |   | ')
                        print('         O   | ')
                        print('             | ')
                        print('             | ')
                        print('             | ')
                        print('     ________|_')
                
                if tries==6:
                        print('         _____ ')
                        print('         |   | ')
                        print('             | ')
                        print('             | ')
                        print('             | ')
                        print('             | ')
                        print('     ________|_')
                
                if tries==7:
                        print('         _____ ')
                        print('             | ')
                        print('             | ')
                        print('             | ')
                        print('             | ')
                        print('             | ')
                        print('     ________|_')
                
                tries -= 1 #If it's wrong, take away a try
                print(f"Wrong guess... You have {tries} tries now")
                

        elif user_guess in used_letters:
            print("You already used that letter. Try another one.")

        else:
            print("Invalid letter... Try again")

    if tries == 0:
      print(f"You lost... sorry. The word was: {word}")
    else:
      print(f"You guessed the word {word}!! ")

guessingWord()



    
   
    





