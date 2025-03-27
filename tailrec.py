def tailrecursion(n, num):
    if n>num:
        return
    tailrecursion(n+1,num)
    print(n)

n = int(input("Enter a number: "))
tailrecursion(1,n)