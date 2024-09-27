num = int(input("write an integer: "))

sum = 0

for loop in range(1,num + 1):
    sum += loop
    print("sum:",sum)

name = input("write your name: ")

reverse = ""

for i in name:
    reverse = i + reverse
print("your name in reverse is: ",reverse)

num2 = int(input("write another number: "))

for i in range(num2,0,-1):
    print("the numbers in reverse: ",i)

o = int(input("write the first number: "))
x = int(input("write the second number: "))

for i in range(o,x+1,2):
    print(i)


INT = int(input("write a number to calculate: "))
INT2 = int(input("write another number to calculate: "))

Sum = 1

for i in range(1,INT2):
    Sum *= INT
print(Sum)


