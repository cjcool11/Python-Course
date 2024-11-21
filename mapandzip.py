numbersA = [2,5,9,10]
numbersB = [6,2,7,11]
adding = map(lambda x,y: x + y, numbersA, numbersB)
print("this is both the lists added together:")
print(list(adding))

nums = [1, 2, 3, 4, 5]
def squarevalue1(n):
    return n*n
squarevalue = list(map(squarevalue1,nums))
print("this is the the numbers' in the list's square value")
print(squarevalue)


#activity 3: exit function
for i in range(0,6):
    if i == 5:
        print("the program is going to exit!")
        exit()
    print(i)