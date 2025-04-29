def maxsumofsubarray(a,a_size):
    max = -9999999999
    cmax = 0
    for i in range(0,a_size):
        cmax = cmax + a[i]
        if(max < cmax):
            max = cmax
        if(cmax<0):
            cmax = 0
    return max

a = [98,-76,120,8,-9]
#length_of_a = len(a)

print(maxsumofsubarray(a,len(a)))
