class Car():
    '''The Product'''
    def __init__(self):
        self.autonomous_driving = False
        self.sunroof = False
        self.fuel = None

    def addAutonomous_driving(self):
        self.autonomous_driving = True
    def addSunroof(self):
        self.sunroof = True
    def addFuel(self, fuel="Electric"):
        self.fuel = fuel

    def __str__(self):
        return f'Autonomous driving: {self.autonomous_driving} | Sunroof: {self.sunroof} | Fuel: {self.fuel}'

#First instance name ModelOne
ModelOne = Car()
ModelOne.addAutonomous_driving()
ModelOne.addSunroof()
ModelOne.addFuel("Petrol")
print("Details of carOne:", ModelOne)
 
#Second instance named ModelTwo
ModelTwo = Car()
ModelTwo.addAutonomous_driving()
ModelTwo.addFuel()
print("Details of carOne:", ModelTwo)
 

#Third instance named ModelThree
ModelThree = Car()
ModelThree.addAutonomous_driving()
ModelThree.addSunroof()
ModelThree.addFuel("Diesel")
print("Details of carOne:", ModelThree)
 