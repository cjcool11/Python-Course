import random

Input1 = int(input("write a number to get swapped: "))
Input2 = int(input("write another number: "))
Input3 = int(input("write another number again: "))

apple = "hello"
orange = "welcome!"

Rando = random.choice(apple)

if Rando == apple:
    print(Input1,"/",Input3,"/",Input2)
else:
    print(Input3,Input1,Input2)
