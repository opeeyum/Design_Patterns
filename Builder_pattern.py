class Car:
    '''The Product'''
    def __init__(self):
        self.autonomous_driving = None
        self.sunroof = None
        self.fuel = None

    def __str__(self):
        return f'Autonomous driving: {self.autonomous_driving} | Sunroof: {self.sunroof} | Fuel: {self.fuel}'

class AbstractBuilder:
    '''Builder Interface'''
    def __init__(self):
        self.car = None
    def createNewCar(self):
        self.car = Car()

class ConcreteBuilder(AbstractBuilder):
    '''Concrete Builder'''
    def addAutonomous_driving(self, AD):
        self.car.autonomous_driving = AD
    def addSunroof(self, SR):
        self.car.sunroof = SR
    def addFuel(self, fuel):
        self.car.fuel = fuel

class Director:
    '''Director'''
    def __init__(self, builder):
        self._builder = builder
    def constructCar(self, AD=False, SR=False, fuel="Electric"):
        self._builder.createNewCar()
        self._builder.addAutonomous_driving(AD)
        self._builder.addSunroof(SR)
        self._builder.addFuel(fuel)
        return self._builder.car

#Instantiation of Builder
concreteBuilder = ConcreteBuilder()
#Calling Director
director = Director(concreteBuilder)
 
#Getting Our Product
ModelOne = director.constructCar()
print("Details of carOne:", ModelOne)

ModelTwo = director.constructCar(True, True, "Diesel")
print("Details of carOne:", ModelTwo)

ModelThree = director.constructCar(True, False, "Petrol")
print("Details of carOne:", ModelThree)


