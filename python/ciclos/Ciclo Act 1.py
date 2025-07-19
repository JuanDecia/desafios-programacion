#escribe un programa en pseudo-código que reciba 5 criptomonedas, cada una con sus respectivas
#cantidades y precios en USD$, luego que imprima el valor que tiene acomulado.

i=0 #Se crea una variable "i" con numero "0" para usar en el ciclo "While".
valor=0.0

while i < 5:
    cripto = input("ingrese el nombre la moneda: ")
    cant = float(input("Ingrese la cantidad de la moneda: "))
    cotiz = float(input("Ingrese la cotización en USD de la moneda: "))
    i = i+1
#El ciclo while se repetirá tantas veces que "i" sea menor que 5. Para ello al final del bloque
#debemos usar la variable "i" creada anteriormente y hacer el calcuclo "i+1" para decirle a la pc
#que sume uno a "i" luego de cumplir el ciclo. Si esto no se hace el ciclo se vuelve infinito.

valor = valor + (cant*cotiz)
print("Usted tiene " +str(valor) + "Dólares Americanos")