User = input("type if you have a medical cause: ")
attendance = int(input("write your attendance percentage: "))
if User == "Y":
    print("You are allowed to go to your exam!")
else:
    if attendance >= 70:
        print("you are a allowed to go because of your attendance!!!")
    else:
        print("you are not allowed to go unfortunatly!")

Units = int(input("How many units do you consume? "))

if Units <= 50:
    amount = Units*2.60
    tax = 25
elif Units <= 100:
    amount = 130 + ((Units - 50)*3.25)
    tax = 35
elif Units <= 200:
    amount = 130 + 162.50 + ((Units - 100)*5.26)
    tax = 45
else:
    amount = 130 + 162.50 + 526 + ((Units - 200)*8.45)
    tax = 55

total_amount = tax + amount
print("the total amount is: ",total_amount)

print("what type of vehicle do you use?")
print("1.bike ")
print("2.car ")
Choice = input("choose one: ")

if Choice == "1":
    print("what type of bike?")
    print("1.baby bike ")
    print("2.adult bike ")
    Choice2 = input("choose another one: ")
    if Choice2 == "1":
        print("you have selected the baby bike!")
    else:
        print("you have selected the adult bike!")
elif Choice == "2":
    print("which type of car?")
    print("1.sedan")
    print("2.Toyota")
    Choice22 = input("Choose a car: ")
    if Choice22 == "1":
        print("you have selected a sedan")
    else:
        print("you have selected a toyota")
