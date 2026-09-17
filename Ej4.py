



# ==========================================
# EJERCICIO 4: CAJERO AUTOMÁTICO INTERACTIVO
# ==========================================

saldo = 1500000
COSTO_RETIRO = 4500
contador_depositos = 0
contador_retiros = 0
opcion = 0

while opcion != 5:
    print("\n--- MENÚ CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver movimientos realizados")
    print("5. Salir")
    
    opcion = int(input("Seleccione una opción (1-5): "))
    
    # OPCIÓN 1: CONSULTAR SALDO
    if opcion == 1:
        print("\nSaldo disponible: $" + str(saldo))
        
    # OPCIÓN 2: DEPOSITAR DINERO
    elif opcion == 2:
        monto_deposito = float(input("\nIngrese la cantidad a depositar: $"))
        
        # Validación: Depósitos mayores a cero
        if monto_deposito > 0:
            saldo = saldo + monto_deposito
            contador_depositos = contador_depositos + 1
            print("Depósito exitoso. Nuevo saldo: $" + str(saldo))
        else:
            print("Error: No se permiten depósitos negativos o de $0.")
            
    # OPCIÓN 3: RETIRAR DINERO
    elif opcion == 3:
        monto_retiro = float(input("\nIngrese la cantidad a retirar (Mínimo $10.000): $"))
        
        # Validación 1: Monto mínimo de retiro
        if monto_retiro < 10000:
            print("Error: La cantidad mínima a retirar es $10.000.")
        else:
            monto_total_descuento = monto_retiro + COSTO_RETIRO
            
            # Validación 2: Saldo suficiente (monto + comisión)
            if monto_total_descuento > saldo:
                print("Error: Saldo insuficiente. El retiro más la comisión ($4.500) superan su saldo.")
            else:
                saldo = saldo - monto_total_descuento
                contador_retiros = contador_retiros + 1
                print("Retiro exitoso. Se descontaron $" + str(monto_retiro) + " + $" + str(COSTO_RETIRO) + " de comisión.")
                print("Nuevo saldo disponible: $" + str(saldo))
                
    # OPCIÓN 4: VER MOVIMIENTOS REALIZADOS
    elif opcion == 4:
        print("\n--- RESUMEN DE MOVIMIENTOS ---")
        print("Cantidad de depósitos realizados:", contador_depositos)
        print("Cantidad de retiros realizados:", contador_retiros)
        print("Saldo actual: $" + str(saldo))
        
    # OPCIÓN 5: SALIR
    elif opcion == 5:
        print("\nGracias por utilizar el cajero automático. ¡Hasta luego!")
        
    # OPCIÓN NO VÁLIDA
    else:
        print("\nOpción no válida. Ingrese un número entre 1 y 5.")