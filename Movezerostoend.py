def MoveZerosToTheEnd(a,a_size):
    zero = 0
    nonzero = 0
    while (nonzero!=a_size):
        if a[nonzero] != 0 :
            a[nonzero],a[zero] = a[zero],a[nonzero]
            zero+=1
        nonzero+=1

a = [0,0,0,0,1,0,3,2,0,0,1,2]
a_length = len(a)
print(a)
MoveZerosToTheEnd(a,a_length)
print("Array after zeros are moved: ",a)