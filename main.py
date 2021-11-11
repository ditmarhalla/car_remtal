import datetime
from car_class import Car

class Rent:
    def __init__(self):
        self.car = []

    def __str__(self):
       ourtput =  '%f' % (self.car)
       return ourtput

    def add_new_car(self,plate,mark=None, model=None,year=None,space=None, km=None):
        self.car.append(Car(plate, mark, model, year, space, km))

    def rent_car()

r = Rent()
test = r.add_new_car("AA 123 AA","Skoda", "Octavia", 1994, 5, 90000)
print(r.car)