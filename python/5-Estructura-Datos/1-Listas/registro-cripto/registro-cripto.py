#Escribe un programa que registre el nombre de cinco criptomonedas, con sus respectivas cantidades
#y precios en USD, haciendo uso de Arreglos. Posteriormente, imprima los datos de cada moneda
#luego de ser ingresados por el usuario.

def esmoneda(cripto):
    criptos = ["btc","bcc","ltc","eth","etc"]
    if cripto in criptos:
        return True
    else:
        return False

def esnumero(numero):
    return numero.replace('.','',1).isdigit()

criptos = [] #Array vacio, luego se le agregan los datos del ciclo while.
cant = [] #Array vacio, luego se le agregan los datos del ciclo while.
cotiz = [] #Array vacio, luego se le agregan los datos del ciclo while.
i=0
while i < 5:
    criptoname = input("Ingrese el nombre de la moneda: ")
    if esmoneda(criptoname):
        criptos.append(criptoname) #el valor se agrega al array "criptos".
        criptocant = ""
        while not esnumero(criptocant):
            criptocant=input("Ingrese la cantidad de "+criptoname+": ")
        criptocotiz = ""
        while not esnumero(criptocotiz):
            criptocotiz=input("Ingrese la cotización en USD de "+criptoname+": ")
        cant.append(criptocant)
        cotiz.append(criptocotiz)
        i=i+1
    else:
        print("Moneda invalida")

i=0
while i < 5:
    print("Moneda: "+criptos[i]+", Cantidad: "+cant[i]+", Valor en USD: "+cotiz[i])
    i=i+1
