# control/GestorVendedor.py
from ..persistency.DBManager import DBManager
from ..entities.VendedorModel import Vendedor
from ..entities.ComisionModel import Comision


class GestorVendedor:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_vendedor(self, nombre, apellido, comision):
        vendedor = Vendedor(
            nombre=nombre, apellido=apellido, comision=comision)
        self.db_manager.register(vendedor)
        return vendedor

    def modificar_vendedor(self, id, nombre=None, apellido=None, comision=None):
        vendedor: Vendedor = self.obtener_vendedor(id)
        if vendedor:
            if nombre:
                vendedor.nombre = nombre
            if apellido:
                vendedor.apellido = apellido
            if comision:
                vendedor.comision = comision
            self.db_manager.update(vendedor)

    def obtener_vendedor(self, id):
        return self.db_manager.get_by_id(entity_class=Vendedor, entity_id=id)

    def eliminar_vendedor(self, id):
        vendedor: Vendedor = self.obtener_vendedor(id=id)
        if vendedor:
            self.db_manager.delete(entity=vendedor)

    def listar_vendedors(self):
        return self.db_manager.get_all(entity_class=Vendedor)
    
