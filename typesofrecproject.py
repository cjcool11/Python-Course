def negativeornot(n):
    n = int(input("Enter a number: "))
    if n<1:
        print("Good Job!")
    else:
        negativeornot(n)

n = int(input("enter a number: "))
negativeornot(n)

    
    
