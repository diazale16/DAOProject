from ..boundary.Auto.AltaAuto import AltaAuto
from ..entities.AutoModel import Auto
from ..persistency.DBManager import DBManager

class AutoService:
    def __init__(self):
        pass
    
    def registrar_auto(self):
        interfazAlta = AltaAuto()
        vin, marca, modelo, año, precio, estado, cliente = interfazAlta.alta()
        auto = Auto(vin=vin, marca=marca, modelo=modelo, año=año, precio=precio, estado=estado, cliente=cliente)
        db_manager = DBManager()
        db_manager.register(auto)