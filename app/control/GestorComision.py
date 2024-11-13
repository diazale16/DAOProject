
from ..persistency.DBManager import DBManager
from ..entities.ComisionModel import Comision


class GestorComision():
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_comision(self, monto, fecha, vendedor_id):
        # reg comision por venta para el vendedor
        comision = Comision(monto=monto, fecha=fecha, vendedor_id=vendedor_id)
        self.db_manager.register(entity=comision)
        return comision

    def obtener_comision(self, id):
        return self.db_manager.get_by_id(entity_class=Comision, entity_id=id)

    def eliminar_venta(self, id):
        comision:Comision = self.obtener_comision(id=id)
        if comision:
            self.db_manager.delete(entity=comision)

    def listar_comisiones(self):
        return self.db_manager.get_all(entity_class=Comision)