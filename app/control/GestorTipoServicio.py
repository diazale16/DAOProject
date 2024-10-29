from ..persistency.DBManager import DBManager
from ..entities.TipoServicioModel import TipoServicio

class GestorTipoServicio:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_tipo_servicio(self, nombre):
        tipo_servicio = TipoServicio(nombre=nombre)
        self.db_manager.register(entity=tipo_servicio)
        return tipo_servicio

    def modificar_tipo_servicio(self, id_tipo_servicio, nombre=None):
        tipo_servicio = self.tipo_servicio_service.obtener_tipo_servicio(id_tipo_servicio)
        if tipo_servicio:
            if nombre:
                tipo_servicio.nombre = nombre
            self.tipo_servicio_service.modificar_tipo_servicio(tipo_servicio)
            print("Tipo de servicio modificado con éxito.")
    
    def eliminar_tipo_servicio(self, id_tipo_servicio):
        tipo_servicio = self.tipo_servicio_service.obtener_tipo_servicio(id_tipo_servicio)
        if tipo_servicio:
            self.tipo_servicio_service.eliminar_tipo_servicio(tipo_servicio)
            print("Tipo de servicio eliminado con éxito.")
    
    def obtener_tipo_servicio(self, id):
        return self.db_manager.get_by_id(entity_class=TipoServicio, entity_id=id)
    
    def listar_tipos_servicio(self):
        return self.db_manager.get_all(entity_class=TipoServicio)
