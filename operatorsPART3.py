Y = input("Write a word: ")
if "hello" in Y:
    print("HI")
else:
    print("whats up")

B = input("Write another word: ")
if "nice to meet you" in B:
    print("Nice to meet you too")
else:
    print("pizza and cheeseburger")

x = "that"
z = "that"

if x is z:
    print("hello")
else:
    print("ice cream")

x1 = 765
z1 = 876

print("x1<<1 ",x1<<1)
print("x1>>1 ",x1>>1)
print("z1<<2",z1<<2)
print("z1>>2",z1>>2)

U = int(input("Write your grade here: "))
if U >= 90 and U <= 100:
    print("you are getting an A+")
elif U >= 85 and U < 90:
    print("you got an A")
elif U >= 60 and U < 85:
    print("you got an A-")
elif U >= 35 and U < 60:
    print("you got below average")
else:
    print("you failed your school year, unfortunately ")