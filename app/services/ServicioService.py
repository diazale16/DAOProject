# services/ServicioService.py

from ..entities.ServicioModel import Servicio
from ..persistency.DBManager import DBManager

class ServicioService:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_servicio(self, servicio: Servicio):
        self.db_manager.register(servicio)
        
    def modificar_servicio(self, servicio: Servicio):
        self.db_manager.update(servicio)
    
    def eliminar_servicio(self, servicio: Servicio):
        self.db_manager.delete(servicio)
    
    def obtener_servicio(self, id_servicio):
        return self.db_manager.get_by_id(Servicio, id_servicio)
    
    def listar_servicios(self):
        servicios = self.db_manager.get_all(Servicio)
        datos_servicios = []
        for servicio in servicios:
            datos_servicios.append((
                servicio.id, 
                servicio.fecha_servicio, 
                servicio.costo, 
                servicio.auto_vin, 
                servicio.tipo_servicio_id
            ))
        return datos_servicios
