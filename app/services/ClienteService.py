# services/ClienteService.py

from ..entities.ClienteModel import Cliente
from ..persistency.DBManager import DBManager

class ClienteService:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_cliente(self, cliente: Cliente):
        self.db_manager.register(cliente)
        
    def modificar_cliente(self, cliente: Cliente):
        self.db_manager.update(cliente)
    
    def eliminar_cliente(self, cliente: Cliente):
        self.db_manager.delete(cliente)
    
    def obtener_cliente(self, id_cliente):
        return self.db_manager.get_by_id(Cliente, id_cliente)
    
    def listar_clientes(self):
        clientes_source = self.db_manager.get_all(Cliente)
        datos_clientes = []
        for cliente in clientes_source:
            if isinstance(cliente, Cliente):
                tupla = (cliente.id, cliente.nombre, cliente.apellido, cliente.direccion, cliente.telefono)
                datos_clientes.append(tupla)
        return datos_clientes
