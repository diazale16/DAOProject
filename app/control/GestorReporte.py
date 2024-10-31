
from datetime import datetime
from ..persistency.DBManager import DBManager
from . import GestorAuto, GestorVenta, GestorServicio
from ..entities.VentaModel import Venta
from ..entities.ServicioModel import Servicio
from ..entities.AutoModel import Auto
from ..entities.ClienteModel import Cliente
from ..entities.VendedorModel import Vendedor
from ..entities.ComisionModel import Comision
from sqlalchemy import Date


class GestorReporte():
    def __init__(self):
        self.db_manager = DBManager()

    def listar_ventas_periodo(self, fecha_desde:Date, fecha_hasta:Date):
        # listar ventas
        gestor_ventas = GestorVenta.GestorVenta()
        ventas:list[Venta] = gestor_ventas.listar_ventas()
        ventas_en_periodo = [venta for venta in ventas if (venta.fecha >= fecha_desde and venta.fecha <= fecha_hasta)]
        return ventas_en_periodo
    
    def ingresos_totales(self):
        # vars
        ingreso_total = ingreso_ventas = ingreso_servicios = 0
        comisiones = {}
        # ventas
        gestor_ventas = GestorVenta.GestorVenta()
        ventas:list[Venta] = gestor_ventas.listar_ventas()
        for venta in ventas:
            ingreso_ventas += venta.monto
        # servicios
        gestor_servicio = GestorServicio.GestorServicio()
        servicios:list[Servicio] = gestor_servicio.listar_servicios()
        for servicio in servicios:
            ingreso_servicios += servicio.costo
        # total
        ingreso_total = ingreso_ventas + ingreso_servicios
        return ingreso_total, ingreso_ventas, ingreso_servicios


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