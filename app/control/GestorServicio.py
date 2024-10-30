# control/GestorServicio.py
from datetime import datetime
from ..persistency.DBManager import DBManager
from ..entities.ServicioModel import Servicio
from ..entities.VendedorModel import Vendedor
from ..entities.ComisionModel import Comision
from ..entities.AutoModel import Auto
from ..entities.TipoServicioModel import TipoServicio


class GestorServicio:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_servicio(self, costo, auto: Auto, tipo_servicio: TipoServicio, vendedor: Vendedor):
        # vars
        fecha_servicio = datetime.today().date()  # formato fecha YYYY-MM-DD
        monto_comision = costo * (vendedor.comision / 100)
        monto_servicio = costo - monto_comision
        # servicio
        servicio = Servicio(fecha_servicio=fecha_servicio, costo=monto_servicio,
                            auto_vin=auto.vin, tipo_servicio_id=tipo_servicio.id, vendedor_id=vendedor.id)
        self.db_manager.register(entity=servicio)
        # comision por venta para el vendedor
        comision = Comision(monto=monto_comision,
                            fecha=fecha_servicio, vendedor_id=vendedor.id)
        self.db_manager.register(entity=comision)
        return servicio

    # def modificar_servicio(self, id_servicio, fecha_servicio=None, costo=None, auto_vin=None, tipo_servicio_id=None):
    #     servicio = self.servicio_service.obtener_servicio(id_servicio)
    #     if servicio:
    #         if fecha_servicio:
    #             servicio.fecha_servicio = fecha_servicio
    #         if costo is not None:
    #             servicio.costo = costo
    #         if auto_vin:
    #             servicio.auto_vin = auto_vin
    #         if tipo_servicio_id:
    #             servicio.tipo_servicio_id = tipo_servicio_id
    #         self.servicio_service.modificar_servicio(servicio)

    def obtener_servicio(self, id):
        return self.db_manager.get_by_id(entity_class=Servicio, entity_id=id)

    def eliminar_servicio(self, id):
        servicio: Servicio = self.obtener_servicio(id)
        if servicio:
            self.db_manager.delete(entity=servicio)

    def listar_servicios(self):
        return self.db_manager.get_all(entity_class=Servicio)
