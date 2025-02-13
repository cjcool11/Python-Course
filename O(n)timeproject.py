def myfunction(n):
    iterations = 0
    for i in range(0, n+1):
        print("First Loop")
        iterations += 1
        print("this is the number of iterations: ", iterations)        

    iterations2 = 0  
    j = 1
    while(j <= n+1):
        print("Second Loop", j)
        j = j * 2
        iterations2 += 1
        print("this is the number of iterations: ", iterations2)

    print("Total iterations in the first loop: ", iterations)
    print("Total iterations in the second loop: ", iterations2)

    iterations3 = 0  
    for i in range(0, 100):
        print("Third Loop")
        iterations3 += 1
        print("the number of iterations is: ", iterations3)

    print("Total iterations in the third loop: ", iterations3)

myfunction(5)
