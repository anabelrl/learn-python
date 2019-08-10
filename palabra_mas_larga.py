'''
palabra_mas_larga.py
Última modificación: agosto 2019
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 
Anabel Rincon
'''
def mas_larga(cadena):
    mas_larga = ""
    longitud = 0
    for elemento in cadena:
        if len(elemento) > longitud:
            mas_larga = elemento
            longitud = len(elemento)
    return mas_larga

if __name__ == "__main__":
     cadena = ["arroz", "amor", "fernando", "aaa"]
     print(mas_larga(cadena))
