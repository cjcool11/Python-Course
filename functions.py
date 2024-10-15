def well_wishes():
    print("what is up?")

well_wishes()

def weather():
    print("the weather is nice in ",summer)
    print("the weather is cool in ",winter)

summer = "winter"
winter = summer

weather()

print("what do you want to calculate 1.multiply 2.divide 3.subtract 4.add")

user = int(input("answer: "))

num1 = int(input("write your number: "))
num2 = int(input("write your second number: "))

def add(num1,num2):
    res = num1 + num2
    return res

def subtract(num1,num2):
    res = num1 - num2
    return res

def multiply(num1,num2):
    res =num1 * num2
    return res

def divide(num1,num2):
    res = num1 / num2
    return res

if user == 1:
    print(multiply(num1,num2))
elif user == 2:
    print(divide(num1,num2))
elif user == 3:
    print(subtract(num1,num2))
elif user == 4:
    print(add(num1,num2))
else:
    print("invalid input")


