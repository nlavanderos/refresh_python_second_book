#!/usr/bin/env python3
try:
    print("Este programa transforma un numero BIN,HEX,OCT A ENTERO")
    numero_consola=str(input("Introduce un numero: ")).lower()
    while True:
        print("________________")
        print("ELIGE UNA BASE")
        print("2.BINARIA")
        print("8.OCTAL")
        print("16.HEXA")
        print("________________")
        print("4.SALIR")
        print("*******************")
        basex=int(input("Base numero: "))
        if basex in [2,8,16]:
            sld=int(numero_consola,base=basex)
            print(f"El valor {numero_consola} ha sido transformado a base {basex} con valor {sld}")
        elif basex==4:
            print("Ha salido del programa")
            break
        else:
            print("Base fuera de los parametros")
        

except:
    print("NO PUDO SER TRANSFORMADO DEBIDO A QUE EL NUMERO NO CORRESPONDE A ESA BASE")