import os # os es una librería de Python
"""
Este es un ejemplo de ABMC primitivo, faltan  las excepciones,  validaciones, detalles de presentacion, etc... 
Para las bajas, vamos a hacer "Borrado lógico", no borramos fisicamente el registro, sino que agregamos un campo Estado,
que utilizamos como indicador, por ejemplo 0=BORRADO, 1=NO BORRADO.En otras palabras: el borrado lógico es en realidad
una modificación del estado, que pasa de 1=NO BORRADO a 0=BORRADO.

Luego debo acordarme de que el programa no "muestre" los registros cuyo estado sea igual a 0=BORRADO, con lo cual el usuario
no lo verá y para él esta borrado.

El borrado lógico es una práctica habitual en sistemas, porque permite recuperar la informacion que fue borrada accidentalmente.
Cuando hacemos el alta/modificacion, seteamos a borrado con un 1 y cuando lo borramos en 0. El usuario desconoce la existencia
de este campo, que es de uso interno del programa.

Nota: el registro siempre debe tener la misma cantidad de caracteres en este tipo de archivos donde la estructura de los
campos es fija.

En nuestro caso: 4 caracteres para legajo + 25 caracteres para el nombre, + 1 caracter para el estado, que en total suman
30 caracteres, sin contar el fin de línea.



"""
def ingresarDatos():
    legajo=input("Ingrese el Legajo=>")
    nombre=input("Ingrese el Nombre=>")
    legajo=legajo.rjust(4,'0')
    nombre=nombre.ljust(25,' ')
    return legajo,nombre
    



def alta():
    print("Alta")
    legajo,nombre=ingresarDatos()
    archivo = open("Estudiantes.txt", "a+t") # Lo abro como append para que si no está el archivo, lo cree.No lo abro como w
    # porque como write lo sobreescribiría. Y como r no lo abro, porque si el archivo no existe daría error.
    archivo.seek(0) # Como se abrío como append, queda el puntero al final del archivo, por lo que es necesario volverlo al inicio
    linea=archivo.readline()
    encontrado=False
    while linea and not encontrado: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        clegajo, cnombre, estado=linea.split(";")
        if (legajo==clegajo):        
            encontrado=True
        else:
            linea=archivo.readline() # Leo la siguiente linea (registro). El puntero del archivo se mueve a la línea siguiente.      

    if not encontrado:
        linea=legajo+";"+nombre+";"+ "1\n"
        archivo.write(linea) # Dado que se llegó final del archivo, el registro se agrega a continuacion. 
    else:
        print("Legajo existente, no puede ser duplicado. ")
        
        
    archivo.close() # Cierro el archivo

       
    input("Presione una tecla para continuar")

def baja():
    print("Baja")
    archivo = open("Estudiantes.txt", "r+t")
    legajo=input("Ingrese el Legajo=>")
    legajo=legajo.rjust(4,'0')

    posant=0 # Guardo la posicion del puntero del archivo al inicio (posant=0)
    linea=archivo.readline()
    encontrado=False   
    while linea and not encontrado: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        clegajo, cnombre, cestado=linea.split(";")
        cestado=cestado.rstrip('\n')
        if (legajo==clegajo and cestado=="1"):        
            encontrado=True
            lineaC=clegajo+";"+cnombre+";"+"0\n" # Dejamos todo como estaba, menos el estado que queda en 0
        else:
            posant=posant=archivo.tell() # Guardo la posicion del puntero por si el siguiente registro es el que quiero modificar
        linea=archivo.readline() # Leo la siguiente linea (registro). El puntero del archivo se mueve a la línea siguiente.      
    if encontrado: # Si encontré el registro a modificar
        
        archivo.seek(posant) # Me posiciono en el registro (linea) a borrar .
        # Borrado Logico
        archivo.write(lineaC) # Sobreescribo el registro con estado=0. 
        print("Registro borrado exitosamente")
    else:
        print("Legajo no encontrado o dado de baja")
    archivo.close() # Cierro el archivo
    
    input("Presione una tecla para continuar")

def modificaciones():
    print("Modificaciones")
    archivo = open("Estudiantes.txt", "r+t")
    legajo,nombre=ingresarDatos()
    posant=0 # Guardo la posicion del puntero del archivo al inicio (posant=0)
    linea=archivo.readline()
    encontrado=False   
    while linea and not encontrado: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        clegajo, cnombre, cestado=linea.split(";")
        cestado=cestado.rstrip('\n')
        if (legajo==clegajo and cestado=="1"):        
            encontrado=True
            lineaC=clegajo+";"+nombre+";"+"1\n" # Observese que ponemos el nombre del input, para que se modifique
        else:
            posant=posant=archivo.tell() # Guardo la posicion del puntero por si el siguiente registro es el que quiero modificar
        linea=archivo.readline() # Leo la siguiente linea (registro). El puntero del archivo se mueve a la línea siguiente.      
    if encontrado: # Si encontré el registro a modificar
        
        archivo.seek(posant) # Me posiciono en el registro (linea) a modificar.
        # Borrado Logico
        archivo.write(lineaC) # Sobreescribo el registro con la línea modificada (lineaC)        
        print("Registro editado exitosamente")
    else:
        print("Legajo no encontrado o dado de baja")
    archivo.close() # Cierro el archivo
    
    input("Presione una tecla para continuar")

def consultas():
    print("Consultas")
    archivo = open("Estudiantes.txt", "rt")
    linea=archivo.readline()
    print("Legajo ".rjust(7),end="")
    print("Nombre".ljust(25))
    while linea: # Leo hasta fin de archivo (linea vacía) o hasta que lo encuentre
        clegajo, cnombre, cestado=linea.split(";")
        cestado=cestado.rstrip('\n')
        if cestado=="1":
            print("%6s %25s" %(clegajo,cnombre))
        linea=archivo.readline() # Leo la siguiente linea (registro). El puntero del archivo se mueve a la línea siguiente.      
  
    archivo.close() # Cierro el archivo
    
    input("Presione una tecla para continuar")
def Fin():    
    print("Fin")
    
def menu(l):
    os.system ("cls")
    n=len(l)
    for i in range(n):
        print (str(i)+"-"+l[i])
    r=int(input("Ingrese opcion=>"))
    while (r < 0 or r >= n):
        print("Opcion invalida")
        r=int(input("Ingrese opcion=>"))
        
    return r
    
def principal(m,f):
    opcion=menu(m)
    while (opcion):
        print("opcion",opcion)
        f[opcion]()
        #eval(f[opcion])
        opcion=menu(m)
#Programa Principal
        
menues=["Fin","Alta","Baja","Modificaciones","Consulta"]
funciones=[Fin,alta,baja, modificaciones,consultas]

principal(menues,funciones)





