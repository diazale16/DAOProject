# GestorVenta.py
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

    def validar_ids(self, cliente_id, vendedor_id, vin):
        cliente = self.db_manager.get_by_id(entity_class=Cliente, entity_id=cliente_id)
        vendedor = self.db_manager.get_by_id(entity_class=Vendedor, entity_id=vendedor_id)
        auto = self.db_manager.get_by_id(entity_class=Auto, entity_id=vin)

        if not cliente:
            raise ValueError(f"No se encontró un cliente con el ID '{cliente_id}'.")
        if not vendedor:
            raise ValueError(f"No se encontró un vendedor con el ID '{vendedor_id}'.")
        if not auto:
            raise ValueError(f"No se encontró un auto con el VIN '{vin}'.")
        
        return cliente, vendedor, auto

    def registrar_venta(self, cliente_id, vendedor_id, vin, fecha_venta=None):
        # Validar los IDs antes de registrar la venta
        cliente, vendedor, auto = self.validar_ids(cliente_id, vendedor_id, vin)
        
        # Utilizar la fecha proporcionada, o la fecha actual si no se especifica
        fecha_venta = fecha_venta if fecha_venta else datetime.today().date()
        monto_comision = auto.precio * (vendedor.comision / 100)
        monto_venta = auto.precio - monto_comision

        # Registrar venta
        venta = Venta(fecha=fecha_venta, auto_vin=auto.vin,
                      cliente_id=cliente.id, vendedor_id=vendedor.id, monto=monto_venta)
        self.db_manager.register(entity=venta)

        # Registrar comisión por venta para el vendedor
        comision = Comision(monto=monto_comision,
                            fecha=fecha_venta, vendedor_id=vendedor.id)
        self.db_manager.register(entity=comision)

        # Asignar auto vendido al cliente
        gestor_autos = GestorAuto.GestorAuto()
        gestor_autos.asignar_cliente(vin=auto.vin, id=cliente.id)

        return venta

    def modificar_venta(self, venta_id, fecha, cliente_id, vendedor_id):
        # Obtener la venta que se va a modificar
        venta = self.obtener_venta(venta_id)
        if venta:
            venta.fecha = fecha
            venta.cliente_id = cliente_id
            venta.vendedor_id = vendedor_id
            self.db_manager.update(venta)
        else:
            raise ValueError("Venta no encontrada")

    def obtener_venta(self, id):
        return self.db_manager.get_by_id(entity_class=Venta, entity_id=id)

    def eliminar_venta(self, id):
        venta:Venta = self.obtener_venta(id=id)
        if venta:
            self.db_manager.delete(entity=venta)

    def listar_ventas(self):
        return self.db_manager.get_all(entity_class=Venta)

    def listar_autos_vendidos(self, id_cliente=None):
        ventas: list[Venta] = self.listar_ventas()
        if id_cliente:
            return [venta.auto_relacion for venta in ventas if venta.cliente_id == id_cliente]
        else:
            return [venta.auto_relacion for venta in ventas]


    # def listar_autos_vendidos_por_cliente(self, id):
    #     ventas: list[Venta] = self.listar_ventas()
    #     autos_vendidos = [venta.auto_relacion for venta in ventas if venta.cliente_id == id]
    #     return autos_vendidos_cliente