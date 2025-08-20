#Escribe un programa en python que dada una criptomoneda, la cantidad acomulada y su correspondiente 
#cotización por USD$, le permita al usuario conocer la fecha y hora del momento en el que 
#obtuvo el sistema esa información, así como el monto en USD$ que tiene el usuario en su wallet
#Considerando un crecimiento del 5% por día, muestrale al usuario para ese mismo día de la siguiente
#semana cuál sería su ganancia en USD$.

import time
ahora = time.strftime("%c") # Retorna la hora en tiempo real.

nombre_cripto = "Bitcoin"
cantidad_cripto = float(1)
cotizacion = float(4001)

valor_total = cantidad_cripto * cotizacion

print("El día de la fecha: " +ahora+ " usted posee un total de USD$: " +str(valor_total)+ " en " 
        +nombre_cripto+ ".")

total_lun = valor_total * 1.05
total_mar = total_lun * 1.05
total_mie = total_mar * 1.05
total_jue = total_mie * 1.05
total_vie = total_jue * 1.05
total_semana = total_vie * 1.05

print("Con la bonificación del %5 en una semana su saldo será: " +str("{0:.2f}".format(total_semana)))
#"{0:.2f}".format() limita el resultado matematico a: total +2 decimales.