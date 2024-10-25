try:
    age = int(input("write your age: "))
    if age % 2 == 0:
        print("your age is even")
    else:
        print("your age is odd")
except ValueError:
    print("A ValueError occured!")
