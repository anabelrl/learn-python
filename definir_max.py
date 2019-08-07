"""
Definir_max.py
Última modicicación: Agosto 2019
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es 
un muy buen ejercicio.
Anabel Rincón
"""

def max_two_num(num1,num2):

    if(num1 >= num2):
        return num1
    elif(num1 < num2):
        return num2


if __name__ == "__main__":

    num1 = int(input("Introducir primer número: "))
    num2 = int(input("Introducir segundo número: "))
    print(max_two_num(num1, num2))

    print(max(num1,num2))
    

    
