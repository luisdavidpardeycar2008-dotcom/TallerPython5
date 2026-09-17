
# Contadores para las estadísticas finales
pares = 0
impares = 0
mayores_50 = 0

# Ciclo externo: Genera los números de las tablas (del 1 al 10)
for i in range(1, 11):
    print("TABLA DEL " + str(i))
    
    # Ciclo interno: Multiplica el número actual por los valores del 1 al 10
    for j in range(1, 11):
        resultado = i * j
        print(str(i) + " × " + str(j) + " = " + str(resultado))
        
        # Evaluar si el resultado es par o impar
        if resultado % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
            
        # Evaluar si el resultado es mayor que 50
        if resultado > 50:
            mayores_50 = mayores_50 + 1

# MOSTRAR ESTADÍSTICAS
print("--- ESTADÍSTICAS GENERALES ---")
print("Cantidad de resultados pares:", pares)
print("Cantidad de resultados impares:", impares)
print("Cantidad de resultados mayores que 50:", mayores_50)