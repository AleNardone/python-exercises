import os

def menu():
    print("*****   MENU   *****")
    print("1. Why do be have to ride a bicycle?")
    print("2. Let's have lunch at school")
    print("3. The story of Tarzan")

menu()

choice=int(input("\nSelect an option from above: "))
os.system("cls")

if choice == 1:
    print("\nWrite the word to complete the story!")
    one= input("Verb: ")
    two= input("Adjective: ")
    three= input("Verb: ")
    four= input("Part of body: ")
    five= input("Adverb: ")
    six= input("Part of body: ")
    seven= input("Noun: ")
    eight= input("Verb: ")
    nine= input("Animal: ")
    ten= input("Noun: ")
    eleven= input("Verb: ")
    twelve= input("Adjective: ")
    thirdteen= input("Color: ")

    os.system("cls")
    print("\nYour mad lib has been created!")
    print("\n Most doctors agree that the bicycle of {} your is a/an {} form of exercise. {} a bicycle enables you to develop your {} muscles as well as {} increase the rate of a {} beat. More {} around the world {} bicycles than drive {}. No matter what kind of {} you are, always {} sure to wear a/an {} helmet. Make sure to have {} reflectors too!".format(one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirdteen))


    
if choice == 2:
    print("\nWrite the word to complete the story!")
    one= input("Adjective: ")
    two= input("Food: ")
    three= input("Adjective: ")
    four= input("Noun: ")
    five= input("Food: ")
    six= input("Name: ").capitalize()
    seven= input("Noun: ")
    eight= input("Verb: ")
    nine= input("Verb: ")
    ten= input("Verb: ")
    eleven= input("Noun: ")
    twelve= input("Noun: ")
    thirdteen= input("Name: ").capitalize()
    fourteen= input("Food: ")

    os.system("cls")
    print("Your mad lib has been created!")
    print("It was {} day at school, and {} was super {} for lunch. But when she went outside to eat, a {} stole her {}! {} chased the {} all over school. She {}, {}, and {} through the playground. Then she tripped on her {} and the {} escaped! Luckily, {}'s friends were willing to share their {} with her.".format(one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirdteen, fourteen))



if choice == 3:
    print("\nWrite the word to complete the story!")
    one= input("Adjective: ")
    two= input("Noun: ")
    three= input("Adjective: ")
    four= input("Place: ")
    five= input("Plural noun: ")
    six= input("Noun: ")
    seven= input("Funny noise: ")
    eight= input("Adjective: ")
    nine= input("Animal in plural: ")

    os.system("cls")
    print("Your mad lib has been created!")
    print("One of the most important characters in fiction is Tarzan of the {}. Tarzan was raised by a/an {} and lives in the {} jungle in the heart of darkest {}. He spends most of his time eating {} and swinging from tree to {}. Whenever he gets angry, he beats on his chest and says, {}! This is his war cry. His best friend is a/an {} chimpanzee named Cheetah. He is supposed to be able to speak to elephants and {}.".format(one, two, three, four, five, six, seven, eight, nine))
