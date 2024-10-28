from ..services.TipoServicioService import TipoServicioService
from ..entities.TipoServicioModel import TipoServicio

class GestorTipoServicio:
    def __init__(self):
        self.tipo_servicio_service = TipoServicioService()

    def registrar_tipo_servicio(self, nombre):
        nuevo_tipo_servicio = TipoServicio(nombre=nombre)
        self.tipo_servicio_service.registrar_tipo_servicio(nuevo_tipo_servicio)
        print("Tipo de servicio registrado con éxito.")

    def modificar_tipo_servicio(self, id_tipo_servicio, nombre=None):
        tipo_servicio = self.tipo_servicio_service.obtener_tipo_servicio(id_tipo_servicio)
        if tipo_servicio:
            if nombre:
                tipo_servicio.nombre = nombre
            self.tipo_servicio_service.modificar_tipo_servicio(tipo_servicio)
            print("Tipo de servicio modificado con éxito.")
    
    def eliminar_tipo_servicio(self, id_tipo_servicio):
        tipo_servicio = self.tipo_servicio_service.obtener_tipo_servicio(id_tipo_servicio)
        if tipo_servicio:
            self.tipo_servicio_service.eliminar_tipo_servicio(tipo_servicio)
            print("Tipo de servicio eliminado con éxito.")
    
    def obtener_tipo_servicio(self, id_tipo_servicio):
        return self.tipo_servicio_service.obtener_tipo_servicio(id_tipo_servicio)
    
    def listar_tipos_servicio(self):
        return self.tipo_servicio_service.listar_tipos_servicio()
