'''
filtrar_palabras.py
Agosto 2019
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, 
y devuelva las palabras que tengan mas de n caracteres. 
Anabel Rincón 
'''

def filtrar_palabras(cadena,n):
    palabras_filtradas =[]
    for elemento in cadena:
        if len(elemento) >= n:
            palabras_filtradas.append(elemento)
    return palabras_filtradas

if __name__ == "__main__":
    cadena = ["arroz", "alo", "fernando", "a"]
    n = 3
    print(filtrar_palabras(cadena,n))