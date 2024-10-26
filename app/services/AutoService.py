from ..entities.AutoModel import Auto
from ..persistency.DBManager import DBManager

class AutoService:
    def __init__(self):
        self.db_manager = DBManager()
    
    def registrar_auto(self, auto:Auto):
        self.db_manager.register(auto)
        
    def modificar_auto(self, auto:Auto):
        self.db_manager.update(auto)
    
    def eliminar_auto(self, auto:Auto):
        self.db_manager.delete(auto)
    
    def obtener_auto(self, vin):
        return self.db_manager.get_by_id(Auto, vin)
    
    def listar_autos(self):
        autos_source = self.db_manager.get_all(Auto) 
        datos_autos = []
        for auto in autos_source:
            if isinstance(auto, Auto):
                if not (auto.cliente_relacion):
                    tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado_relacion.nombre, None)
                else:
                    tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado_relacion.nombre, f"{auto.cliente_relacion.nombre} {auto.cliente_relacion.apellido}")
                datos_autos.append(tupla)
        return datos_autos
