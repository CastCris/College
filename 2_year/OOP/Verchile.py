
class Verchile():
    def __init__(self, brand:str, model:str)->None:
        self.brand = brand
        self.model = model

        self.DISPLAY_ATTR = [ "brand", "model" ]

    @property
    def details(self)->str:
        details = ['\n']

        for i in self.DISPLAY_ATTR:
            attr_value = self.__dict__.get(i, '')
            details.append(i + ': ' + str(attr_value))

        details.append('\n')

        return '\n'.join(details)

class Car(Verchile):
    def __init__(self, brand:str, model:str, ports:int)->None:
        super().__init__(brand, model)

        self.ports = ports
        self.DISPLAY_ATTR.append("ports")

class MotorCycle(Verchile):
    def __init__(self, brand:str, model:str, cylinder_power:int)->None:
        super().__init__(brand, model)

        self.cylinder_power = cylinder_power
        self.DISPLAY_ATTR.append("cylinder_power")

##
car_instance = Car(
    brand="Fiat",
    model="Uno",
    ports=4
)

motor_instance = MotorCycle(
    brand="Hyundai",
    model="AAAAA",
    cylinder_power=100
)

print('Car details: ', car_instance.details)

print('===============')

print('MotorCycle details: ', motor_instance.details)
