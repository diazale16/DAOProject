# control/GestorCliente.py

from ..services.ClienteService import ClienteService
from ..entities.ClienteModel import Cliente

class GestorCliente:
    def __init__(self):
        self.cliente_service = ClienteService()

    def registrar_cliente(self, id, nombre, apellido, direccion, telefono):
        nuevo_cliente = Cliente(id=id, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono)
        self.cliente_service.registrar_cliente(nuevo_cliente)
        print("Cliente registrado con éxito.")
        
    def modificar_cliente(self, id, nombre=None, apellido=None, direccion=None, telefono=None):
        cliente = self.cliente_service.obtener_cliente(id)
        if cliente:
            if nombre:
                cliente.nombre = nombre
            if apellido:
                cliente.apellido = apellido
            if direccion:
                cliente.direccion = direccion
            if telefono:
                cliente.telefono = telefono
            self.cliente_service.modificar_cliente(cliente)
            print("Cliente modificado con éxito.")
    
    def eliminar_cliente(self, id):
        cliente = self.cliente_service.obtener_cliente(id)
        if cliente:
            self.cliente_service.eliminar_cliente(cliente)
            print("Cliente eliminado con éxito.")
    
    def obtener_cliente(self, id):
        return self.cliente_service.obtener_cliente(id)
    
    def listar_clientes(self):
        return self.cliente_service.listar_clientes()
