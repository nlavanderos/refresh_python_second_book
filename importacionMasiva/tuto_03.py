try:
    raise RuntimeWarning('U CAN NOT execute this')
except RuntimeWarning as err:
    print(err)
finally:
    print('SUCCESS')
#exception
class PROMPT_EXCEP(Exception):
    def __init__(self, nerr, msg) -> None:
        self.nerr=nerr
        self.msg=msg
try:
    raise PROMPT_EXCEP(204,'ERROR WITH PARAMS')
except PROMPT_EXCEP as e:
    print(e.msg)
# traceback lib show more exceptions logs

class STK:
    def __init__(self) -> None:
        self._items=[]
    
    def push(self,item) -> None:
        self._items.append(item)

    def pop(self) -> None:
        self._items.pop()
    #x means hexadecimal    
    def __repr__(self) -> str:
        return f'<{type(self).__name__} AT 0x{id(self):x} , SIZE {len(self)}>'
    
    def __len__(self):
        return len(self._items)

stk_ex=STK()
stk_ex.push(12)
print(stk_ex)

#to handle all connections,threads locks,open file without with,etc...
#import atexit
#atexit.register( u need create a function who closses the things.)

#with csv can read csv files but need open the file before

#CREATE VIRTUAL ENV
#python3 -m venv nameoftheenv

def main():
    from sys import argv
    if len(argv)==1:
        prompt=input('introduce un nombre: ')
    elif len(argv)==2:
        prompt=argv[1]
    else:
        raise SystemExit(f'USAGE: {argv[0]} [arg1 arg2 arg3 ]')
    print(prompt)

if __name__ == '__main__':
    print("s")
    # main()
    


#FOR MATRIX MULTIPLICATION CAN USE @ OPERATOR

#FOR MANAGEMENT FRACTIONS AND DECIMAL CAN U USE THE FOLLOWING LIBS.
# from fractions import Fraction
# from decimal import Decimal

#unpacking with *
# lst=[1,2,3,4,5]
# vr,*ss,xz=lst
# print(xz)


#list usefull built in functions
# any
# all
# sorted
# sum
# print(sum(lst))

#GENERATOR EXPRESSIONS
# xlg=(x*x for x in range(1,5))
#u can iterate with next(xlg) or in for loop


