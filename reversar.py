"""
reversar.py
Última modicicación: Agosto 2019
Definir una función inversa() que calcule la inversión de una cadena.
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
 Belba
"""

def inversa(cadena):
    indice = len(cadena) - 1
    cadena_reversada = []

    while indice >= 0:
        letra = cadena[indice]
        cadena_reversada.append(letra)
        indice -= 1

    if len(cadena) == 0: 
        return "Cadena vacía"
  
    return ''.join(cadena_reversada)   

if __name__ == "__main__": 
    print("\n Definir una función inversa() que calcule la inversión de una cadena. \n\
    Por ejemplo la cadena \"estoy probando\" debería devolver la cadena \"odnaborp yotse\" \n")
    cadena = input("introducir cadena a reversar: ")
    print(inversa(cadena))