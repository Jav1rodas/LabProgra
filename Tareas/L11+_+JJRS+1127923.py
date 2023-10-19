#José Javier Rodas Salazar
#Laboratorio Introduccion a la programacion

print("Semana 11")

Contador_ceros = 0
Contador_unos = 0
Contador_otros = 0
String = str(input("Ingrese una cadena de caracteres")) #Pedir ingresar la cadena de caracteres como un string

for i in range(len(String)): #Se analizara la longitud de la cadena ingresada 
    if String[i] == "0": #por cada elemento de la cadena que se ingrese se verificara cada posicion del string 
        Contador_ceros += 1 #Verificar los ceros

    elif String[i] == "1":
        Contador_unos += 1 #Verificar los unos

    else:
        Contador_otros += 1 #Verificar los demas caracteres

print("Cadena: "+String)
print("Cantidad 0:"+ str(Contador_ceros))
print("Cantidad 1:"+ str(Contador_unos))
print("Otros caracteres:"+str(Contador_otros))