class fruits:
    def __init__(self,name,color):
        self.name = name
        self.color = color

B = fruits("banana","yellow")
O = fruits("orange","orange")

print(B.name)
print(O.color)

class car:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

bugatti = car(445,23)
print(bugatti.maxspeed)
print(bugatti.mileage)

class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

coco = parrot("coco",3)
obob = parrot("obob",5)

print("coco is a {}".format(coco.species))
print("obob is also a{}".format(obob.species))

print("{} is {} years old!".format(coco.name,coco.age))
print("{} is {} years old!".format(obob.name,obob.age))



        