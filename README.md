#José Javier Rodas Salazar#
#1127923#

codigo = True
while codigo:
    print("Menú:")
    print("Seleccione 1 si desea encontrar el factorial")
    print("Seleccione 2 si desea encontrar la seciuencia de Fribonacci")
    print("Seleccione 3 si desea salir")

    opcion = int(input("Ingrese el numero de operacion"))
    num = int(input("Ingrese un numero para trabajar"))
    
    factorial = 1
    i = 1

    if opcion == 1:
        while i <= num:
            factorial = factorial* i
            i = i + 1

            print(i-1, "=", str(factorial), "*")

    elif opcion ==2:        

        fibonacci = 1
        u = 1

        while   num > 2:
            fibonacci = num-1 + num-2
            u = u +1
            print(str(fibonacci))

    elif opcion ==3:
        print("¡hasta luego!")
        codigo = False
    else: 
        print("Opción no válida")
# LabProgra
