# control/auto_manager.py

# from app.entities.Auto import Auto
# from app.control.DBManager import DBManager
from ..boundary.Auto.AltaAuto import AltaAuto
from ..entities.Auto import Auto
from ..persistency.DBManager import DBManager

class GestorAuto:
    def __init__(self):
        pass
        # self.db_manager = DBManager()

    def registrar_auto(self):        
        interfazAlta = AltaAuto()
        vin, marca, modelo, año, precio, estado = interfazAlta.registrar_auto()
        
        auto = Auto(vin=vin, marca=marca, modelo=modelo, año=año, precio=precio, estado=estado)
        
        db_manager = DBManager()
        db_manager.register(auto)
        print("añadidoo")
        # session.add(auto)
        # session.commit()
        # session.close()
