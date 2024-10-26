# control/auto_manager.py

# from app.entities.Auto import Auto
# from app.control.DBManager import DBManager
# from ..boundary.Auto.AdministracionAuto import AdministracionAuto
from ..entities import AutoModel, EstadoModel
from ..services import AutoService, EstadoService
class GestorAuto():
    def __init__(self):
        self.auto_service = AutoService.AutoService()

    def registrar_auto(self, vin, marca, modelo, año, precio, estado, cliente):
        # self.listar_autos()        
        estado = self.registrar_estado(estado)
        auto = AutoModel.Auto(vin=vin, marca=marca, modelo=modelo, año=año, precio=precio, estado_id=estado.id, cliente_id=cliente)    
        self.auto_service.registrar_auto(auto)
        print("añadidoo")
    
    def modificar_auto(self, vin, marca, modelo, año, precio, estado, cliente):
        auto = self.auto_service.obtener_auto(vin)
       
    def obtener_auto(self, vin):
        auto = self.auto_service.obtener_auto(vin)
        return auto

    def eliminar_auto(self, vin):
        auto = self.obtener_auto(vin)
        self.auto_service.eliminar_auto(auto)
        
    def registrar_estado(self, nombre_estado):
        estado = EstadoModel.Estado(nombre=nombre_estado)
        estado_service = EstadoService.EstadoService()
        estado_service.registrar_estado(estado)
        return estado
     
    # def home(self):
    #     gestor = Gestor.Gestor()
    #     gestor.home()
    
    def listar_autos(self):
        autos = self.auto_service.listar_autos()
        return autos
        # self.adm_autos = AdministracionAuto(autos)
        
