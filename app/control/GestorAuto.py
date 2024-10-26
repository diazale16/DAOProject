# control/auto_manager.py

# from app.entities.Auto import Auto
# from app.control.DBManager import DBManager
from ..boundary.Auto.AdministracionAuto import AdministracionAuto
from ..entities.AutoModel import Auto
from ..persistency.DBManager import DBManager
from ..services.AutoService import AutoService
from . import Gestor
class GestorAuto():
    def __init__(self):
        self.auto_service = AutoService()

    def registrar_auto(self):
        self.listar_autos()        
        vin, marca, modelo, año, precio, estado, cliente = self.adm_autos.alta()
        auto = Auto(vin=vin, marca=marca, modelo=modelo, año=año, precio=precio, estado=estado, cliente=cliente)    
        self.auto_service.registrar_auto(auto)
        self.home()
        print("añadidoo")
        
    def home(self):
        gestor = Gestor.Gestor()
        gestor.home()
    
    def listar_autos(self):
        autos = self.auto_service.listar_autos()
        self.adm_autos = AdministracionAuto(autos)
        
