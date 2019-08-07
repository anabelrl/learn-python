"""
Escribir una funcion sum() y una función multip() que sumen y 
multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def sumar(cadena):
    suma = 0
    for elemento in cadena:
        suma += elemento
    return suma

def multiplicar(cadena):
    multiplicacion = 1
    for elemento in cadena:
        multiplicacion *= elemento
    return multiplicacion

if __name__ == "__main__":
    cadena = [1, 2, 3, 4]
    #cadena = int(input("Introducir cadena: "))
    print(sumar(cadena))
    print(multiplicar(cadena))
