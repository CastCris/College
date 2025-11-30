class Circle():
    def __init__(self, radius:float):
        self.radius = radius

    @property
    def area(self)->float:
        import math

        ##
        return math.pi * self.radius ** 2
    
    @property
    def perimeter(self)->float:
        import math

        ##
        return 2 * math.pi * self.radius

    def __repr__(self)->str:
        return f"""
        radius: {self.radius};
        area: {self.area};
        perimeter: {self.perimeter}
    """
##

import math

instance = Circle(1 / math.pi)
print(instance)
