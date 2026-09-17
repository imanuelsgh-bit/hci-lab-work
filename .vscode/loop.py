"""
import random 

writeFile = open("Demo.txt", "w")

num = random.randint(1, 10)
state = False
while state == False:
    guess = int(input("choose a num from 1 to 10: "))
    if guess < num:
        print("Your guess is too low.")
    elif guess > num:
        print("Your guess is too high.")
    else:
        print("U got correct num.")
        state = True
        num = str(num)
        with open("Demo.txt", "a") as writeFile:
            writeFile.write("Your number is: " + num)
writeFile.close()
"""



varArray = [None] * 10

for i in 10:
    print(varArray[i])