from class_Vehicles import Vehicles
class airplane(Vehicles):
    def __init__(self,color,model,wheels,km,wings):
        super().__init__(color,model,wheels,km)
        self.wings = wings

    def __str__(self):
        return super().__str__()+' '+ '\nthe number of wings is :'+str(self.wings)

plane1 = airplane("black","f16",2,1000,2)
print(plane1)