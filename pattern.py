Rows = int(input("write the number of rows: "))

for I in range (Rows):
    for j in range(I+1):
        print("*",end=" ")
    print()

Rows = int(input("write the number of rows"))
num = 1
for I in range(Rows):
    for J in range(I+1):
        print(num,end=" ")
        num = num+1
    print()

ROws = int(input("write the number of rows: "))

if ROws%2==0:
    halfdiamrow = int(ROws/2)
else:
    halfdiamrow = int(ROws/2)+1
space = halfdiamrow-1
for i in range(1,halfdiamrow+1):
    for j in range(1,space+1):
        print(end=" ")
    space = space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print( )
space=1
for i in range(1,halfdiamrow):
    for j in range(1,space+1):
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1,2*(halfdiamrow-i)):
        print(end=str(num))
        num = num+1
    print( )





