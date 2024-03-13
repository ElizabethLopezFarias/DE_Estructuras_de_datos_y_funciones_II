# filtro.py

def filtrar_productos(precios, umbral, operacion="mayor"):
    productos_filtrados = {}

    for producto, precio in precios.items():
        if operacion == "mayor" and precio > umbral:
            productos_filtrados[producto] = precio
        elif operacion == "menor" and precio < umbral:
            productos_filtrados[producto] = precio

    return productos_filtrados

if __name__ == "__main__":
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

    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        productos_filtrados = filtrar_productos(precios, umbral)
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