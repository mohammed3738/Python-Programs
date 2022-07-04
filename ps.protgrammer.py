class Programmer:
    comapny="google"
    print('The company name is',comapny)

    def __init__(self, name, product):
        self.name=name
        self.product=product
    def show_details(self):
        print(f"The name of the prorammer is {self.name} and the product on which he is working is {self.product} ")

mohammed=Programmer("mohammed", "skype")
ibrahim=Programmer("ibrahim", "github")
mohammed.show_details()
ibrahim.show_details()