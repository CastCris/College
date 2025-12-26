
class Class():
    class ClassPropertyDescriptor(object):
        def __init__(self, fget=None, fset=None)->None:
            self.fget = fget
            self.fset = fset

        def __get__(self, obj, objClass=None)->object:
            if objClass is None:
                objCLass = type(obj)

            return self.fget.__get__(obj, objClass)()

        def __set__(self, obj, value)->object:
            if not self.fset:
                raise AttributeError('Setter function not defined')

            objClass = type(obj)
            return self.fset.__get__(obj, objClass)(value)

        def setter(self, func)->object:
            if not isinstance(func, (classmethod, staticmethod)):
                func = classmethod(func)

            self.fset = func
            return self

    @classmethod
    def property(cls, func)->ClassPropertyDescriptor:
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)

        return cls.ClassPropertyDescriptor(func)
