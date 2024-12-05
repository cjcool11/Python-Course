class Vehicle:
    def __init__(self, name, capacity):
        self.name = name  
        self.capacity = capacity 
    def fare(self):
        return self.capacity * 100  # each bus ride costs 100 to ride

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare() 
        maintenance_fee = base_fare * 0.1  
        return base_fare + maintenance_fee  
    
bus = Bus("Bus", 10)  # The bus can carry 10 people
print(f"The total fare for {bus.name} with {bus.capacity} people is: {bus.fare()}")

