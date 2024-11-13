# control/GestorVendedor.py
from ..persistency.DBManager import DBManager
from ..entities.VendedorModel import Vendedor


class GestorVendedor:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_vendedor(self, nombre, apellido, porc_comision):
        vendedor = Vendedor(
            nombre=nombre, apellido=apellido, porc_comision=porc_comision)
        self.db_manager.register(vendedor)
        return vendedor

    def modificar_vendedor(self, id, nombre=None, apellido=None, porc_comision=None):
        vendedor: Vendedor = self.obtener_vendedor(id)
        if vendedor:
            if nombre:
                vendedor.nombre = nombre
            if apellido:
                vendedor.apellido = apellido
            if porc_comision:
                vendedor.porc_comision = porc_comision
            self.db_manager.update(vendedor)

    def obtener_vendedor(self, id):
        return self.db_manager.get_by_id(entity_class=Vendedor, entity_id=id)

    def eliminar_vendedor(self, id):
        vendedor: Vendedor = self.obtener_vendedor(id=id)
        if vendedor:
            self.db_manager.delete(entity=vendedor)

    def listar_vendedors(self):
        return self.db_manager.get_all(entity_class=Vendedor)
    
