import asyncio


async def saludo(mr,num_atencion):
    return f'{mr} is waiting {num_atencion}'

async def executor():
    lst_orders=['Zeus','KK','MEM']
    lf= [await saludo(val,idx) for idx,val in enumerate(lst_orders,1)]
    list(map(lambda x:print(x),lf))
    return lf

print(asyncio.run(executor()))


#6.Generators
# def cnt(n):
#     print("counting ",n)
#     while n>0:
#         yield n
#         n-=1

# for x in cnt(2):
#     print('t ',x)


import pathlib
#directory management
import re
#regex
import sys

#append absolute path
# current_work_directory=pathlib.Path.cwd()
# sys.path.append(current_work_directory)
# print(sys.path[-1])
import os
for path in pathlib.Path('.').rglob('*.py'):
    if path.exists():
        print(path)

#POO
# INHERANCE
#CLASS METHOD
#STATIC METHOD
# 7.14
import random

class Card:
    def __init__(self,id):
        self.__id = id
        

    def sacar_dinero(self,ammount):
        self.balance-=ammount
        return self.balance
    
    @staticmethod
    def time():
        import datetime
        return datetime.datetime.now()

class Account(Card):
    '''account create'''
    def __init__(self,name:str,balance:int,id:str):
        self.name = name
        self.balance = balance
        super().__init__(f'{id:x}')

    @classmethod
    def cns(cls,acceso):
        return cls('Admin',0,acceso)
Account()
id_aleatorio=random.randint(1000000000,9999999999)
acc_01=Account('Nico',12000,id_aleatorio)
print(acc_01.__id)
print(acc_01.sacar_dinero(1000))
print(acc_01.time())
print(Card.time())
print(Account.cns(125412541254).balance)

#LECTOR DE XML
from xml.etree.ElementTree import XML
data=XML('''<account>
<name>NICO</name>
</account>''')
print(data.findtext('name'))

# / means c can be positional or keyword
# * means d and e must be keyword arguments
def test_sme(a:int,b:int,/,c:int,*,d:float,e:float)->float:
    return f'{(((a+b)*c)/(d*e)):0.2f}'

print(test_sme(44,12,13,d=1.1,e=2.1))

