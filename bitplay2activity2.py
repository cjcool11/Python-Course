def equalornot(number1,number2):
    if ((number1^number2)!=0):
        print("numbers are not equal")
    else:
        print("numbers are equal")

number1 = int(input("Enter a number: "))
number2 = int(input("enter another number: "))

equalornot(number1,number2)
