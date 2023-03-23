#!/usr/bin/env python3

from importacionMasiva import STK
from collections import defaultdict

stk_ex=STK()
stk_ex.push(12)
stk_ex.push(44)
print(stk_ex)


dct_real={'0':"prueba",'1':"dummty" }
lst_pr=defaultdict(lambda: "Not Present", dct_real)
# lst_pr.setdefault(3,"aaaaa")
print(lst_pr["3"])
print([1,2,3].pop(1))


# index
print([1,2,3].index(2))
# join
print('-'.join(['fgrrr','asasasas']))
# partition
# strip equal to trimmed
print('   sadsa'.strip())
# *args **kwargs

#args as tuple
#kwargs as dict
def pk(*args:tuple,**kwargs:dict)->tuple:
    print(args[0])
    print(kwargs['kt'])
    return args

a,*b=pk('aa','vv','rr',kt=1.23,r=2)
print(a,b)
# casefold
print('ABcD'.casefold()=='abcd')

# isalpha
print('AAAaaa11'.isalnum())

# sort with key for sorting with one value of list,tuple,etc...
lst2 = [('candy','30','100'), ('apple','10','400'), ('baby','20','300')]
lst2.sort(key=lambda x:x[2])
lst2.reverse()
print(lst2)

dct_real['2']='stra'
print(dct_real)

parts = 'url=http://www.python.org'.split('=')
print(parts)

from functools import partial
cd=partial(pk,'aAzzzzzzz')
cd(kt=1.235)
words=['caxzxz','baaa']
result = sorted(words, key=lambda x: len(set(x)))
print(result)

from concurrent.futures import ThreadPoolExecutor
pool = ThreadPoolExecutor(16)
r = pool.submit(sum,[2,3]) 
# Returns a Future
print(r.result())

#DECORATORS
from functools import wraps

def tr(fun):
    #HIDEN METADATA SUCH NAME DOC STRING,TYPE HINTS ,ETC..
    @wraps(fun)
    def llam(*args, **kwargs):
        print('llamada a ', fun.__name__)
        return fun(*args,**kwargs)
    return llam

class SomeClass(object):
    @classmethod
    @tr
    def matem(cls,a,b):
        return a + b
person1 = SomeClass.matem(7,2)
print(person1)


print(list(filter(lambda x: x > 2, [1,2,3])))

import inspect

sig = inspect.signature(pk)
print(sig)
print(list(sig.parameters))

from collections import ChainMap
def debug(*varnames):
    f = inspect.currentframe().f_back
    vars = ChainMap(f.f_locals, f.f_globals)
    print(f'{f.f_code.co_filename}:{f.f_lineno}')
    for name in varnames:
        print(f' {name} = {vars[name]!r}')
def func(x, y):
    z = x + y
    debug('x','y') # Shows x and y along with file/line
    return z
print(func(1,2))


#PARTIAL AND LAMBDA
#LAMBDA RETURN THE LAST VALUE USED
#PARTIAL CACHE THE VALUES

#EXEC AND EVAL
#EVAL CAN ONLY HANDLE ONE SENTENCE AND EXEC A WHOLE CODE

