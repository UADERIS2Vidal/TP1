#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o de un rango de números              *
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

# Función para manejar el rango de números
def calcular_factoriales_en_rango(start, end):
    for i in range(start, end + 1):
        print(f"Factorial de {i} es {factorial(i)}")

# Verificamos si se pasó un argumento
if len(sys.argv) == 1:
    # Si no se pasó argumento, solicitamos al usuario
    rango = input("Debe informar un rango! Ingrese un rango (ej. -10 o 20-): ")
    if rango.startswith("-"):
        end = int(rango[1:])
        start = 1
        calcular_factoriales_en_rango(start, end)
    elif rango.endswith("-"):
        start = int(rango[:-1])
        end = 60
        calcular_factoriales_en_rango(start, end)
    else:
        start, end = map(int, rango.split('-'))
        calcular_factoriales_en_rango(start, end)
else:
    # Si se pasó argumento, usamos el argumento
    rango = sys.argv[1]
    if rango.startswith("-"):
        end = int(rango[1:])
        start = 1
        calcular_factoriales_en_rango(start, end)
    elif rango.endswith("-"):
        start = int(rango[:-1])
        end = 60
        calcular_factoriales_en_rango(start, end)
    else:
        start, end = map(int, rango.split('-'))
        calcular_factoriales_en_rango(start, end)
