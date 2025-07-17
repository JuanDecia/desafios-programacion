# 💰 Conversor de Criptomonedas a USD

Desafío práctico para aplicar condicionales en Python, convirtiendo cantidades de criptomonedas (BTC, DASH, LTC) a dólares estadounidenses (USD).

## 🔍 Enunciado
El programa debe:
1. Pedir al usuario que ingrese una moneda (BTC, DASH o LTC).
2. Validar que la moneda sea soportada.
3. Si es válida, solicitar una cantidad y convertirla a USD según el valor de la moneda.
4. Mostrar el resultado o un mensaje de error.

## 📋 Requisitos
- Usar estructuras condicionales (`if-elif-else`).
- Validar entrada del usuario.
- Manejar números decimales.

## 🎯 Ejemplo de Entrada/Salida
```python
# Ejemplo 1:
Ingrese la moneda a utilizar(BTC, DASH o LTC): BTC
Ingrese la cantidad a utilizar: 0.5
La cantidad de USD recargado fue de: 3815.4

# Ejemplo 2:
Ingrese la moneda a utilizar(BTC, DASH o LTC): ETH
Error: Solo se permite utilizar BTC, DASH o LTC

🚀 Cómo Ejecutar
Navega al directorio del desafío:

bash
cd python/2-condicionales/conversor-cripto
Ejecuta el script:

bash
python solucion.py
💡 Solución
El código utiliza:

Un if principal para validar la moneda ingresada.

Condicionales anidados (elif) para seleccionar la tasa de conversión correcta.

Conversión de tipos (float()) para manejar cantidades decimales.

📌 Notas
Los valores de las criptomonedas están hardcodeados según el desafío original.

Para una versión avanzada, se podrían obtener tasas en tiempo real usando una API.

text

---

### **Contenido de `solucion.py`** *(optimizado)*  
```python
# Tasas de conversión (USD)
BTCUSD = 7630.80
DASHUSD = 315.56
LTCUSD = 120.84

def convertir_cripto():
    moneda = input("Ingrese la moneda a utilizar (BTC, DASH o LTC): ").strip().upper()
    if moneda in ("BTC", "DASH", "LTC"):
        try:
            cantidad = float(input("Ingrese la cantidad a utilizar: "))
            if moneda == "BTC":
                monto = cantidad * BTCUSD
            elif moneda == "DASH":
                monto = cantidad * DASHUSD
            else:
                monto = cantidad * LTCUSD
            print(f"La cantidad de USD recargado fue de: {monto:.2f}")  # Formato a 2 decimales
        except ValueError:
            print("Error: Ingrese una cantidad numérica válida")
    else:
        print("Error: Solo se permite utilizar BTC, DASH o LTC")

if __name__ == "__main__":
    convertir_cripto()
Mejoras Implementadas
Validación adicional:

Uso de .strip().upper() para normalizar la entrada.

Manejo de errores con try-except para cantidades no numéricas.

Formato profesional:

Función encapsulada (convertir_cripto()).

if __name__ == "__main__" para buenas prácticas.

Legibilidad:

Comentarios explicativos.

Strings formateados (f-strings).