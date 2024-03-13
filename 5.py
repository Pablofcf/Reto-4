#Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.

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
     print("Esta fuera de la circunferencia")