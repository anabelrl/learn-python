"""
longitud_cadena.py
Última modicicación: Agosto 2019
Definir una función que calcule la longitud de una lista o una cadena dada.
 (Es cierto que python tiene la función len() incorporada,
 pero escribirla por nosotros mismos resulta un muy buen ejercicio.
 Belba
"""

def longitud_cadena(cadena):
    contar = 0
    for elemento in cadena:
        contar += 1
    return contar

if __name__ == "__main__":
    cadena = input("Introducir cadena: ")
    print(longitud_cadena(cadena))
