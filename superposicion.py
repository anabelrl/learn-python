"""
superposicion.py
Última modicicación: Agosto 2019
Definir una función superposicion() que tome dos listas y devuelava los ementos en comun o False 
Escribir la función usando el bucle for anidado.
 Anabel
"""

def superposicion(cadena1,cadena2):
    cadena_iguales = []
    for elemento1 in cadena1:
        for elemento2 in cadena2:
            if elemento1 == elemento2:
                cadena_iguales.append(elemento1)
    
    if len(cadena_iguales) == 0:
        return False
    else:
        return cadena_iguales

if __name__ == "__main__":
    cadena1 = [1,2,3]
    cadena2 = [12,5,6]
    print(superposicion(cadena1,cadena2))