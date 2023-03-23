from abc import ABC,abstractmethod

class DK(ABC):

    @abstractmethod
    def recieve(self):
        pass


class SmeClass(DK):
    def __init__(self,type,color):
        self.type=type
        self.color=color
        self._brand=None

    @property
    def brand(self):
        print("getter brand method called")
        return self._brand

    @brand.setter
    def brand(self,val):
        print("setter brand method called")
        self._brand=val

    @brand.deleter
    def brand(self):
        print("del brand method called")
        self._brand=None

    def recieve(self):
        ...

sm=SmeClass('GAS','RED')
sm.brand='Ford'
del sm.brand
print(sm.brand)



from enum import Enum
class TYPE_FOOD(Enum):
    pizza=1
    hamburgesa=2
    churrasco=3
print(TYPE_FOOD(2).name)



#MIXIN 
class Duck:
    @staticmethod
    def noise():
        return 'QUACK'

class Loud:
    def noise(self):
        print("Loading")
        return super().noise()

class L(Loud,Duck):
    pass

tst_class=L()
print(tst_class.noise())

#MRO METHOD RESOLUTION ORDER
print(L.__mro__)

#7.20 PAGE 193
handlers = {
Loud: print,
}

func = handlers.get(type(Loud()))
print(func)
func("Encontro algo")