"""
es_palindromo.py
Última modicicación: Agosto 2019
Definir una función es_palindromo() que reconoce palíndromos 
ejemplo: es_palindromo ("radar") tendría que devolver True.
 Belba
"""

import reversar

def es_palindromo(cadena):
    if len(cadena) > 0:
        cadena_inversa = reversar.inversa(cadena)
        return cadena == cadena_inversa
    else: 
        return "cadena vacia"

if __name__ == "__main__":
    print("\n una función es_palindromo() que reconoce palíndromos \n")
    cadena = input(" Escribir cadena: ")
    print (es_palindromo(cadena))