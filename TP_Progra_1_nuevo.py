

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

def alta_proveedor():       #ver el tema de repeticion de cuits

        print("Ingreso de proveedores")

        CUIT, nombre, apellido = ingresodatos()

        archivo = open("proveedor.txt", "a+t") 

        archivo.seek(0) # Como se abrío como append, queda el puntero al final del archivo, por lo que es necesario volverlo al inicio

        linea=archivo.readline()         # empiezo a leer las lineas

        encontrado = False

        while linea and not encontrado:          
            if len(linea.split(";")) == 4:
                v_CUIT , v_nombre , v_apellido , v_activo = linea.split(";")  #lees el archivo y si hay algo en la linea, lo asignas a las variables

                if (CUIT == v_CUIT):
                    encontrado = True
                else:
                    linea = archivo.readline()
            else:
                linea = archivo.readline()# Leo la siguiente linea (registro). El puntero del archivo se mueve a la línea siguiente.      

        if not encontrado:
            linea= CUIT + ";" + nombre + ";" + apellido + ";" +"1\n"
            archivo.write(linea) # Dado que se llegó final del archivo, el registro se agrega a continuacion. 
        else:
            print("CUIT existente, no puede ser duplicado. ")
            
            
        archivo.close() # Cierro el archivo

        
        input("Presione una tecla para continuar")



def baja_proveedor():
    print("Baja de proveedores")

    archivo = open("proveedor.txt", "r+")
    cuit_buscado=input("Ingrese el CUIT buscado:")
    cuit_buscado=cuit_buscado.rjust(11,'0')
    posant= 0 # Guardo la posicion del puntero del archivo al inicio (posant=0)
    linea=archivo.readline()
    encontrado=False   
    while linea and not encontrado: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        CUIT, nombre_prov, apellido_prov, activo = linea.strip().split(";")
        if (cuit_buscado==CUIT and activo=="1"):        
            encontrado=True
            nueva_linea = f"{CUIT};{nombre_prov};{apellido_prov};0\n" # Dejamos todo como estaba, menos el estado que queda en 0
        else:
            posant=archivo.tell() # Guardo la posicion del puntero por si el siguiente registro es el que quiero modificar
            linea=archivo.readline() # Leo la siguiente linea (registro). El puntero del archivo se mueve a la línea siguiente.      
    if encontrado: # Si encontré el registro a modificar
        
        archivo.seek(posant) # Me posiciono en el registro (linea) a borrar .
        # Borrado Logico
        archivo.write(nueva_linea)
        print("Proveedor dado de baja exitosamente")
    else:
        print("CUIT no encontrado o dado de baja")
    archivo.close() 
    
    input("Presione una tecla para continuar")  



def modificar_proveedor():
    print("Modificaciones de proveedores")
    archivo = open("proveedor.txt", "r+t")

    CUIT=input("Ingrese el CUIT a buscar: ")

    while (CUIT.isnumeric() and len(CUIT) == 11)== False:

        print("CUIT inválido. Debe contener exactamente 11 dígitos numéricos.")

        CUIT = input("Ingrese CUIT del proveedor a buscar: ")

    nombre=input("Ingrese el Nombre: ")
    while (nombre.isalpha())==False:

            print("El nombre debe contener solo letras. Inténtelo nuevamente.")
            nombre = input("Ingrese el nombre del proveedor: ")

    posant = 0 # Guardo la posicion del puntero del archivo al inicio (posant=0)
    linea=archivo.readline()
    encontrado=False   
    while linea and not encontrado: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        v_CUIT, v_nombre ,v_apellido, v_activo=linea.split(";")   #guardo los datos de la linea en 5 variables
        v_activo =v_activo.rstrip('\n')
        if (CUIT==v_CUIT and v_activo=="1"):        
            encontrado=True
            linea_nueva = v_CUIT + ";" + nombre + ";" + v_apellido + ";" +"1\n" # Observese que ponemos el nombre del input, para que se modifique
        else:
            posant=archivo.tell() # Guardo la posicion del puntero por si el siguiente registro es el que quiero modificar
        linea=archivo.readline() # Leo la siguiente linea (registro). El puntero del archivo se mueve a la línea siguiente.      
    if encontrado: # Si encontré el registro a modificar
            
        archivo.seek(posant) # Me posiciono en el registro (linea) a modificar.
            # Borrado Logico
        archivo.write(linea_nueva) # Sobreescribo el registro con la línea modificada (lineaC)        
        print("Registro editado exitosamente")
    else:
        print("CUIT no encontrado o dado de baja")
    archivo.close() # Cierro el archivo
        
    input("Presione una tecla para continuar")

    

def listar_proveedores():
    try:
        arch = open('proveedor.txt', 'r')  # Abro el archivo en modo lectura
        
        # Inicializo una lista vacía para almacenar los proveedores
        proveedores = []
        
        # Leo línea por línea y almaceno cada proveedor en la lista
        for linea in arch:
            proveedores.append(linea.strip())
        arch.close()  # Cierro el archivo
        
        # Ordeno la lista de proveedores por CUIT
        proveedores.sort(key=lambda x: int(x.split(';')[0]))  # Ordeno por CUIT
        
        # Muestro los proveedores ordenados en la terminal con el ; reemplazado por espacio
        for proveedor in proveedores:
            datos = proveedor.split(';')
            for dato in datos:
                print(dato.replace(';', ' '), end='\t')  # Reemplazo ; por espacio y separo por tabulación
            print()  # Salto de línea entre cada proveedor

    except FileNotFoundError:
        print("El archivo proveedor.txt no se encuentra.")


#def carga_compras():
    try:
        arch = open('proveedor.txt', 'r+')  # Abro el archivo en modo lectura

        while True:
            cuit = input("Ingrese el CUIT del proveedor (-1 para salir): ")
            if cuit == '-1':
                break

            # Validar el formato de CUIT (ejemplo simple)
            if cuit.isdigit()==False or len(cuit) != 11:
                print("Formato de CUIT incorrecto. Debe tener 11 dígitos.")
                cuit = input("Ingrese el CUIT del proveedor (-1 para salir): ")

            monto_compra = input("Ingrese el monto de la compra: ")
            # Validar el formato del monto (máximo 10 dígitos y dos decimales)

            monto = float(monto_compra)
            while (0 <= monto <= 9999999999.99) == False:
                print("Monto inválido. Debe ser un número entre 0 y 9999999999.99.")
                monto_compra = input("Ingrese el monto de la compra: ")
            
    
            
            csv_writer.writerow([cuit, monto_compra])

    except FileNotFoundError:
        print("El archivo proveedor.txt no se encuentra.")

    print("Carga de compras finalizada.")





def listar_montos_compras():
    # Código para listar montos de compras por proveedor ordenados por CUIT desde el archivo 
    pass

def editar_montos_compras():
    # Código para editar montos de compras por proveedor en el archivo VER CONSIGNA PARA ENTENDER MEJOR
    pass

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
if __name__ == "__main__":
    main()




