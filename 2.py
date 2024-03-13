#Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.

s = str(input("Cadena de longitud 1 ASCII"))
if (ord(s)% 2 == 0):
    print("Es par")
else: 
    print("Es impar")