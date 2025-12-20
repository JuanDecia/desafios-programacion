#Desarrollaremos un programa que nos permita ingresar un código de usuario
#y realize la validación de este código, verificando que c/u de sus caracteres pertenezcan
#a un conjunto de caracteres válidos, pre-definidos por el programa.
#Se le solicitará al usuario ingresar el código y sólo se le permitirá continuar una
#vez que introduzca un código que tenga válidos todos sus caracteres.

#1° asignamos los caracteres válidos para ingresar al codigo en una variable llamada: valid alpha mail.
#en la asignación indicamos que estan disponibles los caracteres con minúsculas, mayúsculas, números
#y 3 caracteres especiales.

#2° usaremos el ciclo while para garantizar la verificación del código del usuario. Dentro del ciclo
#iterativo usaremos los "conjuntos: set()".

#3° los conjuntos van a verificar los caracteres. Esto nos indica que si algún caracter del conjunto b
#no pertenece al conjunto A. Si, ningún caracter pertenece al conjunto A, obtendremos un tamaño <0
#indicando que el codigo se encuentra en la variable B en forma de conjunto lo cual es un
#codigo inválido.

#4° para realizar la función anterior, debemos abrir otro condicional con el siguiente argumento:
# if len(b-a)>0: "si b-a es mayor a 0" el codigo es inválido.

#5° en el caso de que el resultado sea False. Debemos imprimir "usuario inválido" y luego
#usar la función "continue" para que se vuelva a ejecutar el ciclo y que el usuario ingrese los
#caracteres válidos.

#6° si la operación es True, debemos usar "else" para imprimir que el usuario es válido y luego continuar
#con la función de "break" porque el ciclo se tiene que cerrar.

#7° nos queda el último "else" donde si el usuario ingreso un código menor o igual a 4 caracteres
# debemos imprimir en ese mismo "else" que el usuario no es válido.

# Validación de usuario
def valid_alpha_mail():
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_."

# Creación de usuario
def user_creation():
    valid_alpha_mails = valid_alpha_mail()  # Llamamos a la función para obtener los caracteres válidos

    # Bucle para solicitar el nombre de usuario
    while True:

        # Solicitar al usuario que ingrese su nombre
        user = input("Ingrese el nombre del usuario: ")

        # Validar que el usuario tenga más de 4 caracteres
        if len(user) > 4:

            # Convertimos los caracteres válidos y el usuario a conjuntos
            a = set(valid_alpha_mails)
            b = set(user)

            # Verifica si b-a es mayor a 0
            if len(b - a) > 0:  
                print("❌ Usuario inválido.")
                continue
            else:
                print("✅ Usuario válido.")
                break
        else:
            print("❌ Usuario inválido.")

def main():
    print("Bienvenido al sistema de validación de usuario.")
    user_creation()

if __name__ == "__main__":
    main()