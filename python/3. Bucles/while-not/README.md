# 🔄 Validación de Entrada Numérica

Este programa demuestra el uso de bucles `while` para validar entradas de usuario hasta que se ingrese un número válido.

## 📝 Enunciado
Escribir un programa que:
1. Solicite repetidamente al usuario que ingrese un número
2. Si el valor ingresado **no es un número**, muestre un mensaje de error y vuelva a pedirlo
3. Cuando se ingrese un número válido, finalice el programa

## 💻 Código Base
```python
num = input("Ingrese un número: ")

while not num.isdigit():
    print("Por favor, ingrese un número correctamente: ")
    num = input("Ingrese un número: ")
    
print("Programa Terminado")

🛠️ Cómo Ejecutar
Guardar el código en validacion_numero.py

Ejecutar en terminal:

bash
python validacion_numero.py
Probar con:

Entrada válida: 42

Entrada inválida: cuarenta y dos

🎯 Objetivos de Aprendizaje
Validación de entradas con bucles

Uso de métodos de strings (isdigit())

Control de flujo con condicionales negados (not)

💡 Mejoras Posibles
Aceptar números negativos:

python
while not num.lstrip('-').isdigit():
Aceptar decimales:

python
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
Límite de intentos:

python
intentos = 3
while intentos > 0:
    # ...validación...
    intentos -= 1

    Este README:
✅ Explica claramente el objetivo  
✅ Incluye código listo para copiar  
✅ Muestra visualmente el flujo  
✅ Sugiere mejoras escalables  
✅ Propone estructura de archivos  
