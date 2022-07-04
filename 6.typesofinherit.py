class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("I am  vehicle")
        print("Mileage is ", self.mileage)
        print("Cost of the vehicle is ", self.cost)

obj = Vehicle(200, 20000)
obj.show_details()

class Car(Vehicle):
    def __init__(self, mileage, cost, hp, tyres):
        super().__init__(mileage, cost)
        self.hp=hp
        self.tyres=tyres

    def show_car(self):
            print("Nnumber of tyres in a car", self.tyres)
            print("Horse power in car", self.hp)
            print("I am a car ")
d1 = Car(250, 14000, 300, 4)
d1.show_details()
d1.show_car()
