def calc(billtotal,tip_perc):
    total = billtotal * (1 + 0.01*tip_perc)
    total = round(total,2)
    print("you need to pay",total)

calc(124,7)

def cube(num):
    return num**3

def divisible(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False
    
num = int(input("write a number: "))

print( divisible(num))

number = int(input("write a number: "))

def factorial(number):
    '''this is the recursive way of finding factorial'''
    if number ==0 or number ==1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial.__doc__)
print("the factorial of 9 is",factorial(9))