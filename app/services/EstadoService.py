# from ..boundary.Auto.AltaAuto import AltaAuto
from ..entities.EstadoModel import Estado
from ..persistency.DBManager import DBManager

class EstadoService:
    def __init__(self):
        pass
    
    # def registrar_estado(self):
    def registrar_estado(self, estado:Estado):
        # interfazAlta = AltaAuto()
        # vin, marca, modelo, año, precio, estado, cliente = interfazAlta.alta()
        # auto = Auto(vin=vin, marca=marca, modelo=modelo, año=año, precio=precio, estado=estado, cliente=cliente)
        db_manager = DBManager()
        db_manager.register(estado)
        
    def modificar_estado(self, estado:Estado):
        db_manager = DBManager()
        db_manager.update(estado)
    
    def eliminar_estado(self, estado:Estado):
        db_manager = DBManager()
        db_manager.delete(estado)
    
    def obtener_estado(self, estado:Estado):
        db_manager = DBManager()
        db_manager.get_by_id(Estado, estado.id)
