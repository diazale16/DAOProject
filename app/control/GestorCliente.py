from ..persistency.DBManager import DBManager
from ..entities.ClienteModel import Cliente

class GestorCliente():
    def __init__(self):
        self.db_manager = DBManager()


    def registrar_cliente(self, nombre, apellido, telefono, direccion):
        cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, direccion=direccion)    
        self.db_manager.register(cliente)
        return cliente

    
    def modificar_cliente(self, id, nombre, apellido, telefono, direccion):
        cliente:Cliente = self.obtener_cliente(id)        
        
        cliente.nombre = nombre
        cliente.apellido = apellido
        cliente.telefono = telefono
        cliente.direccion = direccion
        self.db_manager.update(cliente)

       
    def obtener_cliente(self, id):
        cliente = self.db_manager.get_by_id(Cliente, id)
        return cliente


    def eliminar_cliente(self, id):
        cliente = self.obtener_cliente(id)
        self.db_manager.delete(cliente)
        
    
    def listar_clientes(self):
        clientes_source = self.db_manager.get_all(Cliente) 
        datos_clientes = []
        for cliente in clientes_source:
            if isinstance(cliente, Cliente):
                tupla = (cliente.id, cliente.nombre, cliente.apellido, cliente.telefono, cliente.direccion)
                datos_clientes.append(tupla)
        return datos_clientes
        
        
