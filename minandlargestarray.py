def minimumelement(a,size):
    temp = a[0]
    for i in range(1,size):
        temp = min(temp,a[i])
    return temp

def maximumelement(a,size):
    temp = a[0]
    for i in range(1,size):
        temp = max(temp, a[i])
    return temp

array = [12,66,99,1212,98987]
array_size = len(array)
print("Minimum element: ",minimumelement(array,array_size))
print("Maximum element: ",maximumelement(array,array_size))
