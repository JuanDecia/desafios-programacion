#A una variable string debemos agregarle el valor "aprobado" si la calificación del
#estudiante es mayor o igual a "10", y "Reprobado" en caso contrario.

nota_estudiante = int(input("Ingrese el valor de su nota: "))

if nota_estudiante < 10:
    print("Reprobado")
else:
    print("Aprobado")

#Necesitamos determinar si un número es positivo, negativo o cero.

numero = int(input("Ingrese un número: "))

if numero == 0:
    print("Cero")
elif numero > 0:
    print("Número positivo")
else:
    print("Número negativo")

#Necesitamos leer la edad de un usuario y si es mayor de edad se puede
#autorizar para la compra de criptomonedas.

usuario = int(input("Ingrese su edad en años: "))

if usuario >= 18:
    print("Usted esta habilitado para hacer compras en criptomonedas.")