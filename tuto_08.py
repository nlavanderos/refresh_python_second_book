def d(m):
    
    print("entra")
    x=yield
   
    yield x*2

    yield "CLIENTE 0"
    yield "CLIENTE 2"
    print("sale")


me=d([1,2,3])
next(me)
fk=me.send(200)

print(fk)
print(list(me))

from dataclasses import dataclass

# from typing import Union

@dataclass
class Punto:
    x:int
    y:int
    def sum(self)->float|int:
        return self.x+self.y

rp=Punto(2,5)
print(rp.sum())
