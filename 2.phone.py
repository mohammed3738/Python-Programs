class Phone():
    def set_color(self, color):
        self.color=color
    def set_cost(self, cost):
        self.cost=cost
    def show_color(self):
        print(self.color)
    def show_cost(self):
        print (self.cost) 
    def make_calls(self):
        print("making calls")
    def play_games(self):
        print("playing games")
p2 = Phone()
p2.set_color("blue")
p2.set_cost("50000")

p2.show_color()
p2.show_cost()
p2.make_calls()
p2.play_games()






