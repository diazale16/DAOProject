from ..persistency.DBManager import DBManager
from ..entities.EstadoModel import Estado


class GestorEstado():
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_estado(self, nombre_estado):
        estado = Estado(nombre=nombre_estado)
        self.db_manager.register(entity=estado)
        return estado

    def modificar_estado(self, id, nom_estado=None):
        estado: Estado = self.db_manager.get_by_id(Estado, id)
        if estado:
            if nom_estado:
                estado.nombre = nom_estado
            self.db_manager.update(entity=estado)

    def obtener_estado(self, id):
        return self.db_manager.get_by_id(entity_class=Estado, entity_id=id)

    def eliminar_estado(self, id):
        estado: Estado = self.obtener_estado(id=id)
        if estado:
            self.db_manager.delete(entity=estado)

    # def obtener_estado(self, id):
    #     return self.db_manager.get_by_id(Estado, id)
