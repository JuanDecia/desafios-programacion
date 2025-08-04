#En este ejemplo, veremos como manipulamos las sublistas.

lista = ["a","b","c","d"]
print(lista[1:3]) #imprime "b" y "c". El conteo del segundo valor es normal.
print(lista[2:]) #Imprime "c" y "d".
print(lista[:2]) #Imprime "a" y "b".
print(lista[::-1]) #Imprime "d", "c", "b", "a". Cuando el número es negativo
                    #el conteo es de derecha a izquierda.

lista[0:2] = "z" #Reemplaza "a" y "b" por "z"
                #quedando así ["z","c","d"]

print(lista) #imprime la lista completa.