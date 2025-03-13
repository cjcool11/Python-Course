def oddoccuring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []

n = int(input("enter array size: "))

while(n):
    num = int(input("enter number: "))
    arr.append(num)
    n -=1

print("the one odd occuring is: ",oddoccuring(arr))