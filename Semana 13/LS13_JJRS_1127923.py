#Semana 13
#Laboratorio de introducción a la porgramación
#Fecha 31/10/2023
#José Javier Rodas Salazar

print("Semana 13")

class Circulo:
    def __init__(self, radio) :
        self.radio  = float(radio)

    def devolver_Perimetro (self):
        return (2 * self.radio * 3.14)
    
    def devolver_Area (self):
        return (3.14 * self.radio * self.radio)
    
    def devolver_Volumen (self):
        return (4 * 3.14 * self.radio * self.radio * self.radio) / 3

   

#VALOR = float(input("Ingrese el valor del radio de su circunferencia"))
circulo1 =Circulo(10)
circulo1.devolver_Area()
circulo1.devolver_Perimetro()
circulo1.devolver_Volumen()

print("Perimetro:"+str(circulo1.devolver_Perimetro()))
print("Area:"+str(circulo1.devolver_Area()))
print("Volumen:"+str(circulo1.devolver_Volumen()))