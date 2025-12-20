#Escribe un programa en python que dada una criptomoneda, la cantidad acomulada y su correspondiente 
#cotización por USD$, le permita al usuario conocer la fecha y hora del momento en el que 
#obtuvo el sistema esa información, así como el monto en USD$ que tiene el usuario en su wallet
#Considerando un crecimiento del 5% por día, muestrale al usuario para ese mismo día de la siguiente
#semana cuál sería su ganancia en USD$.

import json
import datetime
import requests
import os
import time

# Archivo JSON para guardar el historial
HISTORIAL_FILE = "historial.json"

# Configuración de la API (CoinGecko)
API_BASE_URL = "https://api.coingecko.com/api/v3"

CRYPTO_IDS = {
    "BTC": "bitcoin",
    "ETH": "ethereum", 
    "BNB": "binancecoin",
    "ADA": "cardano",
    "XRP": "ripple",
    "SOL": "solana",
    "DOT": "polkadot",
    "DOGE": "dogecoin",
    "AVAX": "avalanche-2",
    "MATIC": "matic-network"
}

def obtener_cotizacion_actual(criptomoneda):
    """Obtiene la cotización actual en USD desde CoinGecko API"""
    cripto_id = CRYPTO_IDS.get(criptomoneda.upper())
    
    if not cripto_id:
        return None, f"Criptomoneda {criptomoneda} no soportada"
    
    try:
        url = f"{API_BASE_URL}/simple/price"
        params = {
            'ids': cripto_id,
            'vs_currencies': 'usd'
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        if cripto_id in data and 'usd' in data[cripto_id]:
            return data[cripto_id]['usd'], None
        else:
            return None, "No se pudo obtener la cotización"
            
    except requests.exceptions.RequestException as e:
        return None, f"Error de conexión: {str(e)}"
    except Exception as e:
        return None, f"Error inesperado: {str(e)}"

# Cargar historial JSON
def cargar_historial():
    if os.path.exists(HISTORIAL_FILE):
        try:
            with open(HISTORIAL_FILE, 'r') as file:
                historial = json.load(file)
                return historial
        except FileNotFoundError:
            return []
    return []

# Guardar Historial JSON
def guardar_historial(historial):
    with open(HISTORIAL_FILE, 'w') as file:
        json.dump(historial, file, indent=4)

# Agregar Transacción
def agregar_transaccion(historial, cripto: str, cantidad: float, precio: float, operacion):
    
    # Datos que guarda
    transaccion = {
        "fecha_hora": datetime.datetime.now().isoformat(),
        "criptomoneda": cripto.upper(),
        "cantidad": cantidad,
        "precio": precio,
        "operacion": operacion,
        "monto_usd": cantidad * precio
    }

    # Agregar transacción al historial
    historial.append(transaccion)

    # Guardar historial actualizado
    guardar_historial(historial)

    # Retornar historial actualizado
    return historial

# Calcular el total de la biletera
def calcular_total_wallet(historial):
    
    resumen = {
        "total_usd": 0,
        "detalle_criptos": {}
    }

    for transaccion in historial:
        cripto = transaccion["criptomoneda"]
        cantidad = transaccion["cantidad"]
        monto_usd = transaccion["monto_usd"]
        
        if transaccion["operacion"] == "suma":
            if cripto not in resumen["detalle_criptos"]:
                resumen["detalle_criptos"][cripto] = {
                    "cantidad": 0,
                    "inversion_usd": 0
                }
            resumen["detalle_criptos"][cripto]["cantidad"] += cantidad
            resumen["detalle_criptos"][cripto]["inversion_usd"] += monto_usd
            resumen["total_usd"] += monto_usd
        elif transaccion["operacion"] == "resta":
            if cripto in resumen["detalle_criptos"]:
                resumen["detalle_criptos"][cripto]["cantidad"] -= cantidad
                resumen["detalle_criptos"][cripto]["inversion_usd"] -= monto_usd
                resumen["total_usd"] -= monto_usd

    return resumen

def obtener_valor_actual_portafolio(resumen):
    """
    Obtiene el valor actual del portafolio con precios reales
    """

    valor_actual_total = 0
    detalle_actual = {}
    
    for cripto, datos in resumen["detalle_criptos"].items():
        if datos["cantidad"] > 0:
            precio_actual, error = obtener_cotizacion_actual(cripto)
            if precio_actual:
                valor_cripto = datos["cantidad"] * precio_actual
                valor_actual_total += valor_cripto
                detalle_actual[cripto] = {
                    "cantidad": datos["cantidad"],
                    "precio_actual": precio_actual,
                    "valor_actual": valor_cripto,
                    "inversion": datos["inversion_usd"],
                    "ganancia_perdida": valor_cripto - datos["inversion_usd"]
                }
    
    return valor_actual_total, detalle_actual

# Proyectar Ganancias
def proyectar_ganancias(monto_actual, dias=7, tasa_crecimiento=0.05):
    
    """
    Proyecta las ganancias futuras basadas en un monto actual, número de días
    y tasa de crecimiento.
    """

    return monto_actual * ((1 + tasa_crecimiento) ** dias)

# Mostrar historial
def mostrar_historial(historial):
    
    print("\n" + "="*60)
    print("HISTORIAL DE TRANSACCIONES")
    print("="*60)

    for i, transaccion in enumerate(historial, 1):
        print(f"{i}. {transaccion['fecha_hora']} - {transaccion['criptomoneda']}")
        print(f"  Cantidad: {transaccion['cantidad']}")
        print(f"  Precio: {transaccion['precio']: .6f}")
        print(f"  Operación: {transaccion['operacion'].upper()}")
        print(f"  Monto USD: {transaccion['monto_usd']: .2f}")
        print("-" * 40)

def mostrar_criptos_soportadas():
    """Muestra las criptomonedas soportadas"""
    print("\n🪙 Criptomonedas soportadas:")
    print(", ".join(CRYPTO_IDS.keys()))
    print("(Puedes sugerir más en las issues del proyecto)")

def main():
    # Cargar historial existente
    historial = cargar_historial()
    
    print("💰 WALLET DE CRIPTOMONEDAS CON API REAL 💰")
    print("=" * 50)
    print("📡 Conectado a CoinGecko API")
    print("=" * 50)
    
    while True:
        print("\n🎯 Opciones:")
        print("1. Agregar criptomoneda")
        print("2. Restar criptomoneda")
        print("3. Ver historial")
        print("4. Ver resumen actual con valores reales")
        print("5. Ver criptomonedas soportadas")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        if opcion == "6":
            print("¡Hasta luego! 💸")
            break
            
        elif opcion == "5":
            mostrar_criptos_soportadas()
            
        elif opcion == "4":
            print("\n📡 Obteniendo cotizaciones actuales...")
            resumen = calcular_total_wallet(historial)
            valor_actual, detalle_actual = obtener_valor_actual_portafolio(resumen)
            
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print("\n" + "="*80)
            print("📊 RESUMEN ACTUAL DEL WALLET (VALORES REALES)")
            print("="*80)
            print(f"📅 Fecha y hora: {fecha_actual}")
            print(f"💵 Valor total actual: ${valor_actual:,.2f}")
            print(f"📈 Inversión total: ${resumen['total_usd']:,.2f}")
            print(f"💰 Ganancia/Pérdida: ${(valor_actual - resumen['total_usd']):,.2f}")
            
            print(f"\n🔍 Detalle por criptomoneda:")
            for cripto, datos in detalle_actual.items():
                estado = "🟢" if datos["ganancia_perdida"] >= 0 else "🔴"
                print(f"{estado} {cripto}:")
                print(f"   Cantidad: {datos['cantidad']:.8f}")
                print(f"   Precio actual: ${datos['precio_actual']:,.2f}")
                print(f"   Valor actual: ${datos['valor_actual']:,.2f}")
                print(f"   Inversión: ${datos['inversion']:,.2f}")
                print(f"   G/P: ${datos['ganancia_perdida']:,.2f}")
            
            # Proyección para la próxima semana
            if valor_actual > 0:
                ganancia_proyectada = proyectar_ganancias(valor_actual)
                print(f"\n📈 PROYECCIÓN (7 días con 5% diario):")
                print(f"💰 Monto proyectado: ${ganancia_proyectada:,.2f}")
                print(f"🎯 Ganancia estimada: ${(ganancia_proyectada - valor_actual):,.2f}")
            
            print("="*80)
            
        elif opcion == "3":
            mostrar_historial(historial)
            
        elif opcion in ["1", "2"]:
            try:
                mostrar_criptos_soportadas()
                cripto = input("\nIngrese la criptomoneda: ").strip().upper()
                
                if cripto not in CRYPTO_IDS:
                    print(f"❌ Criptomoneda {cripto} no está soportada.")
                    continue
                
                print("📡 Obteniendo cotización actual...")
                cotizacion, error = obtener_cotizacion_actual(cripto)
                
                if error:
                    print(f"❌ {error}")
                    usar_manual = input("¿Desea ingresar la cotización manualmente? (s/n): ").lower()
                    if usar_manual != 's':
                        continue
                    cotizacion = float(input("Ingrese la cotización manual en USD: "))
                else:
                    print(f"✅ Cotización actual de {cripto}: ${cotizacion:,.2f}")
                
                cantidad = float(input("Ingrese la cantidad: "))
                
                operacion = "suma" if opcion == "1" else "resta"
                
                historial = agregar_transaccion(historial, cripto, cantidad, cotizacion, operacion)
                
                resumen = calcular_total_wallet(historial)
                fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                print(f"\n✅ Transacción registrada exitosamente!")
                print(f"📅 Fecha/hora: {fecha_actual}")
                print(f"🔧 Operación: {operacion.upper()} {cantidad} {cripto}")
                print(f"💵 Cotización: ${cotizacion:,.2f}")
                print(f"💰 Monto USD: ${cantidad * cotizacion:,.2f}")
                print(f"📊 Total wallet: ${resumen['total_usd']:,.2f}")
                
            except ValueError:
                print("❌ Error: Ingrese valores numéricos válidos.")
            except Exception as e:
                print(f"❌ Error inesperado: {str(e)}")
                
        else:
            print("❌ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()