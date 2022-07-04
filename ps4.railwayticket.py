class Train:
    def __init__(self, name, fare, seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def Train_details(self):
        print(f"The name of the train is{self.name}")
        print(f"The seats available are {self.seats}")
    def fareinfo(self):
        print(f"The fare of the train is {self.fare}")
    def bookticket(self):
        if(self.seats>0):
            print(f"Your tickets has been booked")
            self.seats=self.seats-1
        else:
            print(f"Sorry please try in tatkal ")
    
    
intercity= Train("Intercity", 200, 300)
intercity.Train_details()
intercity.fareinfo()
intercity.bookticket()
intercity.bookticket()
intercity.Train_details()

