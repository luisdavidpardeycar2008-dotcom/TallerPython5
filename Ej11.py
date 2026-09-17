import random
# 1. SELECCIÓN Y VALIDACIÓN DE DIFICULTAD
opcion = 0

while opcion < 1 or opcion > 3:
    print("--- MENÚ DE DIFICULTAD ---")
    print("1. Fácil (1 a 20, 6 intentos)")
    print("2. Intermedio (1 a 50, 5 intentos)")
    print("3. Difícil (1 a 100, 4 intentos)")
    
    try:
        opcion = int(input("Seleccione una dificultad (1-3): "))
        if opcion < 1 or opcion > 3:
            print("Error: Selección no válida. Intente de nuevo.")
    except ValueError:
        print("Error: Debe ingresar un número válido (1, 2 o 3).")
        opcion = 0

# Configurar límite y cantidad de intentos según la opción elegida
if opcion == 1:
    limite = 20
    intentos_restantes = 6
elif opcion == 2:
    limite = 50
    intentos_restantes = 5
else:
    limite = 100
    intentos_restantes = 4

# Generar número aleatorio
numero_secreto = random.randint(1, limite)
adivinado = False

print("¡He generado un número secreto entre 1 y " + str(limite) + "!")

# 2. BUCLE DE JUEGO
while intentos_restantes > 0 and not adivinado:
    print("Intentos disponibles:", intentos_restantes)
    while True:
        try:
            intento = int(input("Ingrese su número: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
    
    # Descontar el intento utilizado
    intentos_restantes = intentos_restantes - 1
    
    if intento == numero_secreto:
        adivinado = True
        print("Número correcto.")
        
        # Cálculo del puntaje con los intentos sobrantes
        puntaje = intentos_restantes * 20
        print("¡Felicidades! Su puntaje es:", puntaje)
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

# 3. VERIFICAR SI AGOTÓ LOS INTENTOS
if not adivinado:
    print("Se han agotado los intentos. ¡Game Over!")
    print("El número secreto era:", numero_secreto)