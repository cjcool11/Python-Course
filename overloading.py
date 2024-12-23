class Points():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y


p1 = Points(4,6)
p2 = Points(1,4)
p3 = p1 + p2

print(p3)