#Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.

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
   print ("El dato seleccionado " +str(c)+ " es invalido para formar un triangulo")