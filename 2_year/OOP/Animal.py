
class Animal():
    def __init__(self, name:str)->None:
        self.name = name

    def emit_sound(self)->str:
        return "( Generic sound )"

class Dog(Animal):
    def emit_sound(self)->str:
        return "Woof!"

    def woof(self)->str:
        return "Woof woof!"

class Cat(Animal):
    def emit_sound(self)->str:
        return "Meow!"

    def meow(self)->str:
        return "Meow Meow!"

##
dog_instance = Dog(name="Princesinha")
cat_instance = Cat(name="Bangula")

print('Dog emit sound: ', dog_instance.emit_sound())
print('Dog woof: ', dog_instance.woof())

print('Cat emit sound: ', cat_instance.emit_sound())
print('Cat meow: ', cat_instance.meow())
