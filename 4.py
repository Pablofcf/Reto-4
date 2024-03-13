#Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero. Para cada caso de debe imprimir el texto que se especifica a continuación:

x : float 
x = float(input("Digite un numero"))
if x >= 1:
    print("El numero "+str(x)+" es positivo")
elif x <= -1:
    print("El numero "+str(x)+" es negativo")
else: 
    print("El numero x es el neutro para la suma")