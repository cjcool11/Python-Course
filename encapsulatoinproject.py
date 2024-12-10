#teacher, i know that the special functions are innecessary, but i have to use them to make this program realted to waht we learned!
class revstr:
    def __reversestr__(self):
        word = input("write any word here: ")
        revstr1 = word[::-1]
        print("this is the word in reverse: ",revstr1)

obj = revstr()
obj.__reversestr__()