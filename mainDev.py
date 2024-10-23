from app.persistency.DBManager import DBManager
from app.control.GestorAuto import GestorAuto

def main():
    # Inicializamos el AutoManager
    auto_manager = GestorAuto()
    # Datos de prueba
    # vin = "1HGCM82633A123456"
    # marca = "Toyota"
    # modelo = "Corolla"
    # año = 2022
    # precio = 20000.0
    # estado = "nuevo"
    auto_manager.registrar_auto()

if __name__ == "__main__":
    main()
