class employee:
    def __init__(self):
        print("employee created!")
    
    def __del__(self):
        print("employee destructed")

    def create_obj(self):
        print("creating object...")
        obj = "employee"
        print("function end!")
        return obj
    
print("calling functions(s)")
obj = employee()
obj.create_obj()
print("program ending...")

