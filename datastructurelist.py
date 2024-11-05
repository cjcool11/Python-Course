list1 = ["a","b","c"]
list2 = []
list3 = ["lemon","apple","food"]

list3.reverse()
print(list1*4)
print(list1[::-1])
print(list3)

def lettersmatching(words):
    count = 0
    lst = []
    for i in words:
        if len(i)>1 and i[0] == i[-1]:
            count += 1
            lst.append(i)
    print("list of words that have the first and last letter the same/n",lst)
    return count
c = lettersmatching(["anna","hello","oppo"])
print("list of words that have the same first letter and last letter are",c)
