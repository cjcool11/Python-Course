Rows = int(input("write the number of rows"))

for i in range(Rows):          
    for j in range(i+1):
        print("*",end="  ")
    print()

print("                              ")

for i in range(Rows):
    for j in range(Rows - i - 1):
        print(" ", end="  ")
    for j in range(i + 1):
        print("*", end="  ")
    print()
