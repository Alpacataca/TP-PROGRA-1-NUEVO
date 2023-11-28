
#anda
def ingresodatos(): 
        CUIT=input("Ingrese el CUIT: ")
        while not CUIT.isnumeric() or len(CUIT) == 11:

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

        isactive = str(1)
        
        return CUIT, nombre_proveedor, apellido_proveedor, isactive

#anda
def alta_proveedor():       

        print("Ingreso de proveedores")

        CUIT, nombre, apellido, isactive = ingresodatos()

        archivo = open("proveedor.txt", "a+t") 

        archivo.seek(0)  #pongo el puntero al comienzo del archivo ya que como abro con append esta al final

        linea=archivo.readline()         # empiezo a leer las lineas

        encontrado = False

        while linea and not encontrado:          
            if len(linea.split(";")) >= 4:
                v_CUIT = linea.strip().split(";")[0]  #lees el archivo y si hay algo en la linea, lo asignas a las variables
                activo = linea.strip().split(";")[3]
                #print (CUIT, v_CUIT)
                #print (CUIT == v_CUIT)
                #print (activo)
                #print (type(activo))
                
                if CUIT == v_CUIT and activo == "1":
                    encontrado = True
                    print ("Hola")
                elif (CUIT == v_CUIT) and activo == "0":
                    encontrado = True
                    print ("CUIT dado de baja. ¿Reactivar?: ")
                    if input("Ingrese: (S/N)").upper() == "S":
                        print("MENSAJE DE ERROR Y RESTO DE CODIGO")
                        break
                else:
                    linea = archivo.readline()
            else:
                linea = archivo.readline() #leo la siguiente linea del archivo    

        if not encontrado:
            linea= CUIT + ";" + nombre + ";" + apellido + ";" + isactive + "\n"
            archivo.write(linea) # agrego el proveedor al final del archivo ya que no se lo encontro en el archivo y se llego al final
        else:
            print("CUIT existente, no puede ser duplicado. ")
            
        archivo.close() 

        
        input("Presione una tecla para continuar")

#anda
def baja_proveedor():
    print("Baja de proveedores")

    cuit_buscado = input("Ingrese el CUIT buscado:")
    encontrado = False

    archivo = open("proveedor.txt", "r+")
    posant = 0  # Guarda la posición del puntero del archivo al inicio (posant=0)
    linea = archivo.readline()

    while linea and not encontrado:
        try:
            v_CUIT = linea.strip().split(";")
            if cuit_buscado == v_CUIT[0] and v_CUIT[3] == "1":
                encontrado = True
                v_CUIT[3] = "0"
                
                archivo.seek(posant)  # Mueve el puntero al inicio de la línea a eliminar
                archivo.write(f"{v_CUIT[0].rjust(11)};{v_CUIT[1].rjust(25)};{v_CUIT[2].rjust(25)};{v_CUIT[3]}")  # Vuelve a escribir la línea con el campo modificado
                print(f"El CUIT {v_CUIT[0]} fue dado de baja")
            else:
                posant = archivo.tell()  # Guarda la posición actual
                linea = archivo.readline()
        except ValueError:
            # Si hay un error al hacer split (la línea no tiene el formato esperado),
            # simplemente avanza a la siguiente línea
            posant = archivo.tell()
            linea = archivo.readline()

#anda
def modificar_proveedor():

    print("Modificaciones de proveedores")

    listar_proveedores_ordenados()

    archivo = open("proveedor.txt", "r+t")
    CUIT, nombre, apellido, activo = ingresodatos()
    posant=0 # Guardo la posicion del puntero del archivo al inicio (posant=0)
    linea=archivo.readline()
    encontrado=False   
    while linea and encontrado == False: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        valores_actuales = linea.strip().split(";")
        v_CUIT = valores_actuales[0]
        v_monto = valores_actuales[3:] # Tomamos los montos actuales para volver a escribirlo en la nueva linea  
        if (CUIT==v_CUIT):        
            encontrado=True
            linea_nueva = v_CUIT + ";" + nombre + ";" + apellido + ';' +';'.join(v_monto) #  ponemos el nombre del input, para que se modifique
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
def procesar_proveedores():
    try:
        archivo = open('proveedor.txt', 'r')  # abro el archivo en modo lectura
        linea=archivo.readline()
        
        # hago una lista vacía para almacenar los proveedores
        proveedores = []
        
        # leo línea por línea y almaceno cada proveedor en la lista
        while linea:
            proveedores.append(linea.strip())
            linea=archivo.readline()

        archivo.close()  # Cierro el archivo

        return proveedores 

    except FileNotFoundError:
        print("El archivo proveedor.txt no se encuentra.")

#anda
def carga_compras():
    print("Carga de compras de proveedores")
    
    cuit = input("Ingrese el CUIT del proveedor (o -1 para finalizar): ")
    while cuit != "-1":
        
        monto = input("Ingrese el monto de la compra: ")

        encontrado = False
        
        try:
            archivo = open("proveedor.txt", "r+t")
            linea = archivo.readline()
            posant = 0

            while linea and not encontrado:
                datos = linea.strip().split(";")
                if datos[0] == cuit:
                    encontrado = True
                    datos.append(monto)
                    nueva_linea = ";".join(datos) + "\n"
                else:
                    posant=archivo.tell() #guardo pos del puntero por si el siguiente registro es el que quiero modificar
                linea=archivo.readline() #leo sig linea      
            if encontrado:
                archivo.seek(posant) #me posiciono en el registro a modificar
                archivo.write(nueva_linea) # sobreescribo    
            else:
                print("CUIT inexistente")
        except FileNotFoundError:
            print("El archivo proveedor.txt no se encuentra.")
        finally: 
            archivo.close()
        cuit = input("Ingrese el CUIT del proveedor (o -1 para finalizar): ")
    
    print("Carga de compras finalizada")

#anda
def listar_proveedores_ordenados():


    #proveedores = procesar_proveedores()
    
    archivo = open("proveedor.txt", "r")

    # ordeno la lista de proveedores por CUIT con una funcion lambda y sort la cual va a hacer que splitee cuando haya un ; y agarre los valores de la primer columna
    # carga todo en variable a traves de un generador
    ordenados = sorted((line.strip().split(';') for line in archivo), key=lambda x: x[0]) # sorted dobre strip/split por compresion, key CUIT
    # Muestro los proveedores ordenados en la terminal con el ; reemplazado por espacio

    archivo.close()

    print ("\nProveedores activos:\n")

    encabezados = ["CUIT", "Proveedor", "Apellido"]
    print (f"{encabezados[0].ljust(15)} | {encabezados[1].ljust(30)} | {encabezados[2].ljust(15)}") # f-STRING formateado

    for proveedor in ordenados:
        if proveedor[3].strip() == "1":

            CUIT, nombre, apellido = proveedor[:3]
            print(f"{CUIT.ljust(15)} | {nombre.ljust(30)} | {apellido.ljust(15)}")
     
    print()

#anda
def listar_montos_compras():
    listar_proveedores_ordenados()
    try:
        archivo = open('proveedor.txt', 'r')
        lines = archivo.readline()
        num_CUIT = input("Ingrese CUIT: ")
        while lines:
            campos = lines.strip().split(';')

            if len(campos) >= 4 and campos[0] == num_CUIT:
                cuit = campos[0]
                nombre = campos[1]
                apellido = campos[2]
                compras = campos[4:]

                print (f"\nLista de compras para {cuit}")
                print (f"{'Compras'.ljust(15)} | {'Monto'.rjust(15)}")
                for i in range(len(compras)):
                    n_compra = "Compra " + str(i)
                    print(f"{n_compra.ljust(15)} | {str(float(compras[i])).rjust(15)}")
                
            lines = archivo.readline()

    except FileNotFoundError as error:
        print("El archivo no existe")
    finally:
        try:
            archivo.close()
        except Exception as error:
            pass
    continuar = input("Realizar otra operacion?: ").upper()
    if continuar == "N":    
        exit()
    else: 
        main()

#anda
def modificar_compras():
    print("Modificación de compras de proveedores")
    
    cuit = input("Ingrese el CUIT del proveedor: ")
    
    try:
        archivo = open("proveedor.txt", "r+t")
        linea = archivo.readline()
        posant = 0
        encontrado = False

        while linea and not encontrado:

            datos = linea.strip().rstrip(';').split(";")
            if datos[0] == cuit:
                encontrado = True
                compras = {f"{i}": compra for i, compra in enumerate(datos[4:], start=1)}  #creo el diccionario con los valores
                for key, value in compras.items():
                    print(f"{key}: {value}\n")
                num_compra = input("Ingrese el numero de compra a modificar: ")
                nuevo_monto = input("Ingrese el nuevo monto de la compra: ")
                compras[num_compra] = nuevo_monto       #actualizo el dic con el nuevo monto
                nueva_linea = ";".join(datos[:4] + list(compras.values())) + "\n"      #creo la linea nueva concatenadno los valores del prov con los valores nuevos
            else:
                posant=archivo.tell() #guardo pos del puntero por si el siguiente registro es el que quiero modificar
            linea=archivo.readline() #leo sig linea      
        if encontrado:
            archivo.seek(posant) #me posiciono en el registro a modificar
            archivo.write(nueva_linea) # sobreescribo    
        else:
            print("CUIT inexistente")
    except FileNotFoundError:
        print("El archivo proveedor.txt no se encuentra.")
    finally: 
        archivo.close()
    print("Modificación de compras finalizada, así quedaron los montos:")
    for key, value in compras.items():
        print(f"{key}: {value}\n")

#anda
def proveedores_mayor_suma():
    proveedores = procesar_proveedores()
    max_compras = 0
    for proveedor in proveedores:
        datos = proveedor.split(';')
        compras = datos[3:]
        suma = 0
        try: 
            for monto in compras:
                suma+=float(monto) 
            if suma > max_compras:
                max_compras = suma
                max_proveedores = [{"cuit": datos[0], "monto": suma}]
            elif suma == max_compras:
                max_proveedores.append({"cuit": datos[0], "monto": suma})
        except IndexError: 
            pass #Proveedor no posee compras
    print(max_proveedores)

menu = [
    "1. Alta de Proveedor",
    "2. Baja de Proveedor",
    "3. Modificación de Proveedor",
    "4. Listado de Proveedores ordenado por CUIT",
    "5. Carga de compras de Proveedor",
    "6. Listado de monto de las compras por Proveedor ordenado por CUIT",
    "7. Edición de Monto de las compras",
    "8. Listado de Proveedores con mayor suma de compras registradas",
    "9. Salir del programa"
]

funciones = [
    alta_proveedor,
    baja_proveedor,
    modificar_proveedor,
    listar_proveedores_ordenados,
    carga_compras,
    listar_montos_compras,
    modificar_compras,
    proveedores_mayor_suma,
    exit
]

def main():
    while True:
        print("****** Menú ******")
        for item in menu:
            print(item)

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(funciones):
                funciones[opcion - 1]()
            else:
                print("Opción no válida. Por favor, elija una opción válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

main()
