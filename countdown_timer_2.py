import time

def countdown(t):
    while t:
        min, s = divmod(t,60) #min = t/60 and s=t%60.
                              # Example: 80 seconds -> min=1 and s=20
        timer = "{:02d}:{:02d}".format(min,s)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print("Over!")

t = input("Enter the time in seconds: ")

countdown(int(t))

        
