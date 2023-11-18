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