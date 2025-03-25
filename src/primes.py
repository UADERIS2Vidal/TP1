#!/usr/bin/python3
# Programa en Python para mostrar todos los números primos dentro de un intervalo dado.

# Definir el límite inferior y superior del intervalo
lower = 1  # Límite inferior del rango (el primer número a verificar)
upper = 500  # Límite superior del rango (el último número a verificar)

# Imprimir el encabezado con el rango en el que se buscarán los números primos
print("Prime numbers between", lower, "and", upper, "are:")

# Recorrer todos los números entre el límite inferior y el superior, incluyendo el superior
for num in range(lower, upper + 1):
    # Los números primos son mayores que 1, por lo que solo se verifican los números mayores a 1
    if num > 1:
        # Verificar si el número 'num' es divisible por cualquier número entre 2 y 'num-1'
        for i in range(2, num):
            # Si 'num' es divisible por 'i', no es un número primo (se puede dividir sin residuo)
            if (num % i) == 0:
                break  # Si encontramos un divisor, salimos del ciclo 'for'
        else:
            # Si no se encuentra ningún divisor, 'num' es un número primo, lo mostramos
            print(num)  # Mostrar el número primo encontrado

