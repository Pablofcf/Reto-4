#Dado un número entero, determinar si ese número corresponde al código ASCII de una vocal minúscula.

a = int(input("Digite un numero entero"))
if a > 97 and a < 122:
    print("El numero entero corresponde a una vocal minuscula en el codigo ASCII, es:"+(chr(a)))
else:
    print("No corresponde a una vocal minuscula en el codigo ASCII")