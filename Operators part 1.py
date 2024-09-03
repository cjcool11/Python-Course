#Activity 1
tree1 = 65
tree2 = 83
tree3 = 21
tree4 = 38
tree5 = 11

sum = tree1+tree2+tree3+tree4+tree5

average = sum/5

print("the average height of trees is: ", average)
#Activity 2

amount =int(input("type a random number"))

note_500 = amount//500
note_200 = (amount%500)//200
note_100 = ((amount%500)%200)//100

print("The 500 AED  is: ",note_500)
print("The 200 AED  is: ",note_200)
print("The 100 AED  is: ",note_100)

#Activity 3
mark1 = int(input("write your math mark in numbers here: "))
mark2 = int(input("write your science mark in numbers here: "))
mark3 = int(input("write your english mark in numbers here: "))

sum = mark1+mark2+mark3

percentage = (sum/300)*100

print("All your marks in total are: ",sum )
print("Your percentage of your score is: ",percentage )