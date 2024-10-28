# control/GestorServicio.py

from ..services.ServicioService import ServicioService
from ..entities.ServicioModel import Servicio

class GestorServicio:
    def __init__(self):
        self.servicio_service = ServicioService()

    def registrar_servicio(self, fecha_servicio, costo, auto_vin, tipo_servicio_id):
        nuevo_servicio = Servicio(
            fecha_servicio=fecha_servicio,
            costo=costo,
            auto_vin=auto_vin,
            tipo_servicio_id=tipo_servicio_id
        )
        self.servicio_service.registrar_servicio(nuevo_servicio)
        
    def modificar_servicio(self, id_servicio, fecha_servicio=None, costo=None, auto_vin=None, tipo_servicio_id=None):
        servicio = self.servicio_service.obtener_servicio(id_servicio)
        if servicio:
            if fecha_servicio:
                servicio.fecha_servicio = fecha_servicio
            if costo is not None:
                servicio.costo = costo
            if auto_vin:
                servicio.auto_vin = auto_vin
            if tipo_servicio_id:
                servicio.tipo_servicio_id = tipo_servicio_id
            self.servicio_service.modificar_servicio(servicio)
    
    def eliminar_servicio(self, id_servicio):
        servicio = self.servicio_service.obtener_servicio(id_servicio)
        if servicio:
            self.servicio_service.eliminar_servicio(servicio)
    
    def listar_servicios(self):
        return self.servicio_service.listar_servicios()
