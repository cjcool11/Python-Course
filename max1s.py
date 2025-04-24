def maxones(a,a_size):
    counter = 0
    max1 = 0
    for i in range(0,a_size):
        if (a[i] == 0):
            counter = 0
        else:
            counter+=1
            max1 = max(max1,counter)
    return max1

a = [0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1]
a_length = len(a)

print("The max amount of 1s in an row is: ",maxones(a,a_length))