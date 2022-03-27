from  class_Vehicles import Vehicles
class Car (Vehicles):
    def __init__(self, color, model, wheels, km , year):
        super().__init__(color,model, wheels, km )
        self.year = year
    def __str__(self):
        return super().__str__() +' ' + str(self.year)


car1 =Car("red","mazda",4,20000,2022)
print(car1)