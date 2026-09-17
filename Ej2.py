while True:
    try:
        cantidad_estudiantes = int(input("Cuantos Estudiantes Son: "))
        if cantidad_estudiantes > 0:
            break
        print("Error: La cantidad de estudiantes debe ser mayor a 0.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

aprobados = 0
reprobados = 0
suma_promedios = 0.0
promedio_alto = 0.0
promedio_bajo = 0.0

for i in range(1, cantidad_estudiantes + 1):
    print("---Estudiante ", i, "--")
    suma_notas = 0.0

    for j in range(1, 4):
        nota = -1.0
        while nota < 0.0 or nota > 5.0:
            try:
                nota = float(input(f"Ingrese la nota {j} (0.0 a 5.0): "))
                if nota < 0.0 or nota > 5.0:
                    print("nota invalida, debe estar entre (0.0 a 5.0)")
            except ValueError:
                print("Error: Debe ingresar un valor numérico válido para la nota.")
                nota = -1.0
        suma_notas = suma_notas + nota

    promedio = suma_notas / 3.0
    print("Promedio Obtenido:", round(promedio, 2))

    if promedio <= 2.9:
        print("Clasificacion, Reprobado")
        reprobados = reprobados + 1
    elif promedio <= 3.9:
        print("Clasificacion, Aprobado")
        aprobados = aprobados + 1
    elif promedio <= 4.5:
        print("Clasificacion, Sobresaliente")
        aprobados = aprobados + 1
    else:
        print("Clasificacion, Excelente")
        aprobados = aprobados + 1

    suma_promedios = suma_promedios + promedio

    if i == 1:
        promedio_alto = promedio
        promedio_bajo = promedio
    else:
        if promedio > promedio_alto:
            promedio_alto = promedio
        if promedio < promedio_bajo:
            promedio_bajo = promedio

print("\n==============================")
print("       RESULTADOS FINALES     ")
print("==============================")
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)
print("Promedio general del grupo:", round(suma_promedios / cantidad_estudiantes, 2))
print("Promedio más alto:", round(promedio_alto, 2))
print("Promedio más bajo:", round(promedio_bajo, 2))









    
