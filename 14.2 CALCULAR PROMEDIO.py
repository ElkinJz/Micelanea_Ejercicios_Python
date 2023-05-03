print("**calcular el promedio de 3 numeros**")
print(" ")

#Entradas
#Use la funciona float para poder digitar numeros con decimales por ejemplo las notas 4.2, 3.5
a = float(input("Digite el Primer Numero  : "))
b = float(input("Digite el Segundo Numero : "))
c = float(input("Digite el Tercer Numero  : "))

#Proceso
prom = (a + b + c) / 3
print(" ")

#Salida
#utilice el condicional if (si) para un ejemplo de de notas (perodio ó ganó) 
if(prom>=3):
    print("El Promedio es: ", prom, "GANÓ")
else:
    print("El Promedio es: ", prom, "PERDIO")
#Salida
#print("El Promedio es: ", prom)
