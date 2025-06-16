#!/usr/bin/env python3
"""
Programa interactivo para operaciones básicas y avanzadas entre dos números.
Ejecute en terminal: python interactive_math_terminal.py
"""

def pedir_numero(nombre):
    while True:
        entrada = input(f"Ingrese el valor de '{nombre}': ")
        try:
            num = float(entrada)
            return num
        except ValueError:
            print(f"Entrada inválida para '{nombre}'. Por favor, ingrese un número válido.")

def pedir_texto():
    return input("Ingrese un texto: ")

def pedir_lista():
    entrada = input("Ingrese elementos de la lista separados por comas: ")
    lista = [x.strip() for x in entrada.split(',')]
    return lista

def pedir_diccionario():
    diccionario = {}
    while True:
        clave = input("Ingrese una clave (o 'salir' para terminar): ")
        if clave.lower() == 'salir':
            break
        valor = input(f"Ingrese el valor para '{clave}': ")
        diccionario[clave] = valor
    return diccionario

def main():
    print("=== Operaciones Básicas y Avanzadas Interactivas ===\n")

    a = pedir_numero('a')
    b = pedir_numero('b')

    print("\nCalculando resultados<=============>\n")

    # Operaciones básicas
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    division_entera = a // b if b != 0 else None
    modulo = a % b if b != 0 else None
    potencia = a ** b

    # Operaciones de comparación
    x = pedir_numero('x')
    y = pedir_numero('y')
    igual = x == y
    diferente = x != y
    mayor = x > y
    menor = x < y
    mayor_igual = x >= y
    menor_igual = x <= y

    # Operaciones lógicas
    and_logico = a > 0 and b > 0
    or_logico = a > 0 or b > 0
    not_logico = not (a > 0)

    # Funciones para strings
    texto = pedir_texto()
    mayusculas = texto.upper()
    minusculas = texto.lower()
    longitud = len(texto)
    reemplazo = texto.replace("Python", "Mundo")

    # Funciones para listas
    lista = pedir_lista()
    lista.append('4')  # Añade elemento '4' como cadena
    if '2' in lista:
        lista.remove('2')  # Remueve el string '2' si existe
    longitud_lista = len(lista)  # Tamaño de la lista
    lista.sort()  # Ordena alfabéticamente (funciona para strings)

    # Funciones para diccionarios
    diccionario = pedir_diccionario()
    claves = list(diccionario.keys())
    valores = list(diccionario.values())
    diccionario["ciudad"] = "Bogotá"
    if "edad" in diccionario:
        del diccionario["edad"]

    # Conversión de tipos
    numero = 10
    texto_numero = str(numero)
    lista_texto = list(texto)
    numero_flotante = float("3.14")

    # Imprimir resultados
    print("\n=== Resultados ===")
    print(f"Suma: {a} + {b} = {suma}")
    print(f"Resta: {a} - {b} = {resta}")
    print(f"Multiplicación: {a} × {b} = {multiplicacion}")
    if division is not None:
        print(f"División: {a} ÷ {b} = {division:.5f}")
    else:
        print("División: Indefinido (división por cero)")
    if division_entera is not None:
        print(f"División entera: {a} // {b} = {int(division_entera)}")
    else:
        print("División entera: Indefinido (división por cero)")    
    if modulo is not None:
        print(f"Módulo: {a} % {b} = {modulo}")
    else:
        print("Módulo: Indefinido (división por cero)")
    print(f"Potencia: {a} ** {b} = {potencia}")

    print("\n=== Operaciones de Comparación ===")
    print(f"¿x es igual a y? {igual}")
    print(f"¿x es diferente de y? {diferente}")
    print(f"¿x es mayor que y? {mayor}")
    print(f"¿x es menor que y? {menor}")
    print(f"¿x es mayor o igual a y? {mayor_igual}")
    print(f"¿x es menor o igual a y? {menor_igual}")

    print("\n=== Operaciones Lógicas ===")
    print(f"AND lógico: {and_logico}")
    print(f"OR lógico: {or_logico}")
    print(f"NOT lógico: {not_logico}")

    print("\n=== Funciones para Strings ===")
    print(f"Texto en mayúsculas: {mayusculas}")
    print(f"Texto en minúsculas: {minusculas}")
    print(f"Longitud del texto: {longitud}")
    print(f"Texto reemplazado: {reemplazo}")

    print("\n=== Funciones para Listas ===")
    print(f"Lista después de añadir '4': {lista}")
    print(f"Tamaño de la lista: {longitud_lista}")

    print("\n=== Funciones para Diccionarios ===")
    print(f"Claves del diccionario: {claves}")
    print(f"Valores del diccionario: {valores}")
    print(f"Diccionario después de añadir 'ciudad': {diccionario}") 

    print("\n=== Conversión de Tipos ===")
    print(f"Texto convertido a número: {texto_numero}")
    print(f"Texto convertido a lista: {lista_texto}")
    print(f"Número flotante: {numero_flotante}")

    print("\n¡Gracias por usar el programa!")

if __name__ == "__main__":
    main()
