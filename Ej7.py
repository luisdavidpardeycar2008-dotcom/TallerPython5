
# 1. VALIDACIÓN DE ENTRADA
numero = 0

while numero <= 0:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero <= 0:
        print("Error: El número debe ser mayor a 0.")

# Guardamos el valor original para la impresión final
numero_original = numero
binario = ""

# 2. DIVISIONES SUCESIVAS ENTRE 2
while numero > 0:
    residuo = numero % 2
    binario = str(residuo) + binario  # Se concatena al inicio para revertir el orden
    numero = numero // 2               # División entera

# 3. MOSTRAR RESULTADO
print("Número decimal:", numero_original)
print("Resultado binario:", binario)