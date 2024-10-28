# services/VendedorService.py

from ..entities.VendedorModel import Vendedor
from ..persistency.DBManager import DBManager

class VendedorService:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_vendedor(self, vendedor: Vendedor):
        """Registra un nuevo vendedor en la base de datos."""
        self.db_manager.register(vendedor)
        
    def modificar_vendedor(self, vendedor: Vendedor):
        """Modifica un vendedor existente en la base de datos."""
        self.db_manager.update(vendedor)
    
    def eliminar_vendedor(self, vendedor: Vendedor):
        """Elimina un vendedor de la base de datos."""
        self.db_manager.delete(vendedor)
    
    def obtener_vendedor(self, id_vendedor):
        """Obtiene un vendedor específico por ID."""
        return self.db_manager.get_by_id(Vendedor, id_vendedor)
    
    def listar_vendedores(self):
        """Devuelve una lista de todos los vendedores."""
        vendedores = self.db_manager.get_all(Vendedor)
        datos_vendedores = []
        for vendedor in vendedores:
            datos_vendedores.append((
                vendedor.id,
                vendedor.nombre,
                vendedor.apellido,
                vendedor.comisiones
            ))
        return datos_vendedores
