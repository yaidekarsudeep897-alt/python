class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=brand
    def display_info(self):
        print(f"Car brand:{self.brand},Model:{self.model}")
my_car=car("Toyota","Caralla")
my_car.display_info()