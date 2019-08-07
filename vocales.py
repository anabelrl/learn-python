"""
vocales.py
Última modicicación: Agosto 2019
Escribir una función que tome un carácter y devuelva True si es una vocal, 
de lo contrario devuelve False.
Fernando El Pipisote
"""

character = input("Escriba un caracter: ")
length = len(character)
if (length == 1):
    if ( character == "a" 
        or character == "e" 
        or character == "i"
        or character == "o"
        or character == "u"
        or character == "A"
        or character == "E"
        or character == "I"
        or character == "O"
        or character == "U"):
        respond = True 
        print ("Es una vocal: " + str(respond))
        
    else: 
        respond = False
        print ("Es una vocal: " + str(respond))
        
else:
    print ("No se recibió un caracter bye")
