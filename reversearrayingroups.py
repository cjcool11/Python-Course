def reverse(a,a_size,n):
    temp = 0
    while (temp<a_size):
        start = temp
        end = min(temp+n-1,a_size-1)
        while (start < end):
            a[start],a[end]=a[end],a[start]
            start +=1;
            end-=1
        temp += n

a = [12,67,89,98,100,144]
print("Original array: ",a)
n=2
a_size = len(a)


reverse(a,a_size,n)
print("Reversed array:")

for i in range(0,a_size):
    print(a[i],end = " ")
 