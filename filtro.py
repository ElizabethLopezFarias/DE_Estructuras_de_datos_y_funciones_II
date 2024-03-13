# filtro.py
"""
Se solicita implementar una función que permita entregar lo siguiente:
● Un diccionario con los productos que cumplen una cierta condición dado un umbral
● La función debe permitir mostrar los valores mayor que o menor que un umbral (siempre estrictos).
● Por defecto la función debe siempre mostrar los valores mayor que el umbral a menos que se indique lo contrario.
Se espera ejecutar el programa de la siguiente manera:
● Si se especifica un argumento, este debe ser el umbral y por defecto debe calcular los que son estrictamente mayores al umbral.
python filtro.py 30000

"""
# Función que  permite realizar el filtrado de los productos dependiendo si son mayores o menores al umbral ingresado
def filtrar_productos(precios, umbral, operacion="mayor"):
    productos_filtrados = {}   # Diccionario para almacenar los productos filtrados
    for producto, precio in precios.items(): #Ciclo que recorre el diccionario para hacer el comparativo
        if operacion == "mayor" and precio > umbral:
            productos_filtrados[producto] = precio
        elif operacion == "menor" and precio < umbral:
            productos_filtrados[producto] = precio

    return productos_filtrados

import sys

# Diccionario de prueba
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}
    #Verifica los argumentos ingresados en el terminal
if len(sys.argv) == 2:
    umbral = int(sys.argv[1])
    productos_filtrados = filtrar_productos(precios, umbral)
    #join() para concatenar los nombres de los productos separados por comas (,) y mostrarlos como una cadena de texto. 
    print(f"Los productos mayores al umbral son: {', '.join(productos_filtrados.keys())}")
elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    operacion = sys.argv[2]
    if operacion in ["mayor", "menor"]:
        productos_filtrados = filtrar_productos(precios, umbral, operacion)
        print(f"Los productos {operacion}es al umbral son: {', '.join(productos_filtrados.keys())}")
    else:
        print("Lo sentimos, no es una operación válida.")
else:
    print("Ingresar parametros correctos, por ejemplo: python filtro.py <umbral> [mayor|menor]")