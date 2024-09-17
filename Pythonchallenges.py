name = "abdullah"
age = 12

if (name == "jack") and ( name == "abdullah" or age <= 12):
    print("ice cream")
else:
    print("burger")

a = 35
b = 46
c = 78
if ((a + b)**(c + a))== 566:
    print("(35 + 46)**(78 + 35)=", 566)
else:
    print("(35 + 46)**(78 + 35)=", (a + b)**(c + a))

UserNumber = int(input("type a number: "))
UserNumber2 = int(input("type another number: "))

if UserNumber % UserNumber2 == 0:
    print("Your number is divisible by: ",UserNumber2)
else:
    print("Your number is not divisible by: ",UserNumber2)

mean1 = 33
total_numbers = 2
wrong = 11
correct = 15
sum1 = mean1 * total_numbers
print("the wrong sum was: ",sum1)
sum2 = sum1 - (wrong - correct)
print(sum2)
mean2 = sum2/total_numbers
print("the correct mean value is",mean2)