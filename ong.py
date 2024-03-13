# ong.py

def calcular(**kwargs):
    for nombre, valor in kwargs.items():
        if nombre.startswith("fact_"):
            numero = int(valor)
            resultado = factorial(numero)
            print(f"El factorial de {numero} es {resultado}")
        elif nombre.startswith("prod_"):
            lista = valor
            resultado = productoria(lista)
            print(f"La productoria de {lista} es {resultado}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def productoria(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

# Ejemplo de uso:
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
