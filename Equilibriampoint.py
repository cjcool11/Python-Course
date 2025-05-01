def equilibriampointfunc(a):
    leftsidesum = 0
    rightsidesum = 0
    n = len(a)
    for i in range(n):
        leftsidesum = 0
        rightsidesum = 0
        for j in range(i):
            leftsidesum += a[j]
        for j in range(i+1,n):
            rightsidesum += a[j]
        if rightsidesum == leftsidesum:
            return i
    return -1

a = [2,3,5,1,0,5,6]
print("Equilibriam point: ",a[equilibriampointfunc(a)])