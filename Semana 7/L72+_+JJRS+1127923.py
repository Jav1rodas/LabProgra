#José Javier Rodas Salazar#
#1127923#

print("Ejercicio 2")


print("La suma es el numero 1")
print("La resta es el numero 2")
print("La multipicación es el numero 3")
print("La división es el numero 4")
print("El modulo es el numero 5")
print("La exponenciación es el numero 6")
print("El cociente es el numero 7")

codigo = True
while codigo:

    operacion= input("ingrese el numero de la operación")
    num1 = input("Ingrese el primer numero")
    num2 = input("Ingrese el segundo numero")

    xnum1 = int(num1)
    xnum2 = int(num2)
    xoperacion = int(operacion)

    suma = xnum1 + xnum2
    resta =xnum1 - xnum2
    mult = xnum1 * xnum2
    div = xnum1 / xnum2
    mod = xnum1 % xnum2
    exp = xnum1 ** xnum2
    coci = xnum1 // xnum2

    print("Seleccione un valor para operar")

    if xoperacion == 1:
            print(num1+"+"+num2+"="+str(suma))
            print("Seleccione un valor para operar")
    elif xoperacion == 2:
            print(num1+"-"+num2+"="+str(resta))
            print("Seleccione un valor para operar")

    elif  xoperacion == 3:
            print(num1+"*"+num2+"="+str(mult))
            print("Seleccione un valor para operar")

    elif  xoperacion == 4:
            print(num1+"/"+num2+"="+str(div))
            print("Seleccione un valor para operar")

    elif xoperacion == 5:
            print(num1+"%"+num2+"="+str(mod))
            print("Seleccione un valor para operar")

    elif  xoperacion == 6:
            print(num1+"**"+num2+"="+str(exp))
            print("Seleccione un valor para operar")

    elif xoperacion == 7:
            print(num1+"//"+num2+"="+str(coci))
            print("Seleccione un valor para operar")
    elif xoperacion == '8':
        print("¡Hasta luego!")
        CODIGO = False 
    else: 
            print("Valor no válido")

