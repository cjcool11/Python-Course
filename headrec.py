def headrecursion(n, num):
    if n>num:
        return
    print(n)
    headrecursion(n+1,num)

n=int(input("Enter a number: "))
headrecursion(1, n)