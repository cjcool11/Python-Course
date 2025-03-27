def increasinganddecreasing(n, num):
    if(n<1 or n>num):
        return
    print(n)
    increasinganddecreasing(n-1,num)
    print(n)

n = int(input("Enter a number: "))
increasinganddecreasing(n,n)