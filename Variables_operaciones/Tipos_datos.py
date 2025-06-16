# Declaración de variables de diferentes tipos
entero = 10  # Tipo int
decimal = 3.14  # Tipo float
texto = "Hola, Python"  # Tipo str
booleano = True  # Tipo bool
lista = [1, 2, 3, 4, 5]  # Tipo list

# Verificación e impresión del tipo de dato y valor
print(f"Valor: {entero},                 Tipo: {type(entero)},      Clase: {type(entero).__name__}")
print(f"Valor: {decimal},               Tipo: {type(decimal)},    Clase: {type(decimal).__name__}")
print(f"Valor: '{texto}',     Tipo: {type(texto)},      Clase: {type(texto).__name__}")
print(f"Valor: {booleano},               Tipo: {type(booleano)},     Clase: {type(booleano).__name__}")
print(f"Valor: {lista},    Tipo: {type(lista)},     Clase: {type(lista).__name__}")
