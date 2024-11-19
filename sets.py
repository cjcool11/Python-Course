
setA = {1,3,5,5,7,7}
print(setA)

setB = {5,"pizza",4,(123,45,7)}
print(setB)

setC = {1, 2, 3, 4, 3, 2 ,4}
print(setC)

setD = set([1, 2, 3, 2])
print("this is the set before removing a random element: ")
print(setD)
setD.pop()
print("this is the set after popping a random element: ")
print(setD)

set1 = {"green","blue"}
set2 = {"blue","yellow"}
intersect = set1.intersection(set2)
print("this is the intersection of set1 and set2",intersect)