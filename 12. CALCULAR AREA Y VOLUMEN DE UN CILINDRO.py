print("**CALCULAR AREA Y VOLUMEN DE UN CILINDRO**")
print(" ")

#Entradas
d = int(input("Digite el Diametro del Cilindro : "))
h = int(input("DIgite la Altura del Cilindro   : "))
pi = 3.1416

##Proceso
#Formula para calcular el Area de un Cilindro
# Area = 2pi.r(r+h)
# El Radio siempre va a ser la mitad del diametro
r = (d / 2)
Area = ((2 * pi) * r) * (r + h)

print(" ")
#Formula para calcular el Volumen de un Cilindro
##AB x h
#AB = Area de Base
#primero se calcula el Area BAse antes de continuar con la formula
#AB = pi.r^2
ab = pi * (r ** 2)
Volumen = (ab * h)

##Salida
print("El Area del Cilindro es    : ", Area)
print("El Volumen del Cilindro es : ", Volumen)




