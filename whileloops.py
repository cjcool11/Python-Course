n = int(input("write a number: "))
sum = 0
number = 1

while number <= n:
    sum = sum + number
    number += 1
print("sum = ",sum)

# d = 3
# while d > 1:
#     print("hello")
 
number = int(input("write a number: "))
n = 0
temp = number

while temp>0:
    digit = temp%10
    n += digit**3
    temp//=10

if number == n:
    print("your number is an armstrong number")
else:
    print("your number is not an armstrong number")


    
