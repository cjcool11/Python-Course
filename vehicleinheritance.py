class bus:
    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

class childbus(bus):
    pass
    #def __init__(self,name,speed,mileage):
        #self.color = color
        #super().__init__(name,speed,mileage)
    #def display(self):
        #print("this bus color is ",childbus.color)
        #print("this bus name is ",childbus.name)
        #print("this bus maxspeed is ",childbus.speed)
        #print("this bus mileage is ", childbus.mileage)

obj = childbus("Volvo bus",80,120)

print("childbus name is ",obj.name)
print("childbus maxspeed is ",obj.speed)
print("childbus mileage is ",obj.mileage)