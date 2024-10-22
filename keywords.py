word = input("write a random word: ")

for i in word:
    if i == "a" or i == "A":
        print("your word has the letter A")
        break
    else:
        print("your word does not have an a")    


#number = int(input("write a number: "))

for number in range(30):
    if number % 20 == 0:
        print("bread")
    elif number % 15 == 0:
        print("hmmm")
    elif number % 10 == 0:
        print("cheese")
    elif number % 5 == 0:
        pass
    elif number % 3 == 0:
        print(number)
    else:
        pass

num = 10

for i in range(num,0,-1):
    if i == 5:
        continue
    print(i)

bill = int(input("write your bill amount: "))

payamount = int(input("write how much you payed: "))


    

        