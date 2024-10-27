from ..entities.VentaModel import Venta
from ..persistency.DBManager import DBManager

class VentaService:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_venta(self, venta: Venta):
        self.db_manager.register(venta)

    def modificar_venta(self, venta: Venta):
        self.db_manager.update(venta)

    def eliminar_venta(self, venta: Venta):
        self.db_manager.delete(venta)

    def obtener_venta(self, venta_id):
        return self.db_manager.get_by_id(Venta, venta_id)

    def listar_ventas(self):
        ventas_source = self.db_manager.get_all(Venta)
        datos_ventas = []
        for venta in ventas_source:
            if isinstance(venta, Venta):
                tupla = (venta.id, venta.fecha, venta.monto_total, f"{venta.cliente_relacion.nombre} {venta.cliente_relacion.apellido}")
                datos_ventas.append(tupla)
        return datos_ventas
