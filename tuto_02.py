#!/usr/bin/env python3

from collections import OrderedDict
import datetime
from collections import Counter
from math import ceil, floor

fruits = Counter({'apples': 0, 'pears': 4, 'oranges': -89})

# SHOW POSITIVE VALUES
print(+fruits)
print(-fruits)


print("__________________")
print("MATEMATICA")
# UP THE VALUE TO NEXT INTEGER
print(ceil(5.1))
# STRIP THE DECIMAL OF THE NUMBER
print(floor(5.4))
# THE NUMBER RAISED TO NEXT INTEGER VALUE IF EQUAL> TO 5
print(round(5.5))


xd = (f'({5//2}, {5%2})')
# SIMULATE STRING TO DATA TYPE
print((eval(xd)) == tuple([5//2, 5 % 2]))

# SAME RESULT
# ROUND VALUE AND THEIR MODULE
print(divmod(5, 2) == tuple([5//2, 5 % 2]))
# ELEVATE NUMBER TO A EXPONENT
print(pow(2, 2) == 2**2)

print("__________________")
print("BINARIOS")
print(int("110", 2))
# agrega un 0 al principio
print(0b110 << 1)
print(50 << 1)
# elimina el primer digito
print(0b110 >> 1)
print(50 >> 1)

# ONE LINER CONDITIONAL STATEMENT
mv = 10 if 55 > 5 else 1
print(mv)

x = 0
while x < 2:

    x += 1
    if x == 1:
        # CONTINUE JUMP TO WHILE AND IGNORE NEXT INSTRUCTIONS.
        continue
    print(x)

# FORMATS

print("{:0.2f}".format(2002.849))
t = 'prueba'
print(t.rjust(len(t)+5, '$').ljust(len(t)+10, '$'))
print(f'{t:*>14}')
print('%d' % 2022)
fecha_actual = datetime.datetime.now()
print(f'{fecha_actual:%Y-%m-%d %H:%M}')

# repr special characters are printed
print(repr("hola\nmundo!"))


# FILES
# w+ data truncated read and write
# r+ i/o if not created read and write
# a+ read and write if not exist create the file
with open('tuto_02.txt', 'r+') as f:
    f.write('dfsad\n')
    for x in f.readlines():
        print(x)

# LISTAS
listas = [12, 10]
listas.insert(1, 11)
listas.remove(10)
print(listas)

# TUPLAS
# ITEMS OF TUPLE IN LIST AND UNPACKED IN VARS
ls = [('AA', 2000, 30)]
brand, price, quanty = ls[0]
print(brand, price, quanty)

# SETS 1.10 PAGE 17

names_set = set(['flask', 'django', 'flask', 'fastapi'])
names_norm = {'fastapi', 'elixir', 'fastapi', 'django', 'flask'}

print(names_set)
print(names_norm)

# UNION
print(names_set | names_norm)
# INTERSECTION
print(names_set & names_norm)
# DIFF and the diff simetric can be with ^
print(names_norm - names_set)

# DICTIONARIES
prices = {'HO': 'SOMEVAL'}
prices[('IBM', 'JUJ')] = 20.1
print(prices[('IBM', 'JUJ')])
print(prices.get('HO', 'OTHERVAL'))
del prices['HO']
print(prices)
dic_nr = {
    ('abc', 12, 200),
    ('dfg', 121, 2200),
    ('hij', 132, 2100)
}

# total_sh=Counter()
total_sh = {s[0]: 0 for s in dic_nr}
for name, qty, _ in dic_nr:
    total_sh[name] += qty
print(total_sh)

# INMUTABLE
# SET,TUPLE,STR

# MUTABLE
# INT,FLOAT,LIST,DICT

cd = [v if v % 4 == 0 else 0 for v in range(0, 21, 2)]
print(cd)

print(total_sh.items())
print(total_sh.keys())
print(total_sh.values())
for x in total_sh.keys():
    print(x)

# SAME AS WITH FOR LOOP
# xd=iter(total_sh.keys())
# print(xd.__next__())
# print(xd.__next__())
# print(xd.__next__())
