class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("I am a Vehicle")
        print("Mileage of Vehicle is ",self.mileage)
        print("Cost of vehicle is ", self.cost)

e1= Vehicle(200, 4000)
e1.show_details()

class Car(Vehicle):
    def show_car(self):
        print("I am a car")

obj= Car(2000, 12000)
obj.show_details()
obj.show_car()
