try:
    num = int(input("write a number: "))
    print("your number was: ",num)
except ValueError as V:
    print("your error is: ",V)


try:
    num1 = int(input("write a dividend number: "))
    num2 = int(input("write the divisor: "))
    result = num1/num2
    print("this is the result: ",result)
except ZeroDivisionError:
    print("no zeros please!")
except ValueError:
    print("who said alphabets are allowed?!")
except NameError as N:
    print("the error is: ",N)
except:
    print("There was an unknown error")
finally:
    print("I am  always here!")


try:
    A = int(input("write the number: "))
    while A % 2 == 0 :
        print("bye")
    else:
        print("your number is odd")
except:
    print("Hmmm,an error happened")

    
        

    