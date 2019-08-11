''''
mayusculas_cadena.py
Agosto 2019
Escribir un programa que le diga al usuario que ingrese una cadena. 
El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
Anabel Rincon
'''

def mayusculas_cadena(cadena):
    count_uppercases = 0
    for elemento in cadena:
        if elemento.isupper():
            count_uppercases +=1
    return count_uppercases
