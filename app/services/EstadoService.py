# from ..boundary.Auto.AltaAuto import AltaAuto
from ..entities.EstadoModel import Estado
from ..persistency.DBManager import DBManager

class EstadoService:
    def __init__(self):
        self.db_manager = DBManager()
    
    # def registrar_estado(self):
    def registrar_estado(self, estado:Estado):
        self.db_manager.register(estado)
        
    def modificar_estado(self, estado:Estado):
        self.db_manager.update(estado)
    
    def eliminar_estado(self, estado:Estado):
        self.db_manager.delete(estado)
    
    def obtener_estado(self, id):
        return self.db_manager.get_by_id(Estado, id)
