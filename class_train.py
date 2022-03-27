from class_Vehicles import Vehicles
class Train(Vehicles):
    def __init__(self,color, model, wheels, km,airPollution= None):
        super().__init__(color,model,wheels,km)
        self.airPollution = airPollution

    def __str__(self):
        return super().__str__() +'\nthe air pollution: '+ str(self.airPollution)

train1 = Train("black","israel",350,500000)
print(train1)
