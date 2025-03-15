# Definir la matriz 3D: ciudades, días de la semana y semanas
# Estructura: matriz_3d[ciudad][día][semana]
matriz_3d = [
    # Ciudad 1
    [
        [25, 26, 27, 28, 29, 30, 31],  # Lunes (Semana 1, 2, 3, 4, 5, 6, 7)
        [24, 25, 26, 27, 28, 29, 30],  # Martes
        [23, 24, 25, 26, 27, 28, 29],  # Miércoles
        [22, 23, 24, 25, 26, 27, 28],  # Jueves
        [21, 22, 23, 24, 25, 26, 27],  # Viernes
        [20, 21, 22, 23, 24, 25, 26],  # Sábado
        [19, 20, 21, 22, 23, 24, 25]   # Domingo
    ],
    # Ciudad 2
    [
        [30, 31, 32, 33, 34, 35, 36],  # Lunes
        [29, 30, 31, 32, 33, 34, 35],  # Martes
        [28, 29, 30, 31, 32, 33, 34],  # Miércoles
        [27, 28, 29, 30, 31, 32, 33],  # Jueves
        [26, 27, 28, 29, 30, 31, 32],  # Viernes
        [25, 26, 27, 28, 29, 30, 31],  # Sábado
        [24, 25, 26, 27, 28, 29, 30]   # Domingo
    ]
]

# Nombres de las ciudades y días de la semana
ciudades = ["Ciudad 1", "Ciudad 2"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = len(matriz_3d[0][0])  # Número de semanas
def calcular_promedio_temperaturas(matriz_3d, ciudades):
        num_semanas = len(matriz_3d[0][0])  # Número de semanas
# Calcular el promedio de temperaturas por ciudad y semana
for ciudad_idx in range(len(matriz_3d)):  # Recorrer ciudades
    for semana in range(num_semanas):  # Recorrer semanas
        suma_temperaturas = 0
        contador_dias = 0
        for dia in range(len(dias_semana)):  # Recorrer días de la semana
            suma_temperaturas += matriz_3d[ciudad_idx][dia][semana]
            contador_dias += 1
        promedio = suma_temperaturas / contador_dias
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana + 1}: {promedio:.2f}°C")