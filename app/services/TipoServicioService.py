from ..entities.TipoServicioModel import TipoServicio
from ..persistency.DBManager import DBManager

class TipoServicioService:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_tipo_servicio(self, tipo_servicio: TipoServicio):
        self.db_manager.register(tipo_servicio)
        
    def modificar_tipo_servicio(self, tipo_servicio: TipoServicio):
        self.db_manager.update(tipo_servicio)
    
    def eliminar_tipo_servicio(self, tipo_servicio: TipoServicio):
        self.db_manager.delete(tipo_servicio)
    
    def obtener_tipo_servicio(self, id_tipo_servicio):
        return self.db_manager.get_by_id(TipoServicio, id_tipo_servicio)
    
    def listar_tipos_servicio(self):
        tipos_servicio_source = self.db_manager.get_all(TipoServicio)
        return [tipo for tipo in tipos_servicio_source]
