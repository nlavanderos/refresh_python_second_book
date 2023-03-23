#!/usr/bin/env python3
from itertools import chain
from copy import deepcopy
from functools import reduce

#enumerate
for index,val in enumerate([22,5,31],start=1):
    print(F'POSITION {index} WITH VALUE {val}')

# zip
lst_var1=[1,2,3,4]
lst_var2=[5,6,8,9]
lst_fin=zip(lst_var1,lst_var2)

vr=list(chain(*lst_fin))
print(vr)

#enter and exit to handle with statement.
class NJ:
    def __init__(self,x) -> None:
        self.x=x
    
    def __enter__(self):
        return self
    
    def __exit__ (self,type,value,tb):
        self.x=0

vr_temp=NJ(42)
with vr_temp as nume:
    print(nume.x)
print(vr_temp.x)


#lambda
#copy an element
cp_lst_var1=deepcopy(lst_var1)
print(list(map(lambda x:x+x,cp_lst_var1)))
print(reduce(lambda x,y:x+y,cp_lst_var1))
