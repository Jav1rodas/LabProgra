#José Javier Rodas Salazar#
#1127923#

print("Ejercicio 1: operaciones aritméticas")

num1 = input("Ingrese el primer numero")
num2 = input("Ingrese el segundo numero")

xnum1 = int(num1)
xnum2 = int(num2)

suma = xnum1 + xnum2
resta =xnum1 - xnum2
mult = xnum1 * xnum2
div = xnum1 / xnum2
mod = xnum1 % xnum2
exp = xnum1 ** xnum2
coci = xnum1 // xnum2

print (num1+"+"+num2+"="+str(suma))
print(num1+"-"+num2+"="+str(resta))
print(num1+"*"+num2+"="+str(mult))
print(num1+"/"+num2+"="+str(div))
print(num1+"%"+num2+"="+str(mod))
print(num1+"**"+num2+"="+str(exp))
print(num1+"//"+num2+"="+str(coci))
