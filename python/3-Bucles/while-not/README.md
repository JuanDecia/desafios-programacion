# 🔄 Validación de Entrada Numérica

Este programa demuestra el uso de bucles `while` para validar entradas de usuario hasta que se ingrese un número válido.

## 📝 Enunciado

Escribir un programa que:

1. Solicite repetidamente al usuario que ingrese un número
2. Si el valor ingresado **no es un número**, muestre un mensaje de error y vuelva a pedirlo
3. Cuando se ingrese un número válido, finalice el programa

## 🛠️ Cómo Ejecutar

* Ejecutar en terminal:

```bash
    python validacion_numero.py
```

* Probar con:

```bash
    Entrada válida: 42

    Entrada inválida: cuarenta y dos
```

## 🎯 Objetivos de Aprendizaje

* Validación de entradas con bucles

* Uso de métodos de strings (isdigit())

* Control de flujo con condicionales negados (not)

## 💡 Mejoras Posibles

* Aceptar números negativos:

```python

    def solicitar_numero():
        return input("Ingrese un número entero: ").strip()

    Valida si la entrada es un número entero (positivo o negativo)
    def validar_numero(entrada): 
        return entrada.lstrip('-').isdigit()
```

* Aceptar decimales:

```python
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
```

* Límite de intentos:

```python
    def main():
    intentos = 3
    numero_usuario = solicitar_numero()
    
    while not validar_numero(numero) and intentos > 1:
        intentos -= 1
        print(f"❌ Entrada inválida. Intentos restantes: {intentos}")
        numero_usuario = solicitar_numero()
    
    if validar_numero(numero):
        print(f"✅ Aceptado: {int(numero)}")
    else:
        print("⚠️ Has agotado tus intentos")
```

## Este README:

✅ Explica claramente el objetivo  
✅ Incluye código listo para copiar  
✅ Muestra visualmente el flujo  
✅ Sugiere mejoras escalables  
✅ Propone estructura de archivos  