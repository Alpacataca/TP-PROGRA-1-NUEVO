

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

def alta_proveedor():
    try:     # uso de excepciones
        proveedor = {}         # creo el diccionario

            #ingreso de datos del proveedor con sus respectivas validaciones

        CUIT = input("Ingrese CUIT del proveedor: ")
        #ingreso de cuit con sus respectivas validaciones
        while (CUIT.isnumeric() and len(CUIT) == 11)== False:

            print("CUIT inválido. Debe contener exactamente 11 dígitos numéricos.")

            CUIT = input("Ingrese CUIT del proveedor: ")
            
        else:
            ("Guardado correcto del CUIT")


        #Ingreso de nombre del proveedor con sus respectivas validaciones
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")

        while (nombre_proveedor.isalpha())==False:

            print("El nombre debe contener solo letras. Inténtelo nuevamente.")
            nombre_proveedor = input("Ingrese el nombre del proveedor: ")

        else:
            ("Guardado correto del CUIT")
        
        #Ingreso del apellido del proveedor con sus respectivas validaciones
        apellido_proveedor = input("Ingrese el apellido del proveedor: ")

        while (apellido_proveedor.isalpha())==False:

            print("El apellido debe contener solo letras. Inténtelo nuevamente.")
            apellido_proveedor = input("Ingrese el apellido  del proveedor: ")

        else:
            ("Guardado correto del CUIT")


        proveedor["Nombre"] = nombre_proveedor             # se guarda cada llave con su

        proveedor["Apellido"] = apellido_proveedor

        proveedor["CUIT"] = CUIT

        proveedor["Activo"] = "1"

        arch = open('proveedor.txt', 'a')     # abro el archivo en append para el agregado de registros
        for key, value in proveedor.items():  #items aparece en la ppt
            arch.write(f"{key}: {value}"+";")    # uso de f string
        arch.write("\n")
        arch.close()
        #se escriben los datos del proveedor mediante el diccionario proveedor, donde se almacenan la info como key y los datos como value
        print("Proveedor agregado correctamente en el archivo proveedor.txt")

    except FileNotFoundError:
        print("Error al escribir en el archivo.")

def baja_proveedor():
    print("Baja proveedor")
    archivo = open("proveedor.txt", "r+")
    cuit_buscado=input("Ingrese el CUIT: ")
    cuit_buscado=cuit_buscado.rjust(11,'0')

    posant=0 # Guardo la posicion del puntero del archivo al inicio (posant=0)
    linea=archivo.readline()
    encontrado=False   
    while linea and not encontrado: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        nombre_prov, apellido_prov, CUIT, activo = linea.strip().split(";")
        if (cuit_buscado==CUIT and activo=="1"):        
            encontrado=True
            nueva_linea=f"{nombre_prov};{apellido_prov};{CUIT};0\n" # Dejamos todo como estaba, menos el estado que queda en 0
        else:
            posant=archivo.tell() # Guardo la posicion del puntero por si el siguiente registro es el que quiero modificar
            linea=archivo.readline() # Leo la siguiente linea (registro). El puntero del archivo se mueve a la línea siguiente.      
    if encontrado: # Si encontré el registro a modificar
        
        archivo.seek(posant) # Me posiciono en el registro (linea) a borrar .
        # Borrado Logico
        archivo.write(nueva_linea) # Sobreescribo el registro con estado=0. 
        print("Registro borrado exitosamente")
    else:
        print("CUIT no encontrado o dado de baja")
    archivo.close() # Cierro el archivo
    
    input("Presione una tecla para continuar")


def modificar_proveedor():
    ("Modificacion de nombre o apellido del proveedor")

    # Código para modificar el nombre de un proveedor en el archivo SOLO EL NOMBRE
    

def listar_proveedores():
    try:
        with open('proveedor.txt', 'r') as archivo:
            lista_proveedores = []  # Lista para almacenar los proveedores

            for linea in archivo:  # Itera sobre cada línea del archivo
                datos = linea.strip().split(";")
                proveedor_info = {}

                for dato in datos:
                    if ":" in dato:  # Verifica el formato clave: valor
                        clave, valor = dato.split(": ", 1)
                        proveedor_info[clave] = valor
                    else:
                        print(f"Formato incorrecto en la línea: {dato}. Se omitirá.")

                if proveedor_info:  # Agrega a la lista solo si hay información válida
                    lista_proveedores.append(proveedor_info)

            # Ordena la lista de proveedores por CUIT de menor a mayor sin usar get()
            lista_proveedores.sort(key=lambda x: int(x["CUIT"]))

            # Muestra la lista ordenada
            print("Listado de proveedores ordenados por CUIT de menor a mayor:")
            for proveedor in lista_proveedores:
                print(proveedor)

    except FileNotFoundError:
        print("El archivo de proveedores no existe.")


def carga_compras():
    # Código para cargar compras de un proveedor en el archivo # LA CARGA SE FINALIZA COMO -1 Y SE ESCRIBE EN PROVEEDORES.CSV AL LADO DE LA INFO DEL PROVEEDOR
    pass

def listar_montos_compras():
    # Código para listar montos de compras por proveedor ordenados por CUIT desde el archivo 
    pass

def editar_montos_compras():
    # Código para editar montos de compras por proveedor en el archivo VER CONSIGNA PARA ENTENDER MEJOR
    pass

def proveedores_mayor_suma():
    # Código para listar proveedores con mayor suma de compras desde el archivo SE IMPRIMEN TODOS AQUELLOS QUE TENGAN EL MONTO MAXIMO
    pass

if __name__ == "__main__":
    main()




