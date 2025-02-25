def sieveoferatosthenes(num):
    prime = [True for i in range(num+1)]

    currentnumber = 2
    while (currentnumber*currentnumber<=num):
        if (prime[currentnumber] == True):
            for i in range(currentnumber**2, num+1, currentnumber):
                prime[i] = False
        currentnumber+=1
    prime[0] = False
    prime[1] = False
    for p in range(num + 1):
        if prime[p]:
            print(p)

num = int(input("enter the number to find the prime numbers less or equal to it: "))
sieveoferatosthenes(num)
print("following are the numbers smaller than or equal to ")
