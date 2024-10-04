word = input("write a word: ")
letter = input("write a letter: ")
b = 0
Count = 0

while (b < len(word)):
    if (word[b] == letter):
        Count += 1
    b += 1

print("the letter",letter,"is found in the word",Count,"times")    

num = int(input("write a number: "))
num2 = int(input("write a second number: "))

for i in range(num,num2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
             print(i)








