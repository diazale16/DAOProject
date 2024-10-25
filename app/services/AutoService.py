from ..boundary.Auto.AltaAuto import AltaAuto
from ..entities.AutoModel import Auto
from ..persistency.DBManager import DBManager

class AutoService:
    def __init__(self):
        self.db_manager = DBManager()
    
    # def registrar_auto(self):
    def registrar_auto(self, auto:Auto):
        # interfazAlta = AltaAuto()
        # vin, marca, modelo, año, precio, estado, cliente = interfazAlta.alta()
        # auto = Auto(vin=vin, marca=marca, modelo=modelo, año=año, precio=precio, estado=estado, cliente=cliente)
        self.db_manager.register(auto)
        
    def modificar_auto(self, auto:Auto):
        self.db_manager.update(auto)
    
    def eliminar_auto(self, auto:Auto):
        self.db_manager.delete(auto)
    
    def obtener_auto(self, auto:Auto):
        return self.db_manager.get_by_id(Auto, auto.vin)
    
    def listar_autos(self):
        return self.db_manager.get_all(Auto)
