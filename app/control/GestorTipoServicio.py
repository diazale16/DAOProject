from ..persistency.DBManager import DBManager
from ..entities.TipoServicioModel import TipoServicio


class GestorTipoServicio:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_tipo_servicio(self, nombre):
        tipo_servicio = TipoServicio(nombre=nombre)
        self.db_manager.register(entity=tipo_servicio)
        return tipo_servicio

    # def modificar_tipo_servicio(self, id, nombre=None):
    #     tipo_servicio: TipoServicio = self.obtener_tipo_servicio(id)
    #     if tipo_servicio:
    #         if nombre:
    #             tipo_servicio.nombre = nombre
    #         self.db_manager.update(entity=tipo_servicio)

    def obtener_tipo_servicio(self, id):
        return self.db_manager.get_by_id(entity_class=TipoServicio, entity_id=id)

    def eliminar_tipo_servicio(self, id):
        tipo_servicio: TipoServicio = self.obtener_tipo_servicio(id=id)
        if tipo_servicio:
            self.db_manager.delete(entity=tipo_servicio)

    def listar_tipos_servicio(self):
        return self.db_manager.get_all(entity_class=TipoServicio)
