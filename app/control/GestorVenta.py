
from datetime import datetime
from ..persistency.DBManager import DBManager
from . import GestorAuto, GestorComision
from ..entities.VentaModel import Venta
from ..entities.AutoModel import Auto
from ..entities.ClienteModel import Cliente
from ..entities.VendedorModel import Vendedor


class GestorVenta():
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_venta(self, auto: Auto, cliente: Cliente, vendedor: Vendedor, fecha=None):
        # vars
        # fecha = datetime.today().strftime("%d/%m/%Y")
        if not fecha:
            fecha = datetime.today().date()  # formato fecha YYYY-MM-DD

        monto_comision = auto.precio * (vendedor.porc_comision / 100)
        monto_venta = auto.precio - monto_comision

        # reg venta
        venta = Venta(fecha=fecha, auto_vin=auto.vin,
                      cliente_id=cliente.id, vendedor_id=vendedor.id, monto=monto_venta)
        self.db_manager.register(entity=venta)
        # reg comision por venta para el vendedor
        gestor_comision = GestorComision.GestorComision()
        gestor_comision.registrar_comision(monto=monto_comision,
                                                      fecha=fecha, vendedor_id=vendedor.id)
        # asignar auto vendido al cliente
        gestor_autos = GestorAuto.GestorAuto()
        gestor_autos.asignar_cliente(vin=auto.vin, id=cliente.id)
        return venta

    # def modificar_venta(self, vin, marca, modelo, año, precio, estado, cliente):
    #     auto:Auto = self.obtener_venta(vin)

    #     gestor_estado = GestorEstado.GestorEstado()
    #     gestor_estado.modificar_estado(auto.estado_id, estado)

    #     auto.marca = marca
    #     auto.modelo = modelo
    #     auto.año = año
    #     auto.precio = precio
    #     # auto.estado.nombre = estado
    #     auto.cliente_id = cliente
    #     self.db_manager.update(auto)

    def obtener_venta(self, id):
        return self.db_manager.get_by_id(entity_class=Venta, entity_id=id)

    def eliminar_venta(self, id):
        venta: Venta = self.obtener_venta(id=id)
        if venta:
            self.db_manager.delete(entity=venta)

    def listar_ventas(self):
        return self.db_manager.get_all(entity_class=Venta)

    def listar_autos_vendidos(self, id_cliente=None):
        ventas: list[Venta] = self.listar_ventas()
        if id_cliente:
            return [venta.auto for venta in ventas if venta.cliente_id == id_cliente]
        else:
            return [venta.auto for venta in ventas]

    # def listar_autos_vendidos_por_cliente(self, id):
    #     ventas: list[Venta] = self.listar_ventas()
    #     autos_vendidos = [venta.auto for venta in ventas if venta.cliente_id == id]
    #     return autos_vendidos_cliente
