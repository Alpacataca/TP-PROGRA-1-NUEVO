## GESTIÓN DE COMPRAS DE PROVEEDORS:

Realizar un programa que Muestre el siguiente menú y realice las operaciones siguientes sobre un archivo txt llamado Proveedors.csv

1.  **Alta de Proveedor** (Se ingresa CUIT, nombre)
2.  **Baja de Proveedor** (Se ingresa CUIT y se realiza eliminación lógica.
3.  **Modificación de Proveedor** (se ingresa CUIT, se muestra el nombre actual, y se permite cambiar el nombre).
4.  **Listado de Proveedores** ordenado por nro. de CUIT.
5.  **Carga de compras de Proveedor**: Se ingresa CUIT y monto de la compra. En caso que el CUIT no haya sido cargado, se debe mostrar la leyenda "CUIT inexistente". La carga finaliza con CUIT igual a -1.  Los montos de las compras se guardan en el mismo archivo Proveedors.csv, a continuación de CUIT y nombre. Es decir, la longitud de la línea es variable, en función a la cantidad de montos de las compras registrados. El monto tiene una longitud máxima de 10 dígitos y dos decimales.
6.  **Listado de monto de las compras inscriptas por cada Proveedor ordenada por CUIT: **Se muestra en pantalla primero el CUIT y el nombre y luego los montos de las compras realizadas poniendo como encabezado el CUIT y el nombre:

CUIT Nombre

Monto de las compras:

Monto de la compra 1

Monto de la compra 2

Monto de la compra 3

1.  **Edición de Monto de las compras: \***El usuario ingresa CUIT.\*
    1.  _El sistema levanta en un diccionario los montos de las compras, donde la clave es el orden del monto de la compra. Es decir, el primer de la compra en el archivo tiene clave=1, el segunda 2, etc..._
    2.  _Los muestra por pantalla._
    3.  _El usuario ingresará clave hasta que clave sea igual a 0, que indicará que dejará de realizar modificaciones. El sistema validará que la clave ingresada exista._
    4.  _El sistema guarda las modificaciones_
2.  **Listados de Proveedores** **con mayor suma de compras registradas** (nro. de CUIT ,  nombre y total ). Se imprimirán todos aquellos que tengan el monto máximo de suma de compras. Para ello armar un diccionario donde la clave sea el CUIT y el valor la suma del monto de las compras.
3.  **Salir del programa**.
