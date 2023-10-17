#Laboratorio introducción a la programación 
#Intergantes: José Javier Rodas Salazar y Hector sebastian Garrido
#Fecha 16/10/2023

print("Proyecto 1")

print("Linea 1")

#Almacerar los datos de la linea de produccion en una funcion 
def linea1():
    #Solicitar los datos requeridos para la elaboracion del programa
    Cantidadm21=float(input("Ingrese la cantidad de metros cuadrados vendidos al mes:"))
    Preciom21=float(input("Ingrese precio de venta por metro cuadrado:"))
    Costo_metro_cuadrado1=Cantidadm21*Preciom21
#Mostrar los datos iniciales de la linea de priduccion
    print("Metros vendidos en linea 1"+":"+str(Cantidadm21)+"m^2") #Convertir las variables inicialmente en enteras a strings
    print("Precio de venta por m^2"+":"+str(Preciom21)+"Q")
    print("Costo po m^2:"+str(Costo_metro_cuadrado1)+"Q")
    
    condicion=True
    NoEmpleados1 = int(input("Ingrese la cantidad de empleados para la linea (maximo 20) "))
    print("Empleados en linea 1"+":"+str(NoEmpleados1)) 
    if NoEmpleados1 <= 20:
        contador1 = 0 #Se crea la variable para llevar el contador de empleados ingresados
        Costo_Total1 = 0 # Se crea una variable para almacenar las operaciones del costo total
        string_Costo1 ="" # Se crea una variable tipo string para almcenar los datos individuales de cada empleado y mostrarlos de la forma solicitada
        while contador1 <NoEmpleados1: #Se crea una condicion que se cumpla mientras se ingrese una cantidad de empleados que cumplan la condicion y se cuenten
            EmpleadoNo1=input("Ingrese el numero de empleado:") 
            Costo_por_hora1=input("Ingrese el costo de hora por empleado:") #Almacenar los datos por empleados dentro del ciclo
            Horas_trabajadas1=input("Ingrese la cantidad de horas trabajadas por empleado:")
            Costo_por_empleado1=(float(Costo_por_hora1)*float(Horas_trabajadas1)) #Calcular el costo individual de cada empleado ingreado
            Costo_Total1 =Costo_Total1 + Costo_por_empleado1 # Se crea la variable para el costo total, que al sumar el costo de empleado lo actualiza
            string_Costo1 = string_Costo1 + "("+str(Horas_trabajadas1)+"*"+str(Costo_por_hora1)+")" #La variable del string costo se irá actualizando por cada ciclo y se mostrará los valores hora y costo por hora en tipo string
            if NoEmpleados1 < 21: #Crear un ciclo para cumplir el maximo de empleados para poder ingresar y si se sumple, mostrar lo requerido
                print("Empleado número:"+EmpleadoNo1)
                print("Horas trabajadas por el empleado:"+Horas_trabajadas1 +"h")
                print("El empleado cobra por hora:"+Costo_por_hora1 +"Q")
                print("El costo de el empleado es de:" +str(Costo_por_empleado1)+"Q")

                contador1 += 1 #Se incrementa el contador de empleados despues de ingresar uno y lo actualiza
        
    else: 
         print("El numero de empleados maximo es 20, ingrese un numero igual o menor.") #En caso de no cumplirse la sentencia if
    condicion = False

    Ganancia_Total1=Cantidadm21*Preciom21 # Se calcula la ganacia total 
    print("La ganancia total es:"+str(Ganancia_Total1)+"Q")
 
    print("El costo total es:"+str(string_Costo1) + "Q" + "="+str(Costo_Total1)+"Q") 

    Ganancia_Neta1 = Ganancia_Total1 - Costo_Total1 #Se calcula la ganancia neta
    print("La ganancia neta es:"+str(Ganancia_Total1)+"Q"+"-"+str(Costo_Total1)+"Q"+"="+str(Ganancia_Neta1)+"Q")

    Indice_Eficiencia1 = Ganancia_Neta1 / NoEmpleados1 #Se calcula el indice de eficiencia
    print("El idice de eficiendia sería:"+str(Ganancia_Neta1)+"/"+str(NoEmpleados1)+"="+str(Indice_Eficiencia1))
#Llamar a la funcion para ejecutar el programa
linea1()

print("Linea 2")

def linea2():
    #Solicitar los datos requeridos para la elaboracion del programa
    Cantidadm22=float(input("Ingrese la cantidad de metros cuadrados vendidos al mes:"))
    Preciom22=float(input("Ingrese precio de venta por metro cuadrado:"))
    Costo_metro_cuadrado2=Cantidadm22*Preciom22
#Mostrar los datos iniciales de la linea de priduccion
    print("Metros vendidos en linea 2"+":"+str(Cantidadm22)+"m^2") #Convertir las variables inicialmente en enteras a strings
    print("Precio de venta por m^2"+":"+str(Preciom22)+"Q")
    print("Costo po m^2:"+str(Costo_metro_cuadrado2)+"Q")
    
    condicion=True
    NoEmpleados2 = int(input("Ingrese la cantidad de empleados para la linea (maximo 20) "))
    print("Empleados en linea 2"+":"+str(NoEmpleados2)) 
    if NoEmpleados2 <= 20:
        contador2 = 0 #Se crea la variable para llevar el contador de empleados ingresados
        Costo_Total2 = 0 # Se crea una variable para almacenar las operaciones del costo total
        string_Costo2 ="" # Se crea una variable tipo string para almcenar los datos individuales de cada empleado y mostrarlos de la forma solicitada
        while contador2 <NoEmpleados2: #Se crea una condicion que se cumpla mientras se ingrese una cantidad de empleados que cumplan la condicion y se cuenten
            EmpleadoNo2=input("Ingrese el numero de empleado:") 
            Costo_por_hora2=input("Ingrese el costo de hora por empleado:") #Almacenar los datos por empleados dentro del ciclo
            Horas_trabajadas2=input("Ingrese la cantidad de horas trabajadas por empleado:")
            Costo_por_empleado2=(float(Costo_por_hora2)*float(Horas_trabajadas2)) #Calcular el costo individual de cada empleado ingreado
            Costo_Total2 =Costo_Total2 + Costo_por_empleado2 # Se crea la variable para el costo total, que al sumar el costo de empleado lo actualiza
            string_Costo2 = string_Costo2 + "("+str(Horas_trabajadas2)+"*"+str(Costo_por_hora2)+")" #La variable del string costo se irá actualizando por cada ciclo y se mostrará los valores hora y costo por hora en tipo string
            if NoEmpleados2 < 21: #Crear un ciclo para cumplir el maximo de empleados para poder ingresar y si se sumple, mostrar lo requerido
                print("Empleado número:"+EmpleadoNo2)
                print("Horas trabajadas por el empleado:"+str(Horas_trabajadas2)+"h")
                print("El empleado cobra por hora:"+str(Costo_por_hora2)+"Q")
                print("El costo de el empleado es de:" +str(Costo_por_empleado2)+"Q")

                contador2 += 1 #Se incrementa el contador de empleados despues de ingresar uno y lo actualiza
        
    else: 
         print("El numero de empleados maximo es 20, ingrese un numero igual o menor.") #En caso de no cumplirse la sentencia if
    condicion = False

    Ganancia_Total2=Cantidadm22*Preciom22 # Se calcula la ganacia total 
    print("La ganancia total es:"+str(Ganancia_Total2)+"Q")
 
    print("El costo total es:"+str(string_Costo2)+"Q"+"="+str(Costo_Total2)+"Q") 

    Ganancia_Neta2 = Ganancia_Total2 - Costo_Total2 #Se calcula la ganancia neta
    print("La ganancia neta es:"+str(Ganancia_Total2)+"Q"+"-"+str(Costo_Total2)+"Q"+"="+str(Ganancia_Neta2)+"Q")

    Indice_Eficiencia2 = Ganancia_Neta2 / NoEmpleados2 #Se calcula el indice de eficiencia
    print("El idice de eficiendia sería:"+str(Ganancia_Neta2)+"/"+str(NoEmpleados2)+"="+str(Indice_Eficiencia2))
#Llamar a la funcion para ejecutar el programa
linea2()

def eficiencia():
    Indice_Eficiencia1=float(input("Ingrese el valor de eficiencia de la linea 1:"))#Se ingresa el valor del indice de eficiencia de la linea 1
    Indice_Eficiencia2=float(input("Ingrese el valor de eficiencia de la linea 2:"))#Se ingresa el valor del indice de eficiecia de la linea 2
    if Indice_Eficiencia1>Indice_Eficiencia2:#Se crea una condicional para que so el valor de la linea 1 es mayor que el de la linea 2 muestre que esa es la linea de mayor eficiencia
        print("La linea de meyor eficiencia es la 1")
    else:#De lo contrario se mostrara que la linea 2 es la mas eficiente
        print("La linea de mayor eficiencia es la 2")
#Llamar a ka función para ejecutar el programa
eficiencia()
