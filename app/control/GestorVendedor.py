# control/GestorVendedor.py

from ..services.VendedorService import VendedorService
from ..entities.VendedorModel import Vendedor

class GestorVendedor:
    def __init__(self):
        self.vendedor_service = VendedorService()

    def registrar_vendedor(self, nombre, apellido, comisiones=0):
        """Crea un nuevo vendedor y lo registra en la base de datos."""
        nuevo_vendedor = Vendedor(
            nombre=nombre,
            apellido=apellido,
            comisiones=comisiones
        )
        self.vendedor_service.registrar_vendedor(nuevo_vendedor)
        
    def modificar_vendedor(self, id_vendedor, nombre=None, apellido=None, comisiones=None):
        """Modifica la información de un vendedor existente."""
        vendedor = self.vendedor_service.obtener_vendedor(id_vendedor)
        if vendedor:
            if nombre:
                vendedor.nombre = nombre
            if apellido:
                vendedor.apellido = apellido
            if comisiones is not None:
                vendedor.comisiones = comisiones
            self.vendedor_service.modificar_vendedor(vendedor)
    
    def eliminar_vendedor(self, id_vendedor):
        """Elimina un vendedor por su ID."""
        vendedor = self.vendedor_service.obtener_vendedor(id_vendedor)
        if vendedor:
            self.vendedor_service.eliminar_vendedor(vendedor)
    
    def listar_vendedores(self):
        """Obtiene una lista de todos los vendedores."""
        return self.vendedor_service.listar_vendedores()
