import time

def schedule_classes(classes, conflicts):
    # Construir grafo de conflictos
    graph = {c: set() for c in classes}
    for c1, c2 in conflicts:
        graph[c1].add(c2)
        graph[c2].add(c1)
    
    # Ordenar clases por grado de conflicto descendente
    sorted_classes = sorted(classes, key=lambda x: len(graph[x]), reverse=True)
    
    # Asignar colores (combinaciones aula-horario)
    color_assignment = {}
    available_colors = [(r, t) for r in aulas for t in horarios]  # Ejemplo: aulas y horarios predefinidos
    
    for c in sorted_classes:
        used_colors = {color_assignment[vecino] for vecino in graph[c] if vecino in color_assignment}
        for color in available_colors:
            if color not in used_colors:
                color_assignment[c] = color
                break
        if c not in color_assignment:
            return None  # No hay solución
    
    return color_assignment

# Ejemplo de uso
classes = ["C1", "C2", "C3", "C4"]
conflicts = [("C1", "C2"), ("C1", "C3"), ("C2", "C4")]
aulas = ["A1", "A2"]
horarios = ["T1", "T2"]

# Medir el tiempo de inicio
start_time = time.time()

schedule = schedule_classes(classes, conflicts)

# Medir el tiempo de fin
end_time = time.time()

# Calcular el tiempo de ejecución
execution_time = end_time - start_time

if schedule:
    for clase, (aula, hora) in schedule.items():
        print(f"{clase} -> Aula: {aula}, Hora: {hora}")
else:
    print("No se encontró solución.")

# Imprimir el tiempo de ejecución
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
