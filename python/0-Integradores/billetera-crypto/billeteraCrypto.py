# Importar libreria de cripto
import json
from pathlib import Path
from pyCoingecko import CoinGeckoAPI

# Obtener la ruta absoluta del directorio actual del script
SCRIPT_DIR = Path(__file__).parent.absolute()
DATA_FILE = SCRIPT_DIR / "cuenta_cripto.json"  # Ruta completa al archivo

# Inicializar la API de CoinGecko
cg = CoinGeckoAPI()

# Obtener precios de las cripto
def get_prices():
    try:
        data = cg.get_price(ids='bitcoin,litecoin,dash', vs_currencies='usd')
        return {
            "BTC": data["bitcoin"]["usd"],
            "LTC": data["litecoin"]["usd"],
            "DASH": data["dash"]["usd"],
        }
    except Exception as e:
        print(f"Error al obtener los precios: {e}.")
        return None

class CryptoAccount:
    def __init__(self):

        self.precios = get_prices()
        self.load_data()  # Cargar datos existentes al iniciar

    # Cargar datos
    def load_data(self):

        try:
            if Path(DATA_FILE).exists():
                with open(DATA_FILE, 'r') as file:
                    data = json.load(file)
                    self.saldos = data.get("saldos", {"BTC": 0.0, "LTC": 0.0, "DASH": 0.0})
                    self.transacciones = data.get("transacciones", [])
            else:
                # Si el archivo no existe, inicializar con valores por defecto
                self.saldos = {
                    "BTC": 0.0,
                    "LTC": 0.0,
                    "DASH": 0.0,
                }
                self.transacciones = []

        except Exception as e:
            print(f"Error cargando datos: {e}")
            self.saldos = {"BTC": 0.0, "LTC": 0.0, "DASH": 0.0}
            self.transacciones = []

    # Guardar datos
    def save_data(self):
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump({
                    'saldos': self.saldos,
                    'transacciones': self.transacciones
                }, f, indent=4)
        except Exception as e:
            print(f"Error guardando datos: {e}")

    def add_amount(self, crypto, amount):
        crypto = crypto.upper()
        if crypto in self.saldos:
            self.saldos[crypto] += amount
            self.transacciones.append((crypto, amount))
            print(f"✅ Añadidos {amount} {crypto} a tu cuenta")
        else:
            print(f"❌ Moneda no válida: {crypto}")
    
    def show_balance(self, ordenados=True):
        print("\n💼 Saldos actuales:")
        saldos_usd = []

        for crypto, amount in self.saldos.items():
            valor_usd = amount * self.precios.get(crypto, 1)
            saldos_usd.append((crypto, amount, valor_usd))

    # Sort saldos_usd by value in descending order if ordenados is True
        if ordenados:
            saldos_usd.sort(key=lambda x: x[2], reverse=True)

        for crypto, amount, valor_usd in saldos_usd:
            print(f"{crypto}: {amount:.8f} (${valor_usd:,.2f} USD)")

    def show_transactions(self):
        print("\n📋 Histórico de transacciones:")
        for i, (moneda, cantidad) in enumerate(self.transacciones, 1):
            print(f"{i}. {moneda}: {cantidad}")
    
# Main Function
def main():

    account = CryptoAccount()
    print(f"💰 Saldo actual: {account.saldos}")  # Muestra saldo existente


    # Load Amounts
    print("💰 Gestor de Criptomonedas")
    print("Monedas soportadas: BTC, LTC, DASH")

    for i in range(3):
        while True:
            try:
                crypto = input(f"Ingrese la criptomoneda a añadir (BTC, LTC, DASH) #{i+1}: ").strip().upper()
                amount = float(input(f"Ingrese la cantidad de {crypto} a añadir: "))
                account.add_amount(crypto, amount)
                break
            except ValueError:
                print("❌ Cantidad inválida. Inténtalo de nuevo.")
    
    # Show Balances
    account.show_balance()
    # Show Transactions
    account.show_transactions()
    # Save Data
    account.save_data()

if __name__ == "__main__":
    main()
