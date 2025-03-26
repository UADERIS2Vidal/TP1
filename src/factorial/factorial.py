#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o de un rango de números              *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función para calcular el factorial de un número
def factorial(num): 
    # Si el número es negativo, no existe el factorial
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    # Si el número es 0, el factorial es 1
    elif num == 0: 
        return 1
    else: 
        fact = 1
        # Calculamos el factorial de forma iterativa
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Función para calcular los factoriales de un rango de números
def calcular_factoriales_en_rango(start, end):
    # Recorremos el rango y calculamos el factorial de cada número
    for i in range(start, end + 1):
        print(f"Factorial de {i} es {factorial(i)}")

# Verificamos si se pasó un argumento por línea de comandos
if len(sys.argv) == 1:
    # Si no se pasó argumento, solicitamos al usuario el rango
    rango = input("Debe informar un rango! Ingrese un rango (ej. -10 o 20-): ")
    
    # Si el rango empieza con "-", calculamos desde 1 hasta el número indicado
    if rango.startswith("-"):
        end = int(rango[1:])  # Eliminar el "-" y convertir a entero
        start = 1  # El inicio siempre es 1
        calcular_factoriales_en_rango(start, end)
    
    # Si el rango termina con "-", calculamos desde el número indicado hasta 60
    elif rango.endswith("-"):
        start = int(rango[:-1])  # Eliminar el "-" y convertir a entero
        end = 60  # El final siempre es 60
        calcular_factoriales_en_rango(start, end)
    
    # Si el rango tiene el formato "inicio-fin", calculamos los factoriales entre esos dos valores
    else:
        start, end = map(int, rango.split('-'))  # Convertimos las partes en enteros
        calcular_factoriales_en_rango(start, end)
else:
    # Si se pasó un argumento, usamos ese argumento como el rango
    rango = sys.argv[1]
    
    # Si el rango empieza con "-", calculamos desde 1 hasta el número indicado
    if rango.startswith("-"):
        end = int(rango[1:])  # Eliminar el "-" y convertir a entero
        start = 1  # El inicio siempre es 1
        calcular_factoriales_en_rango(start, end)
    
    # Si el rango termina con "-", calculamos desde el número indicado hasta 60
    elif rango.endswith("-"):
        start = int(rango[:-1])  # Eliminar el "-" y convertir a entero
        end = 60  # El final siempre es 60
        calcular_factoriales_en_rango(start, end)
    
    # Si el rango tiene el formato "inicio-fin", calculamos los factoriales entre esos dos valores
    else:
        start, end = map(int, rango.split('-'))  # Convertimos las partes en enteros
        calcular_factoriales_en_rango(start, end)
