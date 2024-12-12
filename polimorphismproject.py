from abc import ABC, abstractmethod

class cars(ABC):
    def carinformation(self):
        pass

class BMW(cars):
    def carinformation(self):
        print("I have a 654 horsepower, V6 engine and I am an m3!")

class ferrari(cars):
    def carinformation(self):
        print("i have a 768 horsepower, V8 engine!")

M3BMW = BMW()
M3BMW.carinformation()

ferrari1998 = ferrari()
ferrari1998.carinformation()

