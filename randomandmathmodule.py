import random
#playing = True
#print("i am guessing a number between 0 and a 100")

#computernum = str(random.randint(0,100))
#while playing:
#    usernum = input("write your guess: ")
#    if usernum == computernum:
#        print("you succesfully guessed my number!!!")
#        break
#    else:
#        print("not quite right!")

options = ["Rock","Paper","Scissors"]
competitor = random.choice(options)
ucerchoice = input("write your choice: ")
print("computerchoice is: ",competitor)

if ucerchoice == "Rock" and competitor == "Scissors":
    print("good job! Player")
elif ucerchoice == "Paper" and competitor == "Rock":
    print("good job!")
elif ucerchoice == "Scissors" and competitor == "Paper":
    print("good job!")
elif ucerchoice == competitor:
    print("Awww its a Tie!")
else:
    print("i think i won!")

import math
x = 26
y = 10

z = 23.58
a1 = 10.45

result1 = str(math.gcd(x,y))
print("the gcd of x and y is: ",result1)

result1 = math.ceil(z)
print("x and y ceiled are: ",result1)

result1 = math.floor(x)
print("x floored is: ",result1)

result1 = math.factorial(y)
print("the factorial of y is: ",result1)

result1 = math.copysign(x,y)
print("x and y copysighned are: ",result1)

result1 = math.isnan(x)
print("is x nan: ",result1)