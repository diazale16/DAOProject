# control/GestorVendedor.py
from ..persistency.DBManager import DBManager
from ..entities.VendedorModel import Vendedor

class GestorVendedor:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_vendedor(self, nombre, apellido, comision):
        vendedor = Vendedor(nombre=nombre, apellido=apellido, comision=comision)
        self.db_manager.register(vendedor)
        return vendedor
        
    def modificar_vendedor(self, id_vendedor, nombre=None, apellido=None, comisiones=None):
        vendedor:Vendedor = self.obtener_vendedor(id_vendedor)
        if vendedor:
            if nombre:
                vendedor.nombre = nombre
            if apellido:
                vendedor.apellido = apellido
            if comisiones is not None:
                vendedor.comisiones = comisiones
            self.db_manager.update(vendedor)
    
    def obtener_vendedor(self, id):
        vendedor = self.db_manager.get_by_id(entity_class=Vendedor, entity_id=id)
        return vendedor

    def eliminar_vendedor(self, id):
        vendedor = self.obtener_vendedor(id=id)
        self.db_manager.delete(entity=vendedor)

    def listar_vendedors(self):
        return self.db_manager.get_all(entity_class=Vendedor)
