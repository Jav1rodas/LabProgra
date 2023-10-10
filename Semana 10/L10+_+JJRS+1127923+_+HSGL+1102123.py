#Jose Javier Rodas Salazar Y Hector sebastian Garrido
#Laboratorio de programacion, semana 10
#10/10/2023

print ("Semana 10")

def operacion():
    num1 =int(input("Ingrese un numero:"))
    hexa =""
    letra= ["A", "B", "C", "D", "E", "F"]
    while num1 > 0:
            
            resultado = (num1 % 16)

            if resultado == 10:
             resultado = letra[0]
            elif resultado == 11:
             resultado = letra[1]
            elif resultado == 12:
             resultado = letra[2]
            elif resultado == 13:
             resultado = letra[3]
            elif resultado == 14:
             resultado = letra[4]
            elif resultado == 15:
             resultado = letra[5]
        
            hexa = str(resultado) + hexa
            num1 = num1//16
            print ("Resultado:"+ hexa)
    
operacion()