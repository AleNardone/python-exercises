import numpy as np
import random

numbers =[]
for i in range(100):
    numbers.append(random.randrange(-101,101,1))

positive_num = []
negative_num = []

for number in numbers:
    if number <= 0:
        negative_num.append(number)
    else:
        positive_num.append(number)

file = open('numberlist.txt','w')
file.write(str(negative_num))
file.write(str(positive_num))
file.close()

with open('numberlist.txt', 'r') as file:
    for line in file:
           max_pnumber = max(positive_num)
           min_pnumber = min(positive_num)
           max_nnumber = max(negative_num)
           min_nnumber = min(negative_num)
print(f'Positive list, The max number is: {max_pnumber}, and the min number is: {min_pnumber}')
print(f'Negative list, The max number is: {max_nnumber}, and the min number is: {min_nnumber}')
file.close()




