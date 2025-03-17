def computepwr(x, y):
    result = 1
    while(y>0):
        if(y%2==0):
            x=x*x
            y>>=1
        else:
            result=result*x
            y = y-1
    return result

x = int(input("Enter x for y^x: "))
y = int(input("Enter y for y^x: "))
print("Total = ",computepwr(x, y))