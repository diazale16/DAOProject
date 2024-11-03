from ..persistency.DBManager import DBManager
from ..entities.ClienteModel import Cliente


class GestorCliente():
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_cliente(self, nombre, apellido, telefono, direccion):
        # cliente
        cliente = Cliente(nombre=nombre, apellido=apellido,
                          telefono=telefono, direccion=direccion)
        self.db_manager.register(entity=cliente)
        return cliente

    def modificar_cliente(self, id, nombre=None, apellido=None, direccion=None, telefono=None):
        cliente: Cliente = self.obtener_cliente(id=id)
        if cliente:
            # cliente
            if nombre:
                cliente.nombre = nombre
            if apellido:
                cliente.apellido = apellido
            if telefono:
                cliente.telefono = telefono
            if direccion:
                cliente.direccion = direccion
            self.db_manager.update(entity=cliente)

    def obtener_cliente(self, id):
        return self.db_manager.get_by_id(entity_class=Cliente, entity_id=id)

    def eliminar_cliente(self, id):
        cliente: Cliente = self.obtener_cliente(id=id)
        if cliente:
            self.db_manager.delete(entity=cliente)

    def listar_clientes(self):
        return self.db_manager.get_all(entity_class=Cliente)
