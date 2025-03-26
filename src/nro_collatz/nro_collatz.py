import matplotlib.pyplot as plt

# Función para calcular el número de iteraciones que tarda un número en llegar a 1
def collatz_iterations(n):
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

# Crear listas para almacenar los valores
start_numbers = []
iterations_list = []

# Calcular las iteraciones para los números entre 1 y 10000
for n in range(1, 10001):
    iterations = collatz_iterations(n)
    start_numbers.append(n)
    iterations_list.append(iterations)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(start_numbers, iterations_list, color='blue', s=1)
plt.title('Número de Iteraciones de la Conjetura de Collatz')
plt.xlabel('Número de inicio (n)')
plt.ylabel('Número de iteraciones para converger a 1')
plt.grid(True)
plt.show()
