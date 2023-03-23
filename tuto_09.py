import weakref
class Date:
    _cache = { }
    
    @staticmethod
    def __new__(cls, year, month, day):
        self = Date._cache.get((year,month,day))
        
        if not self:
            # self = object.__new__(cls)
            # self = super().__new__(cls)
            self = super(Date,cls).__new__(cls)
            self.year = year
            self.month = month
            self.day = day
            Date._cache[year,month,day] = weakref.ref(self)
        else:

            self=self()

        return self
    def __init__(self, year, month, day):
        pass
    def __del__(self):
        del Date._cache[self.year,self.month,self.day]

d = Date(2012, 12, 21)
# e = Date(2012, 12, 22)
f = Date(2012, 12, 21)

# del f
# del d
print(Date._cache)

# class wdict(dict):
#     __slots__ = ('__weakref__',)
# w = wdict()
# w_ref = weakref.ref(w)

# class A:
#     @classmethod
#     def __init_subclass__(cls):
#         print('A.init_subclass')
#         super().__init_subclass__()
# class B:

#     @classmethod
#     def __init_subclass__(cls):
#         print('B.init_subclass')
#         super().__init_subclass__()
# # Should see output from both classes here
# class C(A, B):
#     pass

from dataclasses import dataclass
# 7.29
from enum import Enum

class CONTROL:
    def __init_subclass__(cls,*args, **kwargs) -> None:
        cls.MOVE_LEFT="A"
        cls.MOVE_RIGHT="D"
        cls.MOVE_DOWN="S"
        cls.MOVE_UP="W"
        cls.RUN="J"
        cls.JUMP="K"


class Template_Brands_STR(str,Enum):
    DEFAULT=0
    XBOX=1
    PS=2
    PC=3

    @classmethod
    def _missing_(cls, value):
        return cls.DEFAULT

class Template_Brands_INT(int,Enum):
    DEFAULT=0
    XBOX=1
    PS=2
    PC=3
    
    

    @classmethod
    def _missing_(cls, value):
        return cls.DEFAULT
    

@dataclass
class Brand(CONTROL):
    
    console:Template_Brands_STR|Template_Brands_INT
    # def __post_init__(self):
    #  super().__init__(self.console)

    
user_a=Brand(Template_Brands_STR.XBOX)
user_b=Brand(Template_Brands_INT(2))
user_c=Brand(Template_Brands_INT(11))
print(user_a.console.name)
print(user_a.MOVE_LEFT)
print(user_b.console.name)
print(user_c.console.name)

