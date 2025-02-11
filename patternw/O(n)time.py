def printpattern(n):
    iterations = 0
    for i in range(0,n):
        for j in range(0,n):
            print("$", end=" ")
            iterations += 1
        print("")
    print("when 'n' is: ",n,"iterations = ",iterations,"\n")

printpattern(9)
printpattern(3)
printpattern(10)
printpattern(50)
printpattern(12)
printpattern(19)

print("with every 'n', the time taken is equal to n^2 ")
print("O(n*2)")