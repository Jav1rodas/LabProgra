#José Javier Rodas Salazar- 1018723
#Introducción a la Programación 

print("Ejercicio 1")
def calcular_factorial(numero):
    if numero == 0:
        return 1
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


def generar_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence

while True:
    
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        
        numero = int(input("Ingrese un número para calcular su factorial: "))
        factorial = calcular_factorial(numero)
        print(f"{numero} = {numero} * ... * 2 * 1")
        print(f"{numero}! = {factorial}")
    elif opcion == '2':
        numero = int(input("Ingrese un número para generar la secuencia de Fibonacci: "))
        fibonacci_sequence = generar_fibonacci(numero)
        print(", ".join(map(str, fibonacci_sequence)))
    elif opcion == '3':
        print("¡Bye, bye :)!")
        break
    else:
    
        print("La opción ingresada no es válida. Por favor, seleccione una opción válida")
