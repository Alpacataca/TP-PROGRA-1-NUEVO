def baja_proveedor():
    print("Baja proveedor")
    archivo = open("proveedor.txt", "r+")
    cuit_buscado=input("Ingrese el CUIT: ")
    cuit_buscado=cuit_buscado.rjust(11,'0')
    posant= 0 # Guardo la posicion del puntero del archivo al inicio (posant=0)
    linea=archivo.readline()
    encontrado = False   
    while linea and not encontrado: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        nombre_prov, apellido_prov, CUIT, activo = linea.strip().split(";")
        if (cuit_buscado == CUIT and activo== "1"):        
            encontrado = True
            nueva_linea=f"{nombre_prov};{apellido_prov};{CUIT};0\n" # Dejamos todo como estaba, menos el estado que queda en 0
        else:
            posant = archivo.tell() # Guardo la posicion del puntero por si el siguiente registro es el que quiero modificar
            linea = archivo.readline() # Leo la siguiente linea (registro). El puntero del archivo se mueve a la línea siguiente.      
    if encontrado: # Si encontré el registro a modificar
        
        archivo.seek(posant) # Me posiciono en el registro (linea) a borrar .
        # Borrado Logico
        archivo.write(nueva_linea) # Sobreescribo el registro con estado=0. 
        print("Registro borrado exitosamente")
    else:
        print("CUIT no encontrado o dado de baja")
    archivo.close() # Cierro el archivo
    
    input("Presione una tecla para continuar")
