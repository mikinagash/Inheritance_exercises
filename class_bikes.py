from class_Vehicles import Vehicles
class bikes(Vehicles):
    def __init__(self,color, model, wheels, km,size):
        super().__init__(color,model,wheels,km)
        self.size = size

    def __str__(self):
        return super().__str__() +' '+ str(self.size)

bike1 = bikes("red","bmx",2,50,36)
print(bike1)