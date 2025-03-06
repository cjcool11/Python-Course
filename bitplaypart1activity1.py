def SetOrNot(num, n):
    if (num & 1 << (n - 1)):
        print("\nSet")
    else:
        print("\nNot Set")
    
num = int(input("Enter a number: "))
n = int(input("enter bit number: "))
SetOrNot(num, n)