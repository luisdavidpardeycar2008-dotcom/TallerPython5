
# 1. VALIDACIÓN DE ENTRADA
# Usamos un ciclo while para solicitar un número entre 3 y 10.
n = 0

while n < 3 or n > 10:
    n = int(input("Ingrese un número entre 3 y 10: "))
    if n < 3 or n > 10:
        print("Error: El número debe estar en el rango de 3 a 10.")

print()  # Línea en blanco para separar

# 2. PARTE CRECIENTE (Líneas 1 a n)
for i in range(1, n + 1):
    linea = ""
    for j in range(1, i + 1):
        if linea == "":
            linea = str(j)
        else:
            linea = linea + " " + str(j)
    print(linea)

# 3. PARTE DECRECIENTE (Líneas n-1 a 1)
for i in range(n - 1, 0, -1):
    linea = ""
    for j in range(1, i + 1):
        if linea == "":
            linea = str(j)
        else:
            linea = linea + " " + str(j)
    print(linea)