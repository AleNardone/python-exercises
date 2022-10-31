import string
from random import *

name = input("Name: ")
number = input("Favorite number: ")
country = input("Favorite country: ")
punctuation = input("Symbol that you like: ")
food = input("Favorite food: ")

selection = name + number + country + punctuation
#characters = string.ascii_letters + string.punctuation  + string.digits

print("How many characters do you want in your password? ")
min= int(input("Min characters (Please remember that a password can't be too short): "))
max= int(input("Max characters (Please remember that a password can't be too long): "))
password =  "".join(choice(selection) for i in range(randint(min, max)))
print(password)
