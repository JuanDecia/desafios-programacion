## DESAFÍO LISTAS #1 ##

# Función para cargar una lista con valores de ejemplo.
def cargar_lista() -> list:
    lista = []
    
    cantidad_elementos = int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))
    
    for i in range(cantidad_elementos):
        elemento = input(f"Ingrese el elemento {i + 1}: ")
        lista.append(elemento)

    return lista

def manipular_lista(lista: list) -> list:

    while True:
        print("\nLista actual:", lista)
        print("\nOpciones de manipulación:")
        print("1. Mostrar sublista [inicio:fin]")
        print("2. Mostrar sublista desde un índice hasta el final [inicio:]")
        print("3. Mostrar sublista desde el inicio hasta un índice [:fin]")
        print("4. Invertir lista [::-1]")
        print("5. Reemplazar elementos por un valor")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            inicio = int(input("Ingrese el índice de inicio: "))
            fin = int(input("Ingrese el índice de fin: "))
            print("Sublista:", lista[inicio:fin])

        elif opcion == '2':
            inicio = int(input("Ingrese el índice de inicio: "))
            print("Sublista:", lista[inicio:])

        elif opcion == '3':
            fin = int(input("Ingrese el índice de fin: "))
            print("Sublista:", lista[:fin])

        elif opcion == '4':
            print("Lista invertida:", lista[::-1])

        elif opcion == '5':
            elemento_viejo = input("Ingrese el elemento a reemplazar: ")
            elemento_nuevo = input("Ingrese el nuevo elemento: ")
            lista = [elemento_nuevo if x == elemento_viejo else x for x in lista]
            print("Lista después de reemplazar elementos:", lista)

        elif opcion == '6':
            break

        else:
            print("Opción no válida, intente de nuevo.")

def main():
    
    lista = ["a","b","c","d"]

    # El usuario selecciona si desea cargar una lista o usar una de ejemplo
    opcion = input("¿Desea cargar una lista personalizada? (s/n): ").strip().lower()
    if opcion == 's':
        lista_usuario = cargar_lista()
        print("Lista cargada:", lista_usuario)
    else:
        print("Usando lista de ejemplo:", lista)

    manipular_lista(lista)

if __name__ == "__main__":
    main()