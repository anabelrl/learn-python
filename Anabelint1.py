import math

a = [2, 0, 1, 4, 3, 5]
longitud = len(a)
#print(longitud)
b = []
bucle = 0
for i in range (longitud):
    in_box = a[i]
    if in_box not in b:
        while in_box not in b: 
            b.append(in_box)
            in_box= a[in_box]
        bucle += 1    
print("Bucles: " + str(bucle))