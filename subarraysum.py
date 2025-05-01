def SubArraySum(a,n,sum_):
    for i in range(n):
        curr_sum = a[i]
        j = i+1
        while j <= n:
            if curr_sum == sum_:
                print("Sum found between: ")
                print("indexes % d and % d"%(i ,j-1))
                return 1
            if curr_sum > sum_ or j == n:
                break
            curr_sum = curr_sum + a[j]
            j+=1
    print("No subarray found!")
    return 0

a = [5,4,10,23,89]
sum = 19
n = len(a)
SubArraySum(a,n,sum)
