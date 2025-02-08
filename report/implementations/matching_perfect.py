import numpy as np
from scipy.optimize import linear_sum_assignment
import time

# Matriz de costos (filas: profesores, columnas: clases)
# cost[i][j] = costo de asignar la clase j al profesor i
cost = np.array([
    [3, 1, 2],
    [2, 4, 3],
    [3, 2, 1]
])

# Medir el tiempo de inicio
start_time = time.time()

# Aplicar el Algoritmo Húngaro
row_ind, col_ind = linear_sum_assignment(cost)

# Medir el tiempo de fin
end_time = time.time()

# Calcular el tiempo de ejecución
execution_time = end_time - start_time

# Asignaciones óptimas
for teacher, class_idx in zip(row_ind, col_ind):
    print(f"Profesor {teacher} -> Clase {class_idx} (Costo: {cost[teacher][class_idx]})")

# Costo total
print("Costo total:", cost[row_ind, col_ind].sum())

# Imprimir el tiempo de ejecución
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
