CODIGO = True
while CODIGO: 
    print("ejercicio 3 ")
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("ingrese el tercer numero: "))

    print("La numero 1 es a*b+c")
    print("La numero 2 es a*(b+c)")
    print("La numero 3 es a/b+c")
    print("La numero 4 es 3a+2b/c**2")
    print("La numero 5 es salir")

    opcion = input("elija el numero de la ecuacion: ")

    if opcion=="1":
        operacion1= (a*b)+c
        print("resultado de: ", a, "*", b, "+", c, "=", operacion1)
    elif opcion=="2":
        operacion2= a *(b+c)
        print("resultado de: ", a, "*", "(", b, "+", c, ")", "=", operacion2)
    elif opcion=="3":
        operacion3= a/(b+c)
        print("resultado de: ", a, "/", "(", b, "+", c, ")", "=", operacion3)
    elif opcion=="4":
        operacion4= ((3*a)+(2*b))/c**2
        print("resultado de: ""(3 ", a, ")", "+", "(", "2 *", b, ")", "/", c,"* 2", "=", operacion4) 
    elif opcion =="5":
        print("¡hasta luego!")
        CODIGO = False
    else: 
        print("Opción no válida")

    
        
