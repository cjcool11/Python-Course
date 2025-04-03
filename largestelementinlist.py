def largestelement(a):
    Length = len(a)
    if Length == 1:
        return a[0]
    return max(a[0],largestelement(a[1:]))

a = [566,888,1000]

print("The largest element in your list is: ",largestelement(a))