from ..entities import VentaModel
from ..services import VentaService, AutoService

class GestorVenta:
    def __init__(self):
        self.venta_service = VentaService.VentaService()
        self.auto_service = AutoService.AutoService()

    def registrar_venta(self, vin, cliente, vendedor, fecha_venta):
        # Verificar que el auto no haya sido vendido previamente
        auto = self.auto_service.obtener_auto(vin)
        if self.auto_ya_vendido(auto):
            raise Exception("El auto ya ha sido vendido.")

        # Crear la instancia de Venta y registrarla
        venta = VentaModel.Venta(auto_id=auto.id, cliente_id=cliente, vendedor=vendedor, fecha_venta=fecha_venta)
        self.venta_service.registrar_venta(venta)
        print("Venta registrada con éxito.")

    def auto_ya_vendido(self, auto):
        # Comprobar si el auto ya está registrado como vendido
        venta_existente = self.venta_service.obtener_venta_por_auto(auto.id)
        return venta_existente is not None

    def listar_ventas(self):
        # Obtener y devolver todas las ventas registradas
        ventas = self.venta_service.listar_ventas()
        return ventas

    def obtener_venta(self, venta_id):
        # Obtener una venta específica por su ID
        venta = self.venta_service.obtener_venta(venta_id)
        return venta
