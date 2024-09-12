from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    pass

car1 = Car(12,4)

car1.go()
