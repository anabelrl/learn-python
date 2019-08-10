"""
reversar.py
Última modicicación: Agosto 2019
Definir una función inversa() que calcule la inversión de una cadena.
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
 Belba
"""

def reversar(cadena):
    indice = len(cadena) - 1
    cadena_reversada = []

    while indice <= 0:
        letra = cadena[indice]
        cadena_reversada.append(letra)
        indice -= 1

    return cadena_reversada    

#if __name__ == "__main__":