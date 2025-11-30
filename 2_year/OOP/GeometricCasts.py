from abc import ABC, abstractmethod

##
class GeometricCast(ABC):
    @property
    @abstractmethod
    def area(self)->float|int:
        pass

    @property
    @abstractmethod
    def perimeter(self)->float|int:
        pass

class Rectangle(GeometricCast):
    def __init__(self, width:float|int, height:float|int)->None:
        self.width = width
        self.height = height

    @property
    def area(self)->float|int:
        return self.width * self.height

    @property
    def perimeter(self)->float|int:
        return self.width * 2 + self.height * 2
    
    def __repr__(self)->str:
        return f"""
        width: {self.width};
        height: {self.height};

        area: {self.area};
        perimeter: {self.perimeter}.
        """

class Triangle(GeometricCast):
    def __init__(self, a:int|float, b:int|float, c:int|float)->None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self)->float:
        s = (self.a + self.b + self.c) / 2
        A = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** (1/2)
        return A

    @property
    def perimeter(self)->float|int:
        return self.a + self.b + self.c

    def __repr__(self)->str:
        return f"""
        sides(a,b,c): {self.a}, {self.b}, {self.c};

        area: {self.area};
        perimeter: {self.perimeter}.
        """

##
rectangle_instance = Rectangle(
    width = 10,
    height = 20
)

triangle_instance = Triangle(
    a = 3,
    b = 4,
    c = 5
)

print('---Rectangle---')
print(rectangle_instance)

print('---Triangle---')
print(triangle_instance)
