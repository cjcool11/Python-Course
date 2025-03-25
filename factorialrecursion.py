def fac(n):
    if(n==1 or n==0):
        return 1
    return n*fac(n-1)

n = int(input("Enter a number: "))
print("the factorial of ",n,"is",fac(n))