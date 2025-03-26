#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Verificamos si se pasó un argumento
if len(sys.argv) == 1:
    # Si no se pasó argumento, solicitamos al usuario
    num = int(input("Debe informar un número! Ingrese un número: "))
else:
    # Si se pasó argumento, usamos el argumento
    num = int(sys.argv[1])

print("Factorial ", num, "! es ", factorial(num)) 

