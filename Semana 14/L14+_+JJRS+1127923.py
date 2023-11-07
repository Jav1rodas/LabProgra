#Semana 14
#Laboratorio de introducción a la porgramación
#Fecha 7/112023
#José Javier Rodas Salazar

print("Semana 14")

class Automovil:
    def __init__(self) :

        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = True
        self.CambioDolar = 0.0
        self.Descuento = 0.0


    def devolver_modelo(self, unModelo):
        self.modelo = unModelo  
    
    def devolver_precio(self, unPrecio):
        self.precio = unPrecio 
    
    def devolver_marca(self, unaMarca):
        self.marca = unaMarca  
    
    def devolver_disponible(self):
        self.disponible = not self.disponible

    def mostrar_la_disponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No disponible"
    
    def devolver_TipoCambio(self, unTipoCambio):
        self.CambioDolar = unTipoCambio

    def devolver_descuento(self, miDescuento):
        self.Descuento = miDescuento
        self.precio = self.precio - miDescuento

    def MostrarInformacion(self):
        precio_en_dolares = self.precio / self.CambioDolar
        disponibilidad = self.mostrar_la_disponibilidad()
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio de venta: Q{self.precio}, Precio en dólares: ${precio_en_dolares}, {disponibilidad}"

#VALOR = float(input("Ingrese el valor del radio de su circunferencia"))
Auto1 =Automovil()

Auto1.devolver_modelo(2018)
Auto1.devolver_precio(50000.00)
Auto1.devolver_marca("Mazda")
Auto1.devolver_TipoCambio(8)
Auto1.devolver_descuento(0.10)

print(Auto1.MostrarInformacion())