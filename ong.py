"""
Crear un script llamado ong.py que contenga las siguientes funciones:
○ Una función que calcule el factorial.
○ Una función que calcule la productoria.
○ Una función que permita controlar los cálculos. Esta función se debe invocar de la siguiente manera:
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

"""

#Recibe argumentos con nombres que indican si se calcula un factorial o una productoria.
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
# Calcula el factorial de un número no negativo.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#Calcula la productoria de los elementos en una lista.
def productoria(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

# Ejemplo de uso:
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
