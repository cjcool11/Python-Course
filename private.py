class class1:
    __privateVar = 12
    def __privatemeth(self):
        print("this private method is in class1")

    def hello(self):
        print("the value of privateVar is ",class1.__privateVar)

obj = class1()
obj.hello()
obj.__privatemeth