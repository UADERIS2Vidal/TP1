#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                         *
#* Calcula el factorial de un número o de un rango de números con OOP       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Clase que contiene la lógica de cálculo de factoriales
class Factorial:
    def __init__(self):
        # Inicializamos el objeto sin necesidad de parámetros para la construcción
        pass

    # Método para calcular el factorial de un número
    def factorial(self, num): 
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

    # Método para calcular los factoriales entre un rango dado (min y max)
    def run(self, min, max):
        if min > max:
            print("El valor mínimo no puede ser mayor que el valor máximo.")
            return
        for i in range(min, max + 1):
            print(f"Factorial de {i} es {self.factorial(i)}")

# Verificamos si se pasó un argumento
if len(sys.argv) == 1:
    # Si no se pasó argumento, solicitamos al usuario el rango
    rango = input("Debe informar un rango! Ingrese un rango (ej. -10 o 20-): ")
    
    # Si el rango empieza con "-", calculamos desde 1 hasta el número indicado
    if rango.startswith("-"):
        end = int(rango[1:])  # Eliminar el "-" y convertir a entero
        start = 1  # El inicio siempre es 1
        factorial_obj = Factorial()
        factorial_obj.run(start, end)
    
    # Si el rango termina con "-", calculamos desde el número indicado hasta 60
    elif rango.endswith("-"):
        start = int(rango[:-1])  # Eliminar el "-" y convertir a entero
        end = 60  # El final siempre es 60
        factorial_obj = Factorial()
        factorial_obj.run(start, end)
    
    # Si el rango tiene el formato "inicio-fin", calculamos los factoriales entre esos dos valores
    else:
        start, end = map(int, rango.split('-'))  # Convertimos las partes en enteros
        factorial_obj = Factorial()
        factorial_obj.run(start, end)

else:
    # Si se pasó argumento, usamos ese argumento como el rango
    rango = sys.argv[1]
    factorial_obj = Factorial()
    
    # Si el rango empieza con "-", calculamos desde 1 hasta el número indicado
    if rango.startswith("-"):
        end = int(rango[1:])  # Eliminar el "-" y convertir a entero
        start = 1  # El inicio siempre es 1
        factorial_obj.run(start, end)
    
    # Si el rango termina con "-", calculamos desde el número indicado hasta 60
    elif rango.endswith("-"):
        start = int(rango[:-1])  # Eliminar el "-" y convertir a entero
        end = 60  # El final siempre es 60
        factorial_obj.run(start, end)
    
    # Si el rango tiene el formato "inicio-fin", calculamos los factoriales entre esos dos valores
    else:
        start, end = map(int, rango.split('-'))  # Convertimos las partes en enteros
        factorial_obj.run(start, end)
