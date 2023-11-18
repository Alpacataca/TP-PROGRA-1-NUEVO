
#anda
def ingresodatos(): 
        CUIT=input("Ingrese el CUIT: ")
        while (CUIT.isnumeric() and len(CUIT) == 11)== False:

            print("CUIT inválido. Debe contener exactamente 11 dígitos numéricos.")

            CUIT = input("Ingrese CUIT del proveedor: ")
                
        else:
            ("Guardado correcto del CUIT")

        nombre_proveedor=input("Ingrese el Nombre: ")
        while (nombre_proveedor.isalpha())==False:

                print("El nombre debe contener solo letras. Inténtelo nuevamente.")
                nombre_proveedor = input("Ingrese el nombre del proveedor: ")

        else:
            ("Guardado correcto del nombre")

        apellido_proveedor=input("Ingrese el apellido: ")
        while (apellido_proveedor.isalpha())==False:

                print("El apellido debe contener solo letras. Inténtelo nuevamente.")
                apellido_proveedor = input("Ingrese el apellido  del proveedor: ")

        else:
            ("Guardado correto del apellido")

        CUIT=CUIT.rjust(11,'0')

        nombre_proveedor=nombre_proveedor.ljust(25,' ')

        apellido_proveedor = apellido_proveedor.ljust(25,' ')
        
        return CUIT,nombre_proveedor,apellido_proveedor
#anda pero ver el tema de repeticion de cuits
def alta_proveedor():       

        print("Ingreso de proveedores")

        CUIT, nombre, apellido = ingresodatos()

        archivo = open("proveedor.txt", "a+t") 

        archivo.seek(0)  #pongo el puntero al comienzo del archivo ya que como abro con append esta al final

        linea=archivo.readline()         # empiezo a leer las lineas

        encontrado = False

        while linea and not encontrado:          
            if len(linea.split(";")) == 4:
                v_CUIT , v_nombre , v_apellido= linea.split(";")  #lees el archivo y si hay algo en la linea, lo asignas a las variables

                if (CUIT == v_CUIT):
                    encontrado = True
                else:
                    linea = archivo.readline()
            else:
                linea = archivo.readline() #leo la siguiente linea del archivo    

        if not encontrado:
            linea= CUIT + ";" + nombre + ";" + apellido +"\n"
            archivo.write(linea) # agrego el proveedor al final del archivo ya que no se lo encontro en el archivo y se llego al final
        else:
            print("CUIT existente, no puede ser duplicado. ")
            
            
        archivo.close() 

        
        input("Presione una tecla para continuar")
#anda pero chequear que se salga el enter y que no quede una linea vacia cuando elimino
def baja_proveedor():
    print("Baja de proveedores")

    cuit_buscado = input("Ingrese el CUIT buscado:")
    cuit_buscado = cuit_buscado.rjust(11, '0')
    encontrado = False

    with open("proveedor.txt", "r+") as archivo:
        posant = 0  # Guarda la posición del puntero del archivo al inicio (posant=0)
        linea = archivo.readline()
        
        while linea:
            try:
                v_CUIT, nombre, apellido = linea.strip().split(";")
                if cuit_buscado == v_CUIT:
                    encontrado = True
                    archivo.seek(posant)  # Mueve el puntero al inicio de la línea a eliminar
                    archivo.write(" " * len(linea))  # Escribe espacios en blanco para "borrar" la línea
                    break  # Sale del bucle al eliminar la línea
                else:
                    posant = archivo.tell()  # Guarda la posición actual
                linea = archivo.readline()
            except ValueError:
                # Si hay un error al hacer split (la línea no tiene el formato esperado),
                # simplemente avanza a la siguiente línea
                posant = archivo.tell()
                linea = archivo.readline()

        if encontrado:
            print("Proveedor dado de baja exitosamente")
        else:
            print("CUIT no encontrado o dado de baja")
#anda
def modificar_proveedor():
    print("Modificaciones de proveedores")
    archivo = open("proveedor.txt", "r+t")
    CUIT, nombre, apellido = ingresodatos()
    posant=0 # Guardo la posicion del puntero del archivo al inicio (posant=0)
    linea=archivo.readline()
    encontrado=False   
    while linea and not encontrado: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        v_CUIT, v_nombre,v_apellido=linea.split(";")   #guardo los datos de la linea en 5 variables
        if (CUIT==v_CUIT):        
            encontrado=True
            linea_nueva = v_CUIT + ";" + nombre + ";" + apellido +"\n" #  ponemos el nombre del input, para que se modifique
        else:
            posant=archivo.tell() #guardo pos del puntero por si el siguiente registro es el que quiero modificar
        linea=archivo.readline() #leo sig linea      
    if encontrado:
            
        archivo.seek(posant) #me posiciono en el registro a modificar
            # Borrado Logico
        archivo.write(linea_nueva) # sobreescribo    
        print("Registro editado exitosamente")
    else:
        print("Legajo no encontrado o dado de baja")
    archivo.close() # Cierro el archivo
        
    input("Presione una tecla para continuar")
#anda
def listar_proveedores():
    try:
        arch = open('proveedor.txt', 'r')  # abro el archivo en modo lectura
        
        # hago una lista vacía para almacenar los proveedores
        proveedores = []
        
        # leo línea por línea y almaceno cada proveedor en la lista
        for linea in arch:
            proveedores.append(linea.strip())
        arch.close()  # Cierro el archivo
        
        # ordeno la lista de proveedores por CUIT con una funcion lambda y sort la cual va a hacer que splitee cuando haya un ; y agarre los valores de la primer columna
        proveedores.sort(key=lambda x: (x.split(';')[0]))  # Ordeno por CUIT
        
        # Muestro los proveedores ordenados en la terminal con el ; reemplazado por espacio
        for proveedor in proveedores:
            datos = proveedor.split(';')
            for dato in datos:
                print(dato.replace(';', ' '), end='\t')  # Reemplazo ; por espacio y separo por tabulación
            print()  # Salto de línea entre cada proveedor

    except FileNotFoundError:
        print("El archivo proveedor.txt no se encuentra.")
#arreglar todo
def carga_compras():
    print("Carga de compras de proveedores")
    
    while True:
        cuit = input("Ingrese el CUIT del proveedor (o -1 para finalizar): ")
        if cuit == '-1':
            break
        
        monto = input("Ingrese el monto de la compra: ")

        monto = f"{float(monto):.2f}".rjust(13, ' ')  # asegura el formato del monto
        
        encontrado = False

        lineas = []
        
        with open("proveedor.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                if datos[0] == cuit:
                    encontrado = True
                    datos.append(monto)
                    linea = ";".join(datos) + "\n"
                lineas.append(linea)
        
        if not encontrado:
            print("CUIT inexistente")
        else:
            with open("proveedor.txt", "w") as archivo:
                archivo.writelines(lineas)
    
    print("Carga de compras finalizada")
#completar
def listar_montos_compras():
    # Código para listar montos de compras por proveedor ordenados por CUIT desde el archivo 
    pass
#completar
def editar_montos_compras():
    # Código para editar montos de compras por proveedor en el archivo VER CONSIGNA PARA ENTENDER MEJOR
    pass
#completar
def proveedores_mayor_suma():
    # Código para listar proveedores con mayor suma de compras desde el archivo SE IMPRIMEN TODOS AQUELLOS QUE TENGAN EL MONTO MAXIMO
    pass



def main():
    while True:
        print("****** Menú ******")
        print("1. Alta de Proveedor")
        print("2. Baja de Proveedor")
        print("3. Modificación de Proveedor")
        print("4. Listado de Proveedores ordenado por CUIT")
        print("5. Carga de compras de Proveedor")
        print("6. Listado de monto de las compras por Proveedor ordenado por CUIT")
        print("7. Edición de Monto de las compras")
        print("8. Listado de Proveedores con mayor suma de compras registradas")
        print("9. Salir del programa")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            alta_proveedor()
        elif opcion == "2":
            baja_proveedor()
        elif opcion == "3":
            modificar_proveedor()
        elif opcion == "4":
            listar_proveedores()
        elif opcion == "5":
            carga_compras()
        elif opcion == "6":
            listar_montos_compras()
        elif opcion == "7":
            editar_montos_compras()
        elif opcion == "8":
            proveedores_mayor_suma()
        elif opcion == "9":
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

            
main()



