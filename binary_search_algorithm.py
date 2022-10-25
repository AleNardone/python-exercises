import random
import numpy as np

random_numbers = np.random.randint(1,101,30)

print("Let's see if your number is in the list.")
value = int(input("Enter a number: "))

#1. First Method - Simple

#middle_number=len(random_numbers)//2
#first_part=random_numbers[:middle_number]
#second_part=random_numbers[middle_number+1:]

#if value == middle_number:
#    print(f"The number {value} is in the middle of the list!!!")
#elif value in first_part:
#    print(f"The number {value} is in the first part of the list!!!")
#elif value in second_part:
#    print(f"The number {value} is in the second part of the list!!!")
#else:
#    print(f"The number {value} is not in the list... Better luck next time...")

2. Binary Search Algorithm

high = len(random_numbers) - 1
low = 0

def binarySearch(random_numbers, value, low, high):
    while low <= high:
        middle_number = low + (high - low)//2
        if value == random_numbers[middle_number]:
            return middle_number
        elif value > random_numbers[middle_number]:
            return binarySearch(random_numbers, value, middle_number + 1, high)
            high = middle_number - 1
        elif value < random_numbers[middle_number]:
            return binarySearch(random_numbers, value, low, middle_number - 1)
            low = middle_number + 1 
        
    return -1

result = binarySearch(random_numbers, value, low, high)

if result != -1:
    print(f"Your number {value} is in the list!!!")
else:
    print(f"Your number {value} is not in the list!!!")

if __name__ == '__main__':
    result






