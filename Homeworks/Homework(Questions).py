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
    multiplying_num+=1
#6. Write a Python program that asks for a number and tells if it is even or odd.
even_or_odd = int(input("Enter a number to see if it's even or odd: "))
if even_or_odd % 2 == 0:
    print("Your number is Even!!!!")
else:
    print("Your number is Odd!!!!")
#Recursion problems 3:
#7. Write a Python program that asks for two numbers and then asks the user which operation (addition, subtraction, multiplication, division) to perform, then prints the result.
No1 = int(input("Enter a number to do a math operation on: "))
No2 = int(input("Enter another number: "))

operation = int(input("Enter the operation e.g(1=multiplication, 2=division, 3=addition, 4=subtraction): "))
if operation == 1:
    print(No1*No2)
elif operation == 2:
    print(No1 / No2)
elif operation == 3:
    print(No1+No2)
else:
    print(No1 - No2)
##8. Write a Python program that prints the numbers from 1 to 10 using a loop.
nomber = 1
for i in range(1,11):
    print(nomber)
    nomber+=1
#9. Write a Python program that asks for a word and then prints that word 5 times.

word = input("Enter a word: ")
print(word * 5)

