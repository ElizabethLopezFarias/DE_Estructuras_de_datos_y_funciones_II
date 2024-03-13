# velocidad.py
"""
Código en python que debe medir mediante telemetría las velocidades de cada una de sus correas transportadoras. 
Para ello se pide determinar una funcionalidad que calcule el promedio de una lista de velocidades. 
"""
#Función que calcula el promedio de las velocidades en la lista y los asocia a su posición en la lista
def encontrar_correas_sobre_promedio(velocidades):
    total_velocidades = sum(velocidades)
    cantidad_correas = len(velocidades)
    promedio = total_velocidades / cantidad_correas

    correas_sobre_promedio_indices = []
    for indice, valor in enumerate(velocidades): #ciclo que recorre los datos de las correas
        if valor > promedio:
            correas_sobre_promedio_indices.append(indice)

    return correas_sobre_promedio_indices

# Ejemplo de uso:
velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
correas_sobre_promedio = encontrar_correas_sobre_promedio(velocidad)
print("Las correas sobre el promedio están en las posiciones:", correas_sobre_promedio)
