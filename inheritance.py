class father:
    def __init__(self,hair,strong):
        self.hair = hair
        self.strong = strong

    def display(self):
        print("dad has ",self.hair,"hair")
        print("dad is strong!",self.strong)

class child(father):
    def __init__(self,name,age,hair,strong):
        self.name = name
        self.age = age
    
        super().__init__(hair,strong)

obj = child("Zack",12,"brown",True)
obj.display()



