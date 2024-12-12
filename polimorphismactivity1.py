from abc import ABC, abstractmethod

class organisms(ABC):
    def move(self):
        pass

class Human(organisms):
    def move(self):
        print("I can walk, run and sprint!")
    
class Cat(organisms):
    def move(self):
        print("I can also walk, run and sprint!")

class frog(organisms):
    def move(self):
        print("I can jump really high and walk on walls!")

class crab(organisms):
    def move(self):
        print("I can crawl sideways!")

kai = Human()
kai.move()

marshmallow = Cat()
marshmallow.move()

jumpy = frog()
jumpy.move()

crawly = crab()
crawly.move()

