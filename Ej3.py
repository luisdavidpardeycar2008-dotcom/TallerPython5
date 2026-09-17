# 1. VALIDACIÓN DE ENTRADA
# Se utiliza un ciclo while para solicitar el número hasta que sea mayor que 1.

numero = 0

while numero <= 1:
    numero = int(input("Ingrese un numero entero mayor que 1: "))
    if numero <= 1:
        print("Error: El numero tiene que ser mayor que 1")

# 2. CONTADOR Y ACUMULADOR DE DIVISORES
contador_divisores = 0
divisores_texto = ""
# Recorremos desde 1 hasta el número ingresado para evaluar la divisibilidad
for i in range(1, numero + 1):
    if numero % i == 0:
        contador_divisores = contador_divisores + 1
        # Agregamos el divisor al texto para mostrarlo al final
        if divisores_texto == "":
            divisores_texto = str(i)
        else:
            divisores_texto = divisores_texto + ", " + str (i)
# 3. MOSTRAR RESULTADOS
print("Divisores", divisores_texto)

# Un número entero mayor a 1 es primo si tiene EXACTAMENTE 2 divisores (1 y él mismo)
if contador_divisores == 2:
    print("El numero", numero, "Es primo")
else:
    print("El numero", numero, "NO es primo")