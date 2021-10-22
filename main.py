import datetime
from car_class import Car

class Rent:
    def __init__(self):
        self.car = []

    def __str__(self):
       ourtput =  '%s, %s, %s, %s, %s, %s' % (self.car, self.mark, self.model, self.year, self.space, self.km)
       return ourtput

    def add_new_car(self,plate,type=None, model=None,year=None,space=None, km=None):
        self.car.append(Car(plate, type,  model, year, space, km))


r = Rent()
test = r.add_new_car("AA 123 AA")
print(test.car)