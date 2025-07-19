# 📊 Ordenador de Criptomonedas por Cantidad

Programa que recibe tres criptomonedas con sus cantidades y las muestra ordenadas de mayor a menor.

## 🔍 Enunciado
El programa debe:
1. Solicitar al usuario los nombres y cantidades de 3 criptomonedas.
2. Mostrarlas ordenadas de forma decreciente según su cantidad.
3. Manejar posibles empates (aunque el código actual los muestra en orden de entrada).

## 📋 Requisitos
- Usar estructuras condicionales anidadas (`if-elif-else`).
- Validar que las cantidades sean numéricas.
- Mostrar el resultado formateado claramente.

## 🎯 Ejemplo de Entrada/Salida
```python
# Ejemplo 1:
Ingrese el nombre de la primera moneda: BTC
Ingresa la cantidad de BTC: 1.5
Ingrese el nombre de la segunda moneda: ETH
Ingresa la cantidad de ETH: 3.2
Ingrese el nombre de la tercera moneda: SOL
Ingresa la cantidad de SOL: 5.1

SOL 5.1
ETH 3.2
BTC 1.5

# Ejemplo 2 (con empate):
Ingrese el nombre de la primera moneda: ADA
Ingresa la cantidad de ADA: 10
Ingrese el nombre de la segunda moneda: DOT
Ingresa la cantidad de DOT: 10
Ingrese el nombre de la tercera moneda: XRP
Ingresa la cantidad de XRP: 8

ADA 10
DOT 10
XRP 8
🚀 Cómo Ejecutar
Navega al directorio:

bash
cd python/2-condicionales/ordenar-criptomonedas
Ejecuta:

bash
python solucion.py
💡 Solución
El código utiliza:

Condicionales anidados para comparar las 3 cantidades.

6 posibles escenarios de ordenamiento (3! permutaciones).

Inputs directos sin validación adicional (para simplificar el ejemplo base).

🛠️ Mejoras Posibles
Usar listas y el método sort() para simplificar la lógica.

Añadir validación de entradas numéricas.

Mostrar el valor en USD junto al ordenamiento.

text

---

### **Contenido de `solucion.py` (versión optimizada)**
```python
def ordenar_criptos():
    # Entrada de datos
    moneda1 = input("Ingrese el nombre de la primera moneda: ").strip().upper()
    cant1 = float(input(f"Ingresa la cantidad de {moneda1}: "))
    
    moneda2 = input("Ingrese el nombre de la segunda moneda: ").strip().upper()
    cant2 = float(input(f"Ingresa la cantidad de {moneda2}: "))
    
    moneda3 = input("Ingrese el nombre de la tercera moneda: ").strip().upper()
    cant3 = float(input(f"Ingresa la cantidad de {moneda3}: "))

    # Lógica de ordenamiento
    print("\nResultado ordenado:")
    if cant1 >= cant2 and cant1 >= cant3:
        print(f"{moneda1} {cant1}")
        if cant2 >= cant3:
            print(f"{moneda2} {cant2}\n{moneda3} {cant3}")
        else:
            print(f"{moneda3} {cant3}\n{moneda2} {cant2}")
    elif cant2 >= cant1 and cant2 >= cant3:
        print(f"{moneda2} {cant2}")
        if cant1 >= cant3:
            print(f"{moneda1} {cant1}\n{moneda3} {cant3}")
        else:
            print(f"{moneda3} {cant3}\n{moneda1} {cant1}")
    else:
        print(f"{moneda3} {cant3}")
        if cant1 >= cant2:
            print(f"{moneda1} {cant1}\n{moneda2} {cant2}")
        else:
            print(f"{moneda2} {cant2}\n{moneda1} {cant1}")

if __name__ == "__main__":
    ordenar_criptos()
Mejoras Implementadas
Legibilidad:

Uso de f-strings para formateo claro.

Encapsulado en función ordenar_criptos().

Normalización de inputs con .strip().upper().

Presentación:

Salida con \n para mejor espaciado.

Mensaje "Resultado ordenado:" para claridad.

Extensibilidad:

Estructura lista para añadir validaciones o conversiones.