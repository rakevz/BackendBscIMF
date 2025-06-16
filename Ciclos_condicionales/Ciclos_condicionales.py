# ciclos_condicionales.py

# Ejemplo de bucle for
print("=== Ejemplo de bucle for ===")
for i in range(5):  # Itera sobre un rango de 0 a 4
    print(f"Iteración {i}")

# Ejemplo de bucle while
print("\n=== Ejemplo de bucle while ===")
contador = 0
while contador < 5:  # Ejecuta mientras contador sea menor que 5
    print(f"Contador: {contador}")
    contador += 1  # Incrementa el contador

# Ejemplo de condicionales
print("\n=== Ejemplo de condicionales ===")
numero = 10
if numero > 0:
    print(f"{numero} es positivo.")
elif numero < 0:
    print(f"{numero} es negativo.")
else:
    print(f"{numero} es cero.")

# Ejemplo de cláusulas especiales en bucles
print("\n=== Ejemplo de break y continue ===")
for i in range(10):
    if i == 3:
        print("Se encontró el número 3, se termina el bucle.")
        break  # Termina el bucle cuando i es 3
    print(f"Valor de i: {i}")

print("\n=== Ejemplo de continue ===")
for i in range(5):
    if i == 2:
        print("Se encontró el número 2, se salta esta iteración.")
        continue  # Salta a la siguiente iteración cuando i es 2
    print(f"Valor de i: {i}")

# Ejemplo de else en bucles
print("\n=== Ejemplo de else en bucles ===")
for i in range(5):
    print(f"Valor de i: {i}")
else:
    print("El bucle for ha terminado normalmente (sin break).")
