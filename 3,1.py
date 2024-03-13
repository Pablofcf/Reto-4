3,1
#Dado un carácter, construya un programa en Python para determinar si el carácter es un dígito o no.

a = (int(input("Digite un caracter entre el rango de 40 a 60")))
if a >= 48 and a <= 57:
    print("El caracter es un digito y corresponde al numero: "+(chr(a)))
else:
    print("El caracter no es un digito")