#La función "conversioncriptomoneda()" permite convertir una cantidad de dinero acomulada. Retorna el monto
#total de la suma de los valores calculados.

#Para iniciar una funcion debemos inicializar con la palabra clave "def" seguido por el nombre de la función
#"def nombrefuncion()" y si es necesario seguido de parámetros "()".

def conversionCriptomoneda(cantBTC,cantXRP):
    BTCUSD = 50
    XRPUSD = 0.660982
    valortotalUSD = (cantBTC*BTCUSD) + (cantXRP*XRPUSD)
    print("La suma de la cantidad de sus monedas es de USD$: " + str(valortotalUSD))

conversionCriptomoneda(15,30)

conversionCriptomoneda(4,22)