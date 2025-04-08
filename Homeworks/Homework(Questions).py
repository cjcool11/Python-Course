#Reverse With Recursion Lesson:
#Question1:
Name = input("Write your name: ")
print(Name)
#Question2:
Num1 = int(input("Enter a number: "))
Num2 = int(input("Please enter another number: "))
print(Num1+Num2)
#Question3:
Age = int(input("Enter your age: "))
Future_Age = Age + 1
print("You will be: ",Future_Age,"Next Year!!!")
#Recursion problems2:
#Question1
#4. Write a Python program that asks for your favorite color and prints a message with it.
Fav_color = input("Enter your favorite color: ")
print("Wow, I love that color too, its so nice! ",Fav_color,"Is a very loved color.")
#5. Write a Python program that asks for a number and prints its multiplication table from 1 to 10.
Num = int(input("Enter a number to see its multiplication table from 1 to 10: "))
multiplying_num = 1
for i in range(multiplying_num, 11):
    print(Num*multiplying_num)
    multiplying_num+1
#6. Write a Python program that asks for a number and tells if it is even or odd.
even_or_odd = int(input("Enter a number to see if it's even or odd: "))
if even_or_odd % 2 == 0:
    print("Your number is Even!!!!")
else:
    print("Your number is Odd!!!!")