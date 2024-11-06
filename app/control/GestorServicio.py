# control/GestorServicio.py
from datetime import datetime
from ..persistency.DBManager import DBManager
from ..entities.ServicioModel import Servicio
from ..entities.VendedorModel import Vendedor
from ..entities.ComisionModel import Comision
from ..entities.AutoModel import Auto
from . import GestorComision
from ..entities.TipoServicioModel import TipoServicio
from . import GestorAuto
from . import GestorTipoServicio
from . import GestorVendedor


class GestorServicio:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_servicio(self, costo: float, auto_vin , tipo_servicio, vendedor_id: Vendedor, fecha=None):
        # vars
        if not fecha:
            fecha = datetime.today().date()  # formato fecha YYYY-MM-DD
        else:
            fecha = datetime.strptime(fecha, '%Y-%m-%d').date()

        gestor_vendedor = GestorVendedor.GestorVendedor()
        vendedor = gestor_vendedor.obtener_vendedor(vendedor_id)

        monto_comision = costo * (vendedor.porc_comision / 100)
        monto_servicio = costo - monto_comision
        #auto
        gestor_auto = GestorAuto.GestorAuto()
        auto = gestor_auto.obtener_auto(vin=auto_vin)
        #tipo servicio
        gestor_servicio = GestorTipoServicio.GestorTipoServicio()
        tipo = gestor_servicio.registrar_tipo_servicio(tipo_servicio)

        # servicio
        servicio = Servicio(fecha=fecha, costo=monto_servicio,
                            auto_vin=auto.vin, tipo_servicio_id=tipo.id, vendedor_id=vendedor.id)
        self.db_manager.register(entity=servicio)
 

        # reg comision por venta para el vendedor
        gestor_comision = GestorComision.GestorComision()
        gestor_comision.registrar_comision(
            monto=monto_comision, fecha=fecha, vendedor_id=vendedor.id)
        return servicio

    # def modificar_servicio(self, id_servicio, fecha=None, costo=None, auto_vin=None, tipo_servicio_id=None):
    #     servicio = self.servicio_service.obtener_servicio(id_servicio)
    #     if servicio:
    #         if fecha:
    #             servicio.fecha = fecha
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
    
    def obtener_servicios_por_auto(self, auto_vin):
        # Consulta para obtener todos los servicios que están asociados al auto VIN
        servicios = self.db_manager.get_session().query(Servicio).filter(Servicio.auto_vin == auto_vin).all()

        return servicios