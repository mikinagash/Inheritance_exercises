class Vehicles():
    def __init__(self,color,model,wheels,km):
        self.color = color
        self.model = model
        self.wheels = wheels
        self.km = km
    def __str__(self):
        return 'The color is: '+ self.color +' '+ '\nthe model is :'+self.model +' '+'\nthe number of wheels is :' +str(self.wheels) +' '+ '\nthe km is :'+str(self.km)