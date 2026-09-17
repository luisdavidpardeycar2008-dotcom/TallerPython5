
# Inicialización de contadores y acumuladores
cantidad = positivos = negativos = pares = impares = suma = 0
mayor = menor = None

numero = int(input("ingrese un numero (0 para terminar): "))
# Validación del primer número
if numero == 0:
    print("No se ingresaron numeros para analizar")
else:
    # Ciclo hasta ingresar 0
    while numero != 0:
        cantidad = cantidad + 1
        suma = suma + numero

        # Clasificación positivo / negativo
        if numero > 0:
            positivos = positivos + 1
        else:
            negativos = negativos + 1

        # Clasificación par / impar
        if numero % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1

        # Cálculo de mayor y menor
        if mayor is None or numero > mayor:
            mayor = numero
        if menor is None or numero < menor:
            menor = numero

        numero = int(input("Ingrese otro número (0 para terminar): "))

    # Mostrar Estadisticas
    print("--- ESTADÍSTICAS ---")
    print("Cantidad de números ingresados:", cantidad)
    print("Positivos:", positivos)
    print("Negativos:", negativos)
    print("Pares:", pares)
    print("Impares:", impares)
    print("Suma total:", suma)
    print("Promedio:", suma / cantidad if cantidad > 0 else 0)
    print("Número mayor:", mayor)
    print("Número menor:", menor)