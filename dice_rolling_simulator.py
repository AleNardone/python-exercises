from random import randint
import time
import os

def roll_dice():
    number= int(randint(1,7))
    os.system("cls")
    print("LOADING...")
    time.sleep(5)
    os.system("cls")
    print(f"The number is {number}\n")
    
    if number == 1:
        print("*********")
        print("*       *")
        print("*   *   *")
        print("*       *")
        print("*********")

    if number == 2:
        print("*********")
        print("* *     *")
        print("*       *")
        print("*     * *")
        print("*********")

    if number == 3:
        print("*********")
        print("* *     *")
        print("*   *   *")
        print("*     * *")
        print("*********")

    if number == 4:
        print("*********")
        print("* *   * *")
        print("*       *")
        print("* *   * *")
        print("*********")

    if number == 5:
        print("*********")
        print("* *   * *")
        print("*   *   *")
        print("* *   * *")
        print("*********")

    if number == 6:
        print("*********")
        print("* *   * *")
        print("* *   * *")
        print("* *   * *")
        print("*********")

roll_dice()


