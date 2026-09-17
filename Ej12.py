

# Datos iniciales del sistema
usuario_correcto = "administrador"
clave_correcta = "Python2026"

intentos_restantes = 3
acceso_concedido = False

# 1. BUCLE DE AUTENTICACIÓN (Máximo 3 intentos)
while intentos_restantes > 0 and not acceso_concedido:
    print("--- INICIO DE SESIÓN ---")
    usuario_ingresado = input("Usuario: ")
    clave_ingresada = input("Contraseña: ")
    
    # Validar credenciales
    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        acceso_concedido = True
        print("¡Acceso concedido! Bienvenido al sistema.")
    else:
        intentos_restantes = intentos_restantes - 1
        
        # Evaluar el tipo de error específico
        if usuario_ingresado != usuario_correcto and clave_ingresada != clave_correcta:
            print("Error: Tanto el usuario como la contraseña son incorrectos.")
        elif usuario_ingresado != usuario_correcto:
            print("Error: El usuario es incorrecto.")
        else:
            print("Error: La contraseña es incorrecta.")
            
        # Informar intentos restantes si no se ha bloqueado
        if intentos_restantes > 0:
            print("Intentos restantes:", intentos_restantes, "\n")

# 2. SISTEMA BLOQUEADO SI SE AGOTARON LOS INTENTOS
if not acceso_concedido:
    print("Error: Ha superado el límite de 3 intentos fallidos. El sistema ha sido bloqueado.")

# 3. MENÚ INTERACTIVO (Solo si el acceso fue correcto)
if acceso_concedido:
    opcion = 0
    
    while opcion != 3:
        print("--- MENÚ DEL SISTEMA ---")
        print("1. Consultar información")
        print("2. Cambiar contraseña")
        print("3. Cerrar sesión")
        
        while True:
            try:
                opcion = int(input("Seleccione una opción (1-3): "))
                break
            except ValueError:
                print("Error: Debe ingresar un número válido (1, 2 o 3).")
        
        if opcion == 1:
            print("[Información del sistema]")
            print("Usuario activo:", usuario_correcto)
            print("Estado: Sesión iniciada correctamente.")
            
        elif opcion == 2:
            clave_actual = input("Ingrese la contraseña actual: ")
            if clave_actual == clave_correcta:
                nueva_clave = input("Ingrese la nueva contraseña: ")
                if nueva_clave != "":
                    clave_correcta = nueva_clave
                    print("¡Contraseña actualizada con éxito!")
                else:
                    print("Error: La contraseña no puede estar vacía.")
            else:
                print("Error: La contraseña actual es incorrecta. No se realiza ningún cambio.")
                
        elif opcion == 3:
            print("Sesión cerrada correctamente. ¡Hasta luego!")
            
        else:
            print("Opción no válida. Por favor, seleccione un número entre 1 y 3.")