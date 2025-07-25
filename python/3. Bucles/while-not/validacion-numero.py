#Escribir un programa que permita el ingreso de un número.
#Si el usuario no ingresa un número entonces.
#Vuelva a solicitar hasta que lo ingrese correctamente.

num = input("Ingrese un número: ") #tres

while not num.isdigit():
    print("Por favor, ingrese un número correctamente: ")
    num = input("Ingrese un número: ") #3
print("Programa Terminado")
#"not" es un condicional que limita el ciclo a si o no.
#num.isdigit() es una función que requiere al usuario ingresar un dígito numeral.
#en conjunto "While not num.isdigit()" le decimos al ciclo que:
#mientras no sea un número el ingresado de como resultado False y vuelva a solicitar
#ingresar un número.