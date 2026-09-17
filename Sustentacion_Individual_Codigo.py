"""
SUSTENTACIÓN INDIVIDUAL DEL CÓDIGO
TALLER AVANZADO DE PYTHON: IF, FOR Y WHILE

============================================================
1. PRESENTACIÓN GENERAL
============================================================

En este taller se desarrollaron doce ejercicios y un reto integrador con
el objetivo de practicar estructuras básicas de programación en Python,
principalmente if, elif, else, for y while.

Durante los ejercicios también se utilizaron variables, contadores,
acumuladores, validaciones, operadores aritméticos y lógicos, ciclos
anidados y menús interactivos.

La estructura if se utilizó para tomar decisiones.
La estructura for se utilizó cuando se conocía la cantidad de repeticiones.
La estructura while se utilizó cuando una acción debía repetirse mientras
se cumpliera una condición.

Los contadores se utilizaron para registrar cuántas veces ocurrió algo.
Los acumuladores se utilizaron para ir sumando valores durante la
ejecución de los programas.


============================================================
2. EJERCICIO 1. CLASIFICACIÓN DE TRIÁNGULOS
============================================================

En este ejercicio se solicitan las longitudes de tres lados.

Primero utilizo un ciclo while para repetir el ingreso mientras los datos
no sean positivos.

Después verifico si los tres valores pueden formar un triángulo. Para eso
compruebo que la suma de cada par de lados sea mayor que el lado restante.

La variable es_triangulo almacena el resultado de esa comprobación.

Si el triángulo existe, utilizo if, elif y else para clasificarlo:

- Equilátero: los tres lados son iguales.
- Isósceles: dos lados son iguales.
- Escaleno: los tres lados son diferentes.

En este ejercicio el while se utiliza para validar y el if para tomar
decisiones.


============================================================
3. EJERCICIO 2. SISTEMA DE CALIFICACIONES
============================================================

Primero solicito la cantidad de estudiantes y valido que sea mayor que
cero.

Después utilizo un ciclo for para recorrer a todos los estudiantes.

Dentro de ese ciclo existe otro for que solicita exactamente tres notas
por estudiante. Por esta razón este ejercicio utiliza ciclos anidados.

Cada nota se valida para que se encuentre entre 0.0 y 5.0.

Las tres notas se acumulan en suma_notas y posteriormente se calcula el
promedio dividiendo esa suma entre tres.

Luego utilizo if, elif y else para clasificar el promedio como:

- Reprobado.
- Aprobado.
- Sobresaliente.
- Excelente.

También utilizo los contadores aprobados y reprobados.

La variable suma_promedios funciona como acumulador y permite obtener el
promedio general del grupo.

Las variables promedio_alto y promedio_bajo permiten determinar el mayor
y el menor promedio registrado.


============================================================
4. EJERCICIO 3. NÚMERO PRIMO
============================================================

El programa solicita un número entero mayor que uno.

El ciclo while evita continuar mientras el número sea menor o igual a uno.

Después utilizo un for desde 1 hasta el número ingresado.

Para saber si un valor es divisor utilizo el operador módulo:

numero % i == 0

Cuando el residuo es cero significa que la división es exacta.

Cada divisor encontrado aumenta contador_divisores y también se agrega
al texto de divisores.

Finalmente, si el número tiene exactamente dos divisores, que son 1 y él
mismo, se considera primo.


============================================================
5. EJERCICIO 4. CAJERO AUTOMÁTICO
============================================================

El cajero comienza con un saldo de $1.500.000.

Utilizo un while para mantener el menú funcionando hasta que el usuario
seleccione la opción 5.

Las opciones disponibles permiten:

1. Consultar saldo.
2. Depositar dinero.
3. Retirar dinero.
4. Consultar movimientos.
5. Salir.

Cuando se realiza un depósito valido que el monto sea mayor que cero y
lo sumo al saldo.

Cuando se realiza un retiro verifico primero que sea por lo menos de
$10.000.

También calculo el costo total del retiro sumando la comisión de $4.500.

Antes de retirar verifico que el usuario tenga saldo suficiente para
cubrir el retiro y la comisión.

Los contadores contador_depositos y contador_retiros permiten saber
cuántas operaciones de cada tipo se realizaron.


============================================================
6. EJERCICIO 5. FACTURA DE SUPERMERCADO
============================================================

Primero solicito la cantidad de productos y valido que sea mayor que cero.

Utilizo un for para procesar cada producto.

Por cada producto solicito:

- Nombre.
- Precio.
- Cantidad.
- Tipo de producto.

El precio y la cantidad se validan con while.

El tipo también se valida para aceptar únicamente alimento, aseo u otro.

El subtotal de cada producto se obtiene multiplicando:

precio * cantidad

Después aplico las reglas de descuento con condicionales.

Si es alimento se aplica 5 %.

Si es un producto de aseo y la cantidad es mayor o igual a tres, se
aplica 10 %.

Los demás productos no reciben descuento individual.

Los subtotales y descuentos se acumulan para generar el resumen final.

Finalmente, si el subtotal bruto general supera $300.000, se aplica un
descuento general adicional del 5 %.


============================================================
7. EJERCICIO 6. ESTADÍSTICAS DE NÚMEROS
============================================================

Este programa recibe números enteros hasta que el usuario ingresa cero.

El cero solamente sirve para finalizar el ingreso y no se incluye en los
cálculos.

Primero verifico si el primer número es cero. Si lo es, el programa
informa que no existen números para analizar.

Si no es cero, se utiliza un while para procesar los números.

En cada repetición se actualizan:

- La cantidad de números.
- La suma.
- La cantidad de positivos.
- La cantidad de negativos.
- La cantidad de pares.
- La cantidad de impares.
- El número mayor.
- El número menor.

Para determinar si un número es par utilizo:

numero % 2 == 0

El promedio se calcula dividiendo la suma entre la cantidad de números
ingresados.


============================================================
8. EJERCICIO 7. CONVERSIÓN DECIMAL A BINARIO
============================================================

Primero valido mediante while que el número decimal sea positivo.

Guardo el número original porque la variable numero se modifica durante
el procedimiento.

Para convertirlo a binario utilizo divisiones sucesivas entre dos.

El residuo se obtiene mediante:

numero % 2

La división entera se realiza mediante:

numero // 2

Cada residuo se agrega al comienzo de la cadena binario.

El ciclo termina cuando numero llega a cero.

Finalmente se muestra el número decimal original y su representación
binaria.


============================================================
9. EJERCICIO 8. SERIE DE FIBONACCI
============================================================

Primero solicito la cantidad de términos y valido que sea mayor que cero.

La serie comienza con las variables:

a = 0
b = 1

Utilizo un for que se ejecuta exactamente la cantidad de términos
solicitados.

En cada repetición agrego el valor actual a la serie, lo sumo al
acumulador y verifico si es par o impar.

Después calculo el siguiente término mediante:

siguiente = a + b

Luego actualizo las variables para continuar generando la serie.

Al final muestro:

- La serie completa.
- La suma de sus términos.
- La cantidad de términos pares.
- La cantidad de términos impares.


============================================================
10. EJERCICIO 9. TABLAS DE MULTIPLICAR
============================================================

Este ejercicio utiliza dos ciclos for anidados.

El primer for recorre los números del 1 al 10 y determina cuál tabla se
está generando.

El segundo for también recorre del 1 al 10 y realiza cada multiplicación.

El resultado se obtiene mediante:

resultado = i * j

Después se verifica si el resultado es par o impar y también si es mayor
que 50.

Para ello utilizo tres contadores:

- pares
- impares
- mayores_50

Al finalizar se muestran las estadísticas generales.


============================================================
11. EJERCICIO 10. PATRÓN NUMÉRICO
============================================================

Primero solicito un número entre 3 y 10.

El while mantiene la solicitud activa mientras el número se encuentre
fuera de ese rango.

Para crear el patrón utilizo ciclos for anidados.

La primera parte genera las líneas de manera creciente desde 1 hasta n.

La segunda parte comienza desde n - 1 y disminuye hasta 1.

En cada línea existe otro for encargado de agregar los números desde 1
hasta el valor correspondiente a esa fila.

Así se obtiene primero el crecimiento del patrón y después su reducción.


============================================================
12. EJERCICIO 11. JUEGO DE ADIVINANZA
============================================================

En este ejercicio se importa random para generar un número secreto.

Primero se muestra un menú de dificultad:

1. Fácil.
2. Intermedio.
3. Difícil.

Según la dificultad seleccionada se establece el límite del número
secreto y la cantidad de intentos disponibles.

El número se genera utilizando random.randint().

El juego se mantiene activo con un while mientras queden intentos y el
número todavía no haya sido adivinado.

Después de cada intento se disminuye intentos_restantes.

Con if, elif y else se determina si:

- El número es correcto.
- El número secreto es mayor.
- El número secreto es menor.

Si el usuario acierta se calcula el puntaje multiplicando los intentos
restantes por 20.

Si se terminan los intentos sin acertar, se muestra el número secreto.


============================================================
13. EJERCICIO 12. CONTROL DE ACCESO
============================================================

El sistema comienza con un usuario y una contraseña definidos.

El usuario dispone de máximo tres intentos para iniciar sesión.

Utilizo un while que se ejecuta mientras existan intentos y el acceso no
haya sido concedido.

Con condicionales verifico si:

- Usuario y contraseña son correctos.
- Ambos son incorrectos.
- Solamente el usuario es incorrecto.
- Solamente la contraseña es incorrecta.

Cuando una autenticación falla se disminuye el número de intentos.

Si se agotan los tres intentos, el sistema informa que ha sido bloqueado.

Si el acceso es correcto se muestra otro menú con las opciones:

1. Consultar información.
2. Cambiar contraseña.
3. Cerrar sesión.

Para cambiar la contraseña primero se solicita la contraseña actual y se
comprueba que sea correcta antes de permitir el cambio.


============================================================
14. RETO INTEGRADOR. SISTEMA DE VENTAS
============================================================

El reto integrador reúne los conceptos utilizados durante todo el taller.

El programa utiliza un menú principal que se repite con while hasta que
el usuario selecciona salir.

Las opciones permiten:

1. Registrar una venta.
2. Consultar el resumen de ventas.
3. Consultar la venta mayor y menor.
4. Aplicar el cierre de caja.
5. Salir.

Para registrar una venta se solicita el nombre del cliente, la cantidad
de productos, el precio de cada producto y el medio de pago.

La cantidad de productos y los precios se validan para que sean mayores
que cero.

Un ciclo for permite solicitar el precio de cada producto y acumular el
subtotal de la venta.

Después se valida el medio de pago.

Las reglas se aplican mediante condicionales:

- Si la compra supera $500.000, se aplica 10 % de descuento.
- Si se paga en efectivo y la compra supera $200.000, se agrega un
  descuento de 3 %.
- Si se paga con tarjeta, se agrega un recargo de 2 %.
- La transferencia no genera recargo.

El total final se calcula de la siguiente manera:

subtotal - descuentos + recargos

Después de cada venta se actualizan los acumuladores generales:

- cantidad_ventas
- total_bruto
- total_descuentos
- total_recargos
- total_recibido

También se utilizan contadores para saber cuántos pagos fueron realizados
en efectivo, tarjeta y transferencia.

La variable clientes_descuento cuenta cuántos clientes recibieron algún
descuento.

Las variables venta_mayor y venta_menor permiten conservar los valores
de la venta más alta y más baja, junto con los nombres de sus clientes.

Antes de consultar estadísticas se verifica que exista por lo menos una
venta registrada.

En el cierre de caja se muestran todas las estadísticas finales.

La variable caja_cerrada funciona como una bandera. Cuando cambia a True,
el sistema ya no permite registrar nuevas ventas.


============================================================
15. CONCEPTOS QUE DEBO PODER EXPLICAR
============================================================

CONDICIONAL:
Permite tomar una decisión dependiendo de si una condición es verdadera
o falsa.

CONTADOR:
Variable que aumenta normalmente de uno en uno para contar ocurrencias.

Ejemplo:
cantidad_ventas = cantidad_ventas + 1

ACUMULADOR:
Variable que guarda una suma progresiva.

Ejemplo:
total_bruto = total_bruto + subtotal_venta

CICLO ANIDADO:
Es un ciclo que se encuentra dentro de otro ciclo.

OPERADOR MÓDULO (%):
Devuelve el residuo de una división. Se utiliza, por ejemplo, para saber
si un número es par o si un valor divide exactamente a otro.

DIVISIÓN ENTERA (//):
Realiza una división y conserva solamente la parte entera del resultado.

BANDERA:
Variable que representa un estado mediante valores como True o False.

Ejemplos del taller:
datos_validos
acceso_concedido
adivinado
caja_cerrada


============================================================
16. POSIBLES PREGUNTAS DE LA SUSTENTACIÓN
============================================================

Pregunta:
¿Por qué utilizó while en los menús?

Respuesta:
Porque el menú debe seguir apareciendo mientras el usuario no seleccione
la opción de salir. No conozco de antemano cuántas veces utilizará el
menú.

Pregunta:
¿Por qué utilizó for para registrar estudiantes o productos?

Respuesta:
Porque en esos casos conozco la cantidad de repeticiones. Si se ingresan
cinco estudiantes, el proceso debe repetirse cinco veces.

Pregunta:
¿Cuál es la diferencia entre for y while?

Respuesta:
For se utiliza principalmente cuando conozco cuántas repeticiones
necesito. While se utiliza cuando la repetición depende de que una
condición continúe siendo verdadera.

Pregunta:
¿Para qué sirve if?

Respuesta:
Sirve para tomar decisiones. Evalúa una condición y permite ejecutar un
bloque diferente dependiendo del resultado.

Pregunta:
¿Qué diferencia existe entre = y ==?

Respuesta:
Un solo signo igual se utiliza para asignar un valor a una variable.
Doble igual se utiliza para comparar dos valores.

Pregunta:
¿Qué hace el operador %?

Respuesta:
Obtiene el residuo de una división. En el taller lo utilizo para
determinar números pares y para encontrar divisores.

Pregunta:
¿Qué hace range(1, cantidad + 1)?

Respuesta:
Genera valores comenzando en 1. Como el límite final de range no se
incluye, se suma 1 para poder llegar hasta la cantidad indicada.

Pregunta:
¿Qué es un acumulador?

Respuesta:
Es una variable que va guardando la suma de varios valores a medida que
se ejecuta el programa.

Pregunta:
¿Qué es un contador?

Respuesta:
Es una variable que registra cuántas veces ocurre una situación.

Pregunta:
¿Por qué utiliza None para venta_mayor y venta_menor?

Respuesta:
Porque antes de registrar la primera venta todavía no existe un valor
válido para comparar. La primera venta permite inicializar esos datos.

Pregunta:
¿Para qué sirve caja_cerrada?

Respuesta:
Es una bandera que controla el estado de la caja. Empieza en False y
después del cierre cambia a True, evitando que se registren nuevas ventas.

Pregunta:
¿Cómo obtiene el total final de una venta?

Respuesta:
Primero se calcula el subtotal. Después se restan los descuentos y se
suman los recargos.

Pregunta:
¿Por qué no se pueden consultar estadísticas si no existen ventas?

Respuesta:
Porque todavía no existen datos sobre los cuales calcular promedios,
totales, venta mayor o venta menor.

Pregunta:
¿Qué ejercicio utiliza ciclos anidados?

Respuesta:
Entre otros, el ejercicio 2 utiliza un for para estudiantes y otro para
las tres notas. El ejercicio 9 utiliza un for para las tablas y otro para
los multiplicadores. El ejercicio 10 también utiliza for anidados para
construir cada línea del patrón.


============================================================
17. CIERRE DE LA SUSTENTACIÓN
============================================================

Con este taller se aplicaron las estructuras if, for y while en diferentes
situaciones.

If permitió tomar decisiones y aplicar reglas.

For permitió recorrer cantidades conocidas y realizar ciclos anidados.

While permitió validar entradas y mantener activos los menús mientras se
cumplían determinadas condiciones.

También se utilizaron contadores y acumuladores para obtener estadísticas
y se integraron todos esos conceptos en el sistema de ventas del reto
final.
"""
