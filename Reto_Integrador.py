
# RETO INTEGRADOR: SISTEMA DE VENTAS
# Variables globales para acumular estadísticas
opcion = 0
cantidad_ventas = 0
total_bruto = 0.0
total_descuentos = 0.0
total_recargos = 0.0
total_recibido = 0.0

# Contadores específicos
pagos_efectivo = 0
pagos_tarjeta = 0
pagos_transferencia = 0
clientes_descuento = 0

# Variables para mayor y menor venta
venta_mayor = None
venta_menor = None
cliente_mayor = ""
cliente_menor = ""

# Control de estado de caja
caja_cerrada = False

# BUCLE PRINCIPAL DEL MENÚ
while opcion != 5:
    
    print("-------SISTEMA DE VENTAS--------- ")
    
    print("1. Registrar una venta")
    print("2. Consultar resumen de ventas")
    print("3. Consultar venta mayor y menor")
    print("4. Aplicar cierre de caja")
    print("5. Salir")
    print("==========================================")

    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            break
        except ValueError:
            print("Error: Ingrese un número válido del 1 al 5.")

    
    # OPCIÓN 1: REGISTRAR UNA VENTA
    
    if opcion == 1:
        if caja_cerrada:
            print("Error: La caja ya ha sido cerrada. No se pueden registrar más ventas.")
        else:
            print("--- NUEVA VENTA ---")
            nombre_cliente = input("Nombre del cliente: ")

            # Validar cantidad de productos (> 0)
            cantidad_productos = 0
            while cantidad_productos <= 0:
                try:
                    cantidad_productos = int(input("Cantidad de productos a comprar: "))
                    if cantidad_productos <= 0:
                        print("Error: La cantidad de productos debe ser mayor a 0.")
                except ValueError:
                    print("Error: Debe ingresar un número entero válido.")
                    cantidad_productos = 0

            # Lectura de precios y acumulado de subtotal
            subtotal_venta = 0.0
            for i in range(1, cantidad_productos + 1):
                precio_producto = 0.0
                while precio_producto <= 0:
                    try:
                        precio_producto = float(input("Precio del producto " + str(i) + ": $"))
                        if precio_producto <= 0:
                            print("Error: El precio debe ser mayor a 0.")
                    except ValueError:
                        print("Error: Debe ingresar un precio numérico válido.")
                        precio_producto = 0.0
                subtotal_venta = subtotal_venta + precio_producto

            # Validar medio de pago
            medio_pago = ""
            while medio_pago != "efectivo" and medio_pago != "tarjeta" and medio_pago != "transferencia":
                medio_pago = input("Medio de pago (efectivo / tarjeta / transferencia): ").lower()
                if medio_pago != "efectivo" and medio_pago != "tarjeta" and medio_pago != "transferencia":
                    print("Error: Ingrese un medio de pago válido.")

            # CÁLCULO DE DESCUENTOS Y RECARGOS
            descuento_venta = 0.0
            recargo_venta = 0.0

            # Regla 1: Descuento del 10% si supera los $500.000
            if subtotal_venta > 500000:
                descuento_venta = descuento_venta + (subtotal_venta * 0.10)

            # Regla 2: Descuento adicional del 3% si paga en efectivo y supera los $200.000
            if medio_pago == "efectivo" and subtotal_venta > 200000:
                descuento_venta = descuento_venta + (subtotal_venta * 0.03)

            # Regla 3: Recargo del 2% si paga con tarjeta
            if medio_pago == "tarjeta":
                recargo_venta = subtotal_venta * 0.02

            # Total neto de la venta
            total_final = subtotal_venta - descuento_venta + recargo_venta

            # ACTUALIZACIÓN DE ACUMULADORES GLOBALES
            cantidad_ventas = cantidad_ventas + 1
            total_bruto = total_bruto + subtotal_venta
            total_descuentos = total_descuentos + descuento_venta
            total_recargos = total_recargos + recargo_venta
            total_recibido = total_recibido + total_final

            # Conteo por medio de pago
            if medio_pago == "efectivo":
                pagos_efectivo = pagos_efectivo + 1
            elif medio_pago == "tarjeta":
                pagos_tarjeta = pagos_tarjeta + 1
            else:
                pagos_transferencia = pagos_transferencia + 1

            # Conteo de clientes con descuento
            if descuento_venta > 0:
                clientes_descuento = clientes_descuento + 1

            # Evaluación de venta mayor y menor
            if venta_mayor is None or total_final > venta_mayor:
                venta_mayor = total_final
                cliente_mayor = nombre_cliente

            if venta_menor is None or total_final < venta_menor:
                venta_menor = total_final
                cliente_menor = nombre_cliente

            # Imprimir comprobante
            print("--- COMPROBANTE DE REGISTRO ---")
            print("Cliente:", nombre_cliente)
            print("Subtotal bruto: $" + str(subtotal_venta))
            print("Descuentos: $" + str(descuento_venta))
            print("Recargos: $" + str(recargo_venta))
            print("Total a pagar: $" + str(total_final))

    
    # OPCIÓN 2: CONSULTAR RESUMEN DE VENTAS
    
    elif opcion == 2:
        if cantidad_ventas == 0:
            print("Error: No se han registrado ventas aún en el sistema.")
        else:
            promedio = total_recibido / cantidad_ventas
            print("--- RESUMEN GENERAL DE VENTAS ---")
            print("Cantidad de ventas realizadas:", cantidad_ventas)
            print("Valor total antes de descuentos (Bruto): $" + str(total_bruto))
            print("Total de descuentos otorgados: $" + str(total_descuentos))
            print("Total de recargos aplicados: $" + str(total_recargos))
            print("Dinero definitivo recibido (Neto): $" + str(total_recibido))
            print("Promedio de ventas: $" + str(promedio))
            print("Desglose por medios de pago:")
            print(" - Efectivo:", pagos_efectivo)
            print(" - Tarjeta:", pagos_tarjeta)
            print(" - Transferencia:", pagos_transferencia)
            print("Clientes beneficiados con descuento:", clientes_descuento)

    
    # OPCIÓN 3: CONSULTAR VENTA MAYOR Y MENOR
    
    elif opcion == 3:
        if cantidad_ventas == 0:
            print("Error: No se han registrado ventas aún en el sistema.")
        else:
            print("--- VENTA MAYOR Y MENOR ---")
            print("Venta más alta: $" + str(venta_mayor) + " (Cliente: " + cliente_mayor + ")")
            print("Venta más baja: $" + str(venta_menor) + " (Cliente: " + cliente_menor + ")")

    
    # OPCIÓN 4: APLICAR CIERRE DE CAJA
    
    elif opcion == 4:
        if cantidad_ventas == 0:
            print("Error: No se puede aplicar el cierre de caja sin ventas registradas.")
        else:
            promedio = total_recibido / cantidad_ventas
            
            print("------REPORTE DE CIERRE DE CAJA------")
            
            print("Total de ventas procesadas:", cantidad_ventas)
            print("Recaudo Bruto: $" + str(total_bruto))
            print("Descuentos aplicados: $" + str(total_descuentos))
            print("Recargos cobrados: $" + str(total_recargos))
            print("DINERO DEFINITIVO EN CAJA: $" + str(total_recibido))
            print("Promedio por venta: $" + str(promedio))
            print("Venta máxima: $" + str(venta_mayor) + " (" + cliente_mayor + ")")
            print("Venta mínima: $" + str(venta_menor) + " (" + cliente_menor + ")")
            print("Pagos registrados:")
            print(" - Efectivo:", pagos_efectivo)
            print(" - Tarjeta:", pagos_tarjeta)
            print(" - Transferencia:", pagos_transferencia)
            print("Clientes con descuento:", clientes_descuento)

            caja_cerrada = True
            print("¡Cierre de caja finalizado exitosamente! El registro de ventas ha sido bloqueado.")

    
    # OPCIÓN 5: SALIR
   
    elif opcion == 5:
        print("Saliendo del sistema de ventas. ¡Que tenga un excelente día!")

    # OPCIÓN INVÁLIDA
    else:
        print("Opción no válida. Por favor, seleccione un número del 1 al 5.")