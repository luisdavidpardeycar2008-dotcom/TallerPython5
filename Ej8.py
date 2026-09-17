
# 1. VALIDACIÓN DE ENTRADA
terminos = 0

while terminos <= 0:
    terminos = int(input("Ingrese la cantidad de términos a generar: "))
    if terminos <= 0:
        print("Error: La cantidad de términos debe ser mayor a 0.")

# Variables iniciales de Fibonacci
a = 0
b = 1

# Acumuladores y contadores
suma = 0
pares = 0
impares = 0
serie_texto = ""

# 2. GENERACIÓN DE LA SERIE Y CÁLCULOS
for i in range(terminos):
    # Formatear la cadena de la serie
    if serie_texto == "":
        serie_texto = str(a)
    else:
        serie_texto = serie_texto + ", " + str(a)

    # Acumular suma
    suma = suma + a

    # Evaluar si el término actual es par o impar
    if a % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    # Calcular el siguiente término
    siguiente = a + b
    a = b
    b = siguiente

# 3. MOSTRAR RESULTADOS
print("--- RESULTADOS ---")
print("Serie de Fibonacci:", serie_texto)
print("Suma total de los términos:", suma)
print("Cantidad de términos pares:", pares)
print("Cantidad de términos impares:", impares)