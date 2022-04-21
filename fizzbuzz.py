import time

numbercount = input("How many numbers do you want?")
while numbercount.isnumeric() == False:
    numbercount = input("That's not a number, try again:")


for x in range(int(numbercount)):
    x += 1
    if (x % 15) == 0:
        print("Fizzbuzz", str((x)))
        time.sleep(0.3)
    elif x % 3 == 0:
        print ("Fizz", str((x)))
        time.sleep(0.3)
    elif x % 5 == 0:
        print ("Buzz", str((x)))
        time.sleep(0.3)
    else:
        print(x)
        time.sleep(0.3)
