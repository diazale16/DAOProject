
from datetime import datetime
from ..persistency.DBManager import DBManager
from . import GestorAuto
from ..entities.VentaModel import Venta
from ..entities.AutoModel import Auto
from ..entities.ClienteModel import Cliente
from ..entities.VendedorModel import Vendedor
from ..entities.ComisionModel import Comision
from sqlalchemy import Date


class GestorVenta():
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_venta(self, auto: Auto, cliente: Cliente, vendedor: Vendedor):
        # vars
        # fecha_venta = datetime.today().strftime("%d/%m/%Y")
        fecha_venta = datetime.today().date()  # formato fecha YYYY-MM-DD
        monto_comision = auto.precio * (vendedor.comision / 100)
        monto_venta = auto.precio - monto_comision

        # TODO: preguntar si solo los autos vendidos tienen un cliente
        # reg venta
        venta = Venta(fecha=fecha_venta, auto_vin=auto.vin,
                      cliente_id=cliente.id, vendedor_id=vendedor.id, monto=monto_venta)
        self.db_manager.register(entity=venta)
        # reg comision por venta para el vendedor
        comision = Comision(monto=monto_comision,
                            fecha=fecha_venta, vendedor_id=vendedor.id)
        self.db_manager.register(entity=comision)
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
    #     # auto.estado_relacion.nombre = estado
    #     auto.cliente_id = cliente
    #     self.db_manager.update(auto)

    def obtener_venta(self, id):
        venta = self.db_manager.get_by_id(entity_class=Venta, entity_id=id)
        return venta

    def eliminar_venta(self, id):
        venta = self.obtener_venta(id=id)
        self.db_manager.delete(entity=venta)

    def listar_ventas(self):
        return self.db_manager.get_all(entity_class=Venta)

    def listar_autos_vendidos(self):
        ventas: list[Venta] = self.listar_ventas()
        autos_vendidos = [venta.auto_relacion for venta in ventas]
        return autos_vendidos

    def listar_autos_vendidos_por_cliente(self, id):
        ventas: list[Venta] = self.listar_ventas()
        autos_vendidos_cliente = [venta.auto_relacion for venta in ventas if venta.cliente_id == id]
        return autos_vendidos_cliente