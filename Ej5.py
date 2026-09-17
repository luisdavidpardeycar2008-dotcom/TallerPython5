

# 1. VALIDACIÓN DE CANTIDAD DE PRODUCTOS
cantidad_productos = 0

while cantidad_productos <= 0:
    cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))
    if cantidad_productos <= 0:
        print("Error: La cantidad de productos debe ser mayor a 0.")

# ACUMULADORES GENERALES
subtotal_bruto_general = 0.0
total_descuentos_productos = 0.0

# 2. REGISTRO Y CÁLCULO POR PRODUCTO
for i in range(1, cantidad_productos + 1):
    print("--- PRODUCTO", i, "---")
    nombre = input("Nombre del producto: ")
    
    # Validar precio positivo
    precio = 0.0
    while precio <= 0:
        precio = float(input("Precio unitario: $"))
        if precio <= 0:
            print("Error: El precio debe ser mayor a 0.")
            
    # Validar cantidad positiva
    cantidad = 0
    while cantidad <= 0:
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor a 0.")
            
    # Validar tipo de producto (alimento, aseo, otro)
    tipo = ""
    while tipo != "alimento" and tipo != "aseo" and tipo != "otro":
        tipo = input("Tipo de producto (alimento / aseo / otro): ").lower()
        if tipo != "alimento" and tipo != "aseo" and tipo != "otro":
            print("Error: Ingrese una categoría válida (alimento, aseo u otro).")

    # Cálculos por producto
    subtotal_producto = precio * cantidad
    descuento_producto = 0.0
    
    # Condicionales para descuentos individuales
    if tipo == "alimento":
        descuento_producto = subtotal_producto * 0.05
    elif tipo == "aseo" and cantidad >= 3:
        descuento_producto = subtotal_producto * 0.10
    else:
        descuento_producto = 0.0
        
    # Mostrar resultados por producto
    print(" Subtotal del producto: $" + str(subtotal_producto))
    print(" Descuento aplicado al producto: $" + str(descuento_producto))
    
    # Acumular en los totales generales
    subtotal_bruto_general = subtotal_bruto_general + subtotal_producto
    total_descuentos_productos = total_descuentos_productos + descuento_producto

# 3. CÁLCULO DE DESCUENTO GENERAL Y TOTALES FINALES
total_antes_descuento_general = subtotal_bruto_general - total_descuentos_productos
descuento_general = 0.0

# Evaluación de la condición de subtotal mayor a $300.000
if subtotal_bruto_general > 300000:
    descuento_general = total_antes_descuento_general * 0.05

total_descuentos = total_descuentos_productos + descuento_general
total_definitivo = subtotal_bruto_general - total_descuentos

# 4. MOSTRAR RESUMEN FINAL
print("--------- RESUMEN DE COMPRA -----------")
print("Total antes del descuento general: $" + str(total_antes_descuento_general))
print("Descuento general (5% por compra > $300.000): $" + str(descuento_general))
print("Total de descuentos acumulados: $" + str(total_descuentos))
print("Total definitivo a pagar: $" + str(total_definitivo))