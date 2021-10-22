class Car:
    def __init__(self,plate, mark=None, model=None,year=None,space=None, km=None): 
        self.plate = plate
        self.mark = mark
        self.model = model
        self.year = year
        self.space = space
        self.km = km

    def __str__(self):
       ourtput =  '%s, %s, %s, %s, %s, %s' % (self.plate, self.mark, self.model, self.year, self.space, self.km)
       return ourtput

    def find(self, filter):
        return  filter in self.plate or filter in self.model

    
'''
c1 = Car("AA 123 AA")
c2 = Car("BB 123 AA")
c3 = Car("CC 123 AA")
c4 = Car("DD 123 AA")
'''