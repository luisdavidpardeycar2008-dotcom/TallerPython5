1. # VALIDACIÓN Y ENTRADA DE DATOS
# Usamos un ciclo while para asegurar que los tres lados sean números positivos.
datos_validos = False

while not datos_validos:
   print("Ingrese las longitudes de los 3 lados") 
   lado1 = int(input("Ingrese el lado 1: "))
   lado2 = int(input("Ingrese el lado 2: "))
   lado3 = int(input("Ingrese el lado 3: "))
# Validar que los lados sean estrictamente positivos (> 0)
   if lado1 > 0 and lado2 > 0 and lado3 > 0: 
    datos_validos = True # Rompe el ciclo si todos son positivos
   else:
     print("Error, Todos los datos tienen que ser mayores a 0, Intentelo de Nuevo.")

     # 2. VERIFICACIÓN DE EXISTENCIA Y CLASIFICACIÓN
# Condición de existencia: La suma de dos lados siempre debe ser mayor al tercero.
es_triangulo = (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

if es_triangulo:
    print("los lados SI forman un triangulo")
    # Condicionales anidados para determinar el tipo de triángulo
    if lado1 == lado2 and lado2 == lado3:
       print("Tipo de Triangulo: Equilatero(3 LADOS IGUALES)")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
       print("Tipo de Triangulo: Isoceles(2 LADOS IGUALES)")
    else:
       print("Tipo de Triangulo: Escaleno(3 LADOS DIFERENTES)")
else: 
   print("\nNO Forman un triangulo ya que la suma de sus dos lados no supera al lado restante")
