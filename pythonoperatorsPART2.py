num1 = 23
num2 = 11
num3 = 1

if num1 and num2 and num3 > 0:
    print("all of the numbers are greater then 0")
else:
    print("there is a number less than zero in this list")

a = 34
b = -45
c = 21

if a or b or c > 0:
    print("some of the numbers are greater than 0")
else:
    print("none of the numbers are greater than 0")

a1 = 12
b1 = 8

if (b1 == 12) != (a1 == 12):
    print("welcome")
else:
    print("see you soon!")

c1 = "hello"
d1 = "welcome"

if c1 != d1:
    print(c1,"and",d1)

weight = float(input("write your weight in kgs: "))
height = float(input("write your height in m: "))

bmi = weight/(height**2)
if bmi < 18.4:
    print("you are underweight")
elif bmi < 24.9:
    print("you are normal")
elif bmi < 29.9:
    print("you are overweight")
elif bmi < 39.9:
    print("you are obese")
else:
    print("you are severly obese")