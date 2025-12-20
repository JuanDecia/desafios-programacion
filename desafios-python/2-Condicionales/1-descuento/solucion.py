#En una tienda se hace el 10% de descuento a los clientes cuya compra sea menor a $100.
#20% si los supera. ¿Cual será el valor a pagar de los usuarios?

compra = float(input("Ingrese el valor de su compra: "))

if compra <= 100:
    descuento1 = compra * 0.1
    total1 = compra - descuento1
    print("Usted debe abonar " + str(total1))
else:
    descuento2 = compra * 0.2
    total2 = compra - descuento2
    print("Usted debe abonar " + str(total2))