file = open("fibonacci.txt", "w")

def fibonacci(x):
    if x <=1:
        return x
    else:
        return (fibonacci(x-1) + fibonacci(x-2))

terms = int(input("How many terms: "))
if terms <=0:
    print("Enter a positive number please")
else:
    list = []
    (f"\nFibonacci Sequence upto {terms}: ")
    for i in range(terms):
        list.append(fibonacci(i))
    print(list)
        
file.write(str(list))
file.close()

