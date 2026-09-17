"""
TALLER AVANZADO DE PYTHON
EXPLICACIÓN DE IF, FOR Y WHILE
TABLA DE PRUEBAS

============================================================
1. EXPLICACIÓN DEL USO DE IF, FOR Y WHILE
============================================================

1.1. ESTRUCTURA IF
------------------

La estructura if se utiliza para tomar decisiones dentro de un programa.
Su función es evaluar una condición y ejecutar un bloque de instrucciones
solamente cuando dicha condición se cumple.

Cuando existen varias posibilidades, se pueden utilizar las estructuras
elif y else.

Estructura básica:

if condicion:
    # Instrucciones que se ejecutan si la condición es verdadera.
elif otra_condicion:
    # Instrucciones que se ejecutan si la segunda condición es verdadera.
else:
    # Instrucciones que se ejecutan cuando ninguna condición anterior se cumple.

En los ejercicios del taller, la estructura if se utiliza principalmente
para validar datos, clasificar resultados y aplicar diferentes reglas.

Por ejemplo, en el ejercicio de clasificación de triángulos se utiliza
para determinar el tipo de triángulo según la longitud de sus lados.

Si los tres lados son iguales, el triángulo es equilátero.
Si solamente dos lados son iguales, el triángulo es isósceles.
Si todos los lados son diferentes, el triángulo es escaleno.

También se utiliza en el reto integrador para aplicar descuentos y recargos.
Por ejemplo, si una compra supera los $500.000, se aplica un descuento
del 10 %. Si el pago se realiza con tarjeta, se aplica un recargo del 2 %.

Por lo tanto, if permite que el programa tome decisiones dependiendo de
los datos ingresados o de los resultados obtenidos durante la ejecución.


1.2. ESTRUCTURA FOR
-------------------

La estructura for se utiliza para repetir un conjunto de instrucciones
una cantidad determinada de veces.

Normalmente se utiliza cuando se conoce previamente el número de
repeticiones que se deben realizar.

Estructura básica:

for variable in range(inicio, fin):
    # Instrucciones que se repiten.

La función range() permite definir los valores que tomará la variable
durante cada repetición.

Por ejemplo:

for numero in range(1, 6):

genera los números:

1, 2, 3, 4 y 5.

El valor final de range() no se incluye, por esta razón se utiliza 6
cuando se necesita llegar hasta 5.

En el taller, el ciclo for se utiliza en diferentes ejercicios.

En el sistema de calificaciones se utiliza para recorrer la cantidad de
estudiantes y también para solicitar las tres calificaciones de cada uno.

En las tablas de multiplicar se utilizan ciclos for anidados. El primer
ciclo controla la tabla que se está generando y el segundo ciclo controla
los números por los cuales se realiza la multiplicación.

Ejemplo conceptual:

for tabla in range(1, 11):
    for multiplicador in range(1, 11):
        resultado = tabla * multiplicador

Un ciclo anidado significa que existe un ciclo dentro de otro ciclo.

También se utilizan ciclos for en el patrón numérico y en otros ejercicios
en los que se conoce exactamente cuántas repeticiones se necesitan.


1.3. ESTRUCTURA WHILE
---------------------

La estructura while se utiliza para repetir instrucciones mientras una
condición sea verdadera.

A diferencia del ciclo for, se utiliza principalmente cuando no se conoce
exactamente cuántas veces será necesario repetir una acción.

Estructura básica:

while condicion:
    # Instrucciones que se repiten mientras la condición sea verdadera.

En este taller se utiliza principalmente para realizar validaciones y
para mantener activos los menús interactivos.

Por ejemplo, cuando se solicita un número positivo, el programa puede
seguir preguntando mientras el valor ingresado sea menor o igual a cero.

Ejemplo:

numero = 0

while numero <= 0:
    numero = int(input("Ingrese un número positivo: "))

De esta forma, el programa no continúa hasta recibir un dato válido.

Otro uso importante aparece en los menús.

En el reto integrador se utiliza una estructura similar a:

opcion = 0

while opcion != 5:
    # Mostrar el menú.
    # Solicitar una opción.
    # Ejecutar la opción seleccionada.

El ciclo permanece activo mientras el usuario no seleccione la opción
de salir.

También se utiliza while en ejercicios como el cajero automático,
el juego de adivinanza, el control de acceso y las validaciones de datos.


1.4. DIFERENCIA ENTRE IF, FOR Y WHILE
-------------------------------------

IF:
Se utiliza para tomar decisiones.
Ejemplo: determinar si un número es positivo o negativo.

FOR:
Se utiliza para repetir instrucciones una cantidad conocida de veces.
Ejemplo: solicitar las notas de una cantidad determinada de estudiantes.

WHILE:
Se utiliza para repetir instrucciones mientras se cumpla una condición.
Ejemplo: seguir solicitando un dato mientras sea incorrecto.

En resumen:

if    -> permite decidir.
for   -> permite repetir una cantidad conocida de veces.
while -> permite repetir mientras una condición sea verdadera.


============================================================
2. TABLA DE PRUEBAS
============================================================

La siguiente tabla contiene casos normales, incorrectos y valores límite
para comprobar el funcionamiento de cada programa.

IMPORTANTE:
El resultado esperado corresponde al comportamiento que debería presentar
el programa. Antes de tomar las capturas definitivas se debe comprobar que
cada caso produzca realmente dicho resultado.


EJERCICIO 1. CLASIFICACIÓN DE TRIÁNGULOS
-----------------------------------------

Prueba: Normal
Entrada:
lado1 = 3
lado2 = 4
lado3 = 5
Resultado esperado:
Los lados forman un triángulo y se clasifica como escaleno.

Prueba: Incorrecta
Entrada:
lado1 = -2
lado2 = 4
lado3 = 5
Resultado esperado:
El programa debe rechazar el valor negativo y solicitar nuevamente un
valor válido.

Prueba: Valor límite
Entrada:
lado1 = 1
lado2 = 1
lado3 = 2
Resultado esperado:
Los valores son positivos, pero no forman un triángulo porque
1 + 1 no es mayor que 2.


EJERCICIO 2. SISTEMA DE CALIFICACIONES
--------------------------------------

Prueba: Normal
Entrada:
Cantidad de estudiantes = 1
Notas = 4.0, 4.0, 4.0
Resultado esperado:
Promedio = 4.0.
Clasificación = Sobresaliente.
El estudiante se contabiliza como aprobado.

Prueba: Incorrecta
Entrada:
Cantidad de estudiantes = 0
o una calificación = 5.5
Resultado esperado:
El programa debe rechazar el dato y solicitar nuevamente un valor válido.

Prueba: Valor límite
Entrada:
Notas = 0.0, 0.0, 0.0
Resultado esperado:
Promedio = 0.0.
Clasificación = Reprobado.
El valor 0.0 debe ser aceptado porque pertenece al rango permitido.

También puede comprobarse el límite superior utilizando:
5.0, 5.0, 5.0
Resultado esperado:
Promedio = 5.0.
Clasificación = Excelente.


EJERCICIO 3. NÚMERO PRIMO
-------------------------

Prueba: Normal
Entrada:
15
Resultado esperado:
Divisores: 1, 3, 5, 15.
El número 15 no es primo.

Prueba: Incorrecta
Entrada:
1
Resultado esperado:
El programa debe rechazarlo porque se solicita un entero mayor que 1.

Prueba: Valor límite
Entrada:
2
Resultado esperado:
Divisores: 1 y 2.
El número 2 es primo.
Es el menor número primo permitido por el ejercicio.


EJERCICIO 4. CAJERO AUTOMÁTICO
------------------------------

Prueba: Normal
Entrada:
Opción: Depositar dinero.
Valor del depósito: 50000
Resultado esperado:
El saldo aumenta en $50.000 y se registra un depósito.

Prueba: Incorrecta
Entrada:
Opción: Retirar dinero.
Valor del retiro: 5000
Resultado esperado:
El programa debe informar que no se permiten retiros inferiores a $10.000.

Prueba: Valor límite
Entrada:
Opción: Retirar dinero.
Valor del retiro: 10000
Resultado esperado:
El retiro debe ser aceptado si existe saldo suficiente.
Además del retiro se debe descontar la comisión de $4.500.


EJERCICIO 5. FACTURA DE SUPERMERCADO
------------------------------------

Prueba: Normal
Entrada:
Producto: Arroz
Precio: 10000
Cantidad: 2
Tipo: alimento
Resultado esperado:
Subtotal = $20.000.
Descuento del producto = 5 %.
Descuento = $1.000.
Total del producto después del descuento = $19.000.

Prueba: Incorrecta
Entrada:
Precio = 0
o cantidad = 0
Resultado esperado:
El programa debe rechazar el dato porque precio y cantidad deben ser
positivos.

Prueba: Valor límite
Entrada:
Subtotal general = 300000
Resultado esperado:
No debe aplicarse el descuento general adicional del 5 %, porque el
enunciado indica que el subtotal debe superar los $300.000.


EJERCICIO 6. ESTADÍSTICAS DE NÚMEROS
------------------------------------

Prueba: Normal
Entrada:
5
-2
4
0
Resultado esperado:
Cantidad de números = 3.
Positivos = 2.
Negativos = 1.
Pares = 2.
Impares = 1.
Suma total = 7.
Promedio aproximado = 2.33.
Mayor = 5.
Menor = -2.

Prueba: Incorrecta
Entrada:
abc
Resultado esperado:
El programa debe informar que el dato no es un número entero válido y
solicitar nuevamente la entrada.

Prueba: Valor límite
Entrada:
0 como primer número
Resultado esperado:
El programa debe finalizar el ingreso e informar que no existen números
para realizar los cálculos.


EJERCICIO 7. CONVERSIÓN DECIMAL A BINARIO
-----------------------------------------

Prueba: Normal
Entrada:
25
Resultado esperado:
Divisiones sucesivas entre 2.
Resultado binario = 11001.

Prueba: Incorrecta
Entrada:
-5
Resultado esperado:
El programa debe rechazar el número porque debe ser positivo.

Prueba: Valor límite
Entrada:
1
Resultado esperado:
Resultado binario = 1.


EJERCICIO 8. SERIE DE FIBONACCI
-------------------------------

Prueba: Normal
Entrada:
Cantidad de términos = 8
Resultado esperado:
Serie:
0, 1, 1, 2, 3, 5, 8, 13
Suma = 33.
Pares = 3, contando 0, 2 y 8.
Impares = 5.

Prueba: Incorrecta
Entrada:
0
Resultado esperado:
El programa debe rechazar la cantidad porque se requiere al menos un
término.

Prueba: Valor límite
Entrada:
1
Resultado esperado:
Serie = 0.
Suma = 0.
Cantidad de términos pares = 1.
Cantidad de términos impares = 0.


EJERCICIO 9. TABLAS DE MULTIPLICAR
----------------------------------

Prueba: Normal
Entrada:
No requiere datos de entrada.
Resultado esperado:
El programa genera las tablas del 1 al 10 y calcula las cantidades de
resultados pares, impares y mayores que 50.

Prueba: Incorrecta
Entrada:
No aplica.
Resultado esperado:
No existe entrada incorrecta porque el programa genera automáticamente
las tablas.

Prueba: Valor límite
Entrada:
No requiere datos.
Resultado esperado:
Debe generar correctamente desde la TABLA DEL 1 hasta la TABLA DEL 10,
incluyendo la multiplicación por 1 y por 10.


EJERCICIO 10. PATRÓN NUMÉRICO
-----------------------------

Prueba: Normal
Entrada:
5
Resultado esperado:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

Prueba: Incorrecta
Entrada:
2
Resultado esperado:
El programa debe rechazarlo porque el número debe estar entre 3 y 10.

Prueba: Valor límite
Entrada:
3
Resultado esperado:
El programa debe aceptar el valor porque 3 es el mínimo permitido y
generar correctamente el patrón correspondiente.

También puede comprobarse el límite superior utilizando 10.


EJERCICIO 11. JUEGO DE ADIVINANZA
---------------------------------

Prueba: Normal
Entrada:
Dificultad = 1
Intentos dentro del rango de 1 a 20.
Resultado esperado:
El programa genera un número secreto entre 1 y 20, informa si el número
secreto es mayor o menor y permite máximo 6 intentos.

Prueba: Incorrecta
Entrada:
Dificultad = 4
Resultado esperado:
El programa debe rechazar la opción porque solamente existen los niveles
1, 2 y 3.

También debe rechazarse una adivinanza que se encuentre fuera del rango
correspondiente al nivel seleccionado.

Prueba: Valor límite
Entrada:
Dificultad = 3
Adivinanza = 1 o 100
Resultado esperado:
Los valores 1 y 100 deben ser aceptados como intentos válidos porque
pertenecen al rango del nivel difícil.


EJERCICIO 12. CONTROL DE ACCESO
-------------------------------

Prueba: Normal
Entrada:
Usuario = administrador
Contraseña = Python2026
Resultado esperado:
Acceso concedido y visualización del menú:
1. Consultar información
2. Cambiar contraseña
3. Cerrar sesión

Prueba: Incorrecta
Entrada:
Usuario = usuario
Contraseña = clave
Resultado esperado:
El programa debe indicar que el usuario y la contraseña son incorrectos,
descontar un intento y mostrar cuántos quedan.

Prueba: Valor límite
Entrada:
Primer intento incorrecto.
Segundo intento incorrecto.
Tercer intento correcto.
Resultado esperado:
El sistema debe permitir el acceso porque el tercer intento todavía es
válido.

Si también falla el tercer intento, el sistema debe quedar bloqueado.


RETO INTEGRADOR. SISTEMA DE VENTAS
----------------------------------

Prueba: Normal
Entrada:
Cliente = Ana
Cantidad de productos = 1
Precio = 100000
Medio de pago = transferencia
Resultado esperado:
Subtotal = $100.000.
No se aplica descuento.
No se aplica recargo.
Total recibido = $100.000.
Se registra una venta por transferencia.

Prueba: Incorrecta
Entrada:
Cantidad de productos = 0
o precio = 0
o medio de pago diferente de efectivo, tarjeta o transferencia.
Resultado esperado:
El programa debe rechazar el dato inválido y solicitar nuevamente la
información correspondiente.

Prueba: Valor límite
Entrada:
Subtotal de la compra = 500000
Medio de pago = transferencia
Resultado esperado:
No se aplica el descuento del 10 %, porque la regla indica que la compra
debe superar los $500.000.

Prueba adicional de valor límite:
Subtotal de la compra = 200000
Medio de pago = efectivo
Resultado esperado:
No se aplica el descuento adicional del 3 %, porque la compra debe superar
los $200.000.

También se puede comprobar:
Subtotal = 200001
Medio de pago = efectivo
Resultado esperado:
Sí se aplica el descuento adicional del 3 %.


"""
