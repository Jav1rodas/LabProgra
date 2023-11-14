class Tablero:
    def __init__(self):#Se genera el metodo constructor de la clase
        self.tablero = [[' ' for _ in range(10)] for _ in range(10)] #Se crea un atributo en la clase que representa el tablero con las celdas vacías
        self.barcos = {'pequeno': 3, 'grande': 5}#Se crea un atributo en forma de diccionario para almacenar las longitudes de los barcos

    def imprimir_tablero(self): #Metodo
        print("  1 2 3 4 5 6 7 8 9 10") #Imprime la fila de numeros que representan las filas del tablero
        letras = 'ABCDEFGHIJ' # Se almacena una cadena de letras que representa las columnas del tablero
        for i in range(10): #Se analiza las filas del tablero en un ciclo 
            fila = ' '.join(self.tablero[i]) # Se convierte la cadena de letras a una cadena donde los elementos estan separados por espacios 
            print(letras[i] + ' ' + fila, ) #Se imprime la letra de la fila y su representacion en el tablero

    def casilla_en_uso(self, fila, columna, size, orientacion): #Se define el metodo tomando los datos necesarios
        if orientacion == 'h': #Con un ciclo if se verifica la horientzacion
            return any(self.tablero[fila][columna + i] != ' ' for i in range(size)) #Se regresa una verificacion si alguna de las casillas que ocuparia el barco estan  en uso
        elif orientacion == 'v':
            return any(self.tablero[fila + i][columna] != ' ' for i in range(size)) #Si un valor está en uso, toda la cadena se cancela 

    def validar_posicion(self, fila, columna, size, orientacion): 
        if 0 <= fila < 10 and 0 <= columna < 10: # Se verifica que la posicion este dentro del rango del tablero
            if orientacion == 'h' and columna + size <= 10:
                return not self.casilla_en_uso(fila, columna, size, orientacion) #Si no cumple el, rango retorna false
            elif orientacion == 'v' and fila + size <= 10:
                return not self.casilla_en_uso(fila, columna, size, orientacion)
        return False

    def colocar_barco(self, posicion, orientacion, tipo):
        fila = ord(posicion[0]) - ord('A') # Se convierte la letra a un numero y se resta para obtener la posicion final en el tablero
        columna = int(posicion[1:]) - 1 # Se crea una variable para almacenar los valores numericos de las columnas 
        size = self.barcos[tipo] # Obtiene la longitd del barco

        if self.validar_posicion(fila, columna, size, orientacion): #Se verifica la posicion y orientacion llamandoal metodo
            if orientacion == 'h': 
                for i in range(size):
                    self.tablero[fila][columna + i] = tipo[0] # coloca el barco en una posicion horizontal
            elif orientacion == 'v':
                for i in range(size):
                    self.tablero[fila + i][columna] = tipo[0] # se coloca el barco en una posicion verticañ
            self.imprimir_tablero()
        else:
            print("¡Posición no válida! El barco no puede ser colocado aquí.")

    def disparar(self, fila, columna):
        if self.tablero[fila][columna] in ['p', 'g']: #Si la casilla seleccionada contiene un barco pequeño o grande
            print("¡Has alcanzado un barco!")
            barco = self.tablero[fila][columna] #Se crea una variable para el tipo de barco al que le dio el jugador
            self.tablero[fila][columna] = 'X' # Marca la casilla si contiene un barco
            if self.verificar_hundido(barco):
                print(f"¡Has hundido un barco {barco.upper()}!")
        else:
            print("¡Fallo!")

    def verificar_hundido(self, barco):
        for i in range(10): #si en el rango del tablero, filas y columnas
            for j in range(10):
                if self.tablero[i][j] == barco and barco in ['p', 'g'] and 'X' not in self.tablero[i]: # Se verifica si la casilla actual contiene un barco pequeño o grande y si está marcado o no
                    return False
        return True

class JuegoBatallaNaval: #Se crea una clase para almacenar los dsatos
    def __init__(self): 
        self.nombre_jugador1 = input("Ingrese el nombre del Jugador 1: ") #Se solicitan los datos del jugador dn una instancia
        self.nombre_jugador2 = input("Ingrese el nombre del Jugador 2: ")

        self.tablero_jugador1 = Tablero() #Se crea una instancia de la clase y se le asigna un atributo
        self.tablero_jugador2 = Tablero()

        self.jugadores = [self.nombre_jugador1, self.nombre_jugador2] # Se almacenan lo nombres en una lista
        self.tableros = [self.tablero_jugador1, self.tablero_jugador2] #Se almacenan los tableros segun sus instancias

        self.iniciar_juego() #Se llama el metodo de inicio

    def iniciar_juego(self):
        for i in range(2): #En un rango de dos jugadores
            for _ in range(3): #Analiza los 3 barcos pequeños
                while True: #Se crea un ciclo infinito hasta que se ingres euna posicion 
                    posicion = input(f"{self.jugadores[i]}, ingresa la posición para un barco pequeño (A1-J10): ") #Solicita al jugador las posiciones d elos barcos 
                    orientacion = input(f"{self.jugadores[i]}, ingresa la orientación para un barco pequeño (v/h): ")#Se solicita la orientación
                    if self.tableros[i].validar_posicion(ord(posicion[0]) - ord('A'), int(posicion[1:]) - 1, 3, orientacion): #Se llama a los metodos para verificar
                        break #Se rompe el bucle infinito
                    else:
                        print("¡Posición no válida! El barco no puede ser colocado aquí.")#Si no es valida
                self.tableros[i].colocar_barco(posicion, orientacion, 'pequeno') #Se coloca el barco en el tablero del jugador i

            for _ in range(2): #Analiza los barcos garndes
                while True:
                    posicion = input(f"{self.jugadores[i]}, ingresa la posición para un barco grande (A1-J10): ")#Solicita al jugador las posiciones d elos barcos
                    orientacion = input(f"{self.jugadores[i]}, ingresa la orientación para un barco grande (v/h): ") #Se solicita la orientación
                    if self.tableros[i].validar_posicion(ord(posicion[0]) - ord('A'), int(posicion[1:]) - 1, 5, orientacion):
                        break
                    else:
                        print("¡Posición no válida! El barco no puede ser colocado aquí.")
                self.tableros[i].colocar_barco(posicion, orientacion, 'grande') #Se coloca el barco en el tablero del jugador i

        turno = 0 #Se crea una variable para almacenar los turnos

        while True: 
            self.tableros[turno].imprimir_tablero()
            posicion = input(f"{self.jugadores[turno]}, ingresa la posición para disparar (A1-J10): ") #Imprime el tablero del jugador que está en su turno
            fila = ord(posicion[0]) - ord('A')#Se convierte la leta en una posicion en la fila del tablero
            columna = int(posicion[1:]) - 1 #Convierte la parte numerica en la piscion
            self.tableros[1 - turno].disparar(fila, columna) #Se realiza un disparo en el tablero del otro jugador

            if all(' ' not in fila for fila in self.tableros[1 - turno].tablero):#Verifica si las filas del oponente no tienen espaciosen blanco para determinar el ganador
                print(f"{self.jugadores[turno]} ha ganado. ¡Felicidades!")
                break #Sale del bicle infinito

            turno = 1 - turno  # Alternar turnos entre Jugador 1 y Jugador 2


if __name__ == "__main__":
   JuegoBatallaNaval() #Se llama la clase