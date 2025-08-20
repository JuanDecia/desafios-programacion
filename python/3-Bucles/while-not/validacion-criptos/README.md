# 🔍 Validación de Criptomonedas con While

Este desafío demuestra cómo validar que un valor ingresado por el usuario esté presente en un array predefinido de criptomonedas, utilizando un bucle while para garantizar la entrada correcta.

## 📝 Enunciado

Desarrollar un programa que:

* Tenga un array predefinido con nombres de criptomonedas válidas.

* Solicite al usuario ingresar el nombre de una moneda.

* Verifique continuamente si la moneda ingresada existe en el array.

* Permita reintentos ilimitados hasta que se ingrese una moneda válida.

* Informe al usuario cuando la moneda no existe.

* Confirme cuando se ingresa una moneda válida.

* Entrada/salida estándar por consola

## 🔧 Requisitos Técnicos

* Python 3.6+
* Ide
* No se requieren librerías externas

## 🌐 Cómo Usar

1. Ejecución directa del código:

```bash
    python validacion_criptos.py
```

2. Ejemplo de flujo de ejecución:

```text
    Ingrese el nombre de la moneda: doge
    La moneda DOGE no existe. Ingrese el nombre de la moneda: btc
    Moneda Válida.
```

## 📚 Conceptos Aprendidos

* Bucle While con Condición

* Validación con operador 'not in'

## 💡 Optimizaciones:

* Convertir array a set para búsquedas más rápidas

* Implementar timeout después de X intentos

* Agregar opción para salir del bucle