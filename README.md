# Reto4

1. Dado un número entero, determinar si ese número corresponde al código ASCII de una vocal minúscula.
```python
a = int(input("Digite un numero entero"))
if a > 97 and a < 122:
    print("El numero entero corresponde a una vocal minuscula en el codigo ASCII, es:"+(chr(a)))
else:
    print("No corresponde a una vocal minuscula en el codigo ASCII")
```
2. Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.
```python
s = str(input("Cadena de longitud 1 ASCII"))
if (ord(s)% 2 == 0):
    print("Es par")
else: 
    print("Es impar"))
```

3. Dado un carácter, construya un programa en Python para determinar si el carácter es un dígito o no.
```python
s = (str(input("Digite un caracter")))
if s == "0":
    print("Es un digito")
elif s == "1":
    print("Es un digito")
elif s == "2":
    print("Es un digito")
elif s == "3":
    print("Es un digito")
elif s == "4":
    print("Es un digito")
elif s == "5":
    print("Es un digito")
elif s == "6":
    print("Es un digito")
elif s == "7":
    print("Es un digito")
elif s == "8":
    print("Es un digito")
elif s == "9":
    print("Es un digito")
else: 
    print("No es un digito"))
```

3.1. Dado un carácter, construya un programa en Python para determinar si el carácter es un dígito o no.
```python
a = (int(input("Digite un caracter entre el rango de 40 a 60")))
if a >= 48 and a <= 57:
    print("El caracter es un digito y corresponde al numero: "+(chr(a)))
else:
    print("El caracter no es un digito"))
```

4. Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero. Para cada caso de debe imprimir el texto que se especifica a continuación:
```python
x : float 
x = float(input("Digite un numero"))
if x >= 1:
    print("El numero "+str(x)+" es positivo")
elif x <= -1:
    print("El numero "+str(x)+" es negativo")
else: 
    print("El numero x es el neutro para la suma"))
```

5. Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.
```python
radio = float(input("Digite un numero para el radio:"))
y1 = float(input("Digite un numero x1:"))
x1 = float(input("Digite un numero y2:"))

y2 = float(input("Digite un numero y2:"))
x2 = float(input("Digite un numero x2:"))
distancia = float(((x2-x1)**2 +(y2-y1)**2)**(1/2))
if distancia>radio:
  print ("Esta dentro de la circunferencia")
else:
   if distancia==radio:
     print ("Esta sobre la circunferencia")

   else:
     print("Esta fuera de la circunferencia"))
```

6. Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.
```python
a = int(input("Digite un numero"))
b = int(input("Digite un numero"))
c = int(input("Digite un numero"))

if a + b > c and b + c > a and c + a > b:
   print ("El dato seleccionado " +str(a)+ " es valido para formar un triangulo")
   print ("El dato seleccionado " +str(b)+ " es valido para formar un triangulo")
   print ("El dato seleccionado " +str(c)+ " es valido para formar un triangulo")
else:
   print ("El dato seleccionado " +str(a)+ " es invalido para formar un triangulo")
   print ("El dato seleccionado " +str(b)+ " es invalido para formar un triangulo")
   print ("El dato seleccionado " +str(c)+ " es invalido para formar un triangulo"))
```
