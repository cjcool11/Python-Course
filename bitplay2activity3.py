def twoodd(arr, size):
    xorof2 = arr[0]
    x= 0
    y= 0
    #set bit = 0
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]

    setbit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

        print("the two ODD elements are: ",x,"&",y,)


arr = []

arraysize = int(input("enter array size: "))
for i in range(0, arraysize):
    z = int(input("Enter an element"))
    arr.append(z)

twoodd(arr,arraysize)





