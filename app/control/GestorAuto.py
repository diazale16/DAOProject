# control/auto_manager.py

# from app.entities.Auto import Auto
# from app.control.DBManager import DBManager
from ..boundary.Auto.AltaAuto import AltaAuto
from ..entities.AutoModel import Auto
from ..persistency.DBManager import DBManager
from ..services.AutoService import AutoService

class GestorAuto:
    def __init__(self):
        pass
        # self.db_manager = DBManager()

    def registrar_auto(self):    
            
        auto_service = AutoService()
        auto_service.registrar_auto()
        print("añadidoo")
        # session.add(auto)
        # session.commit()
        # session.close()
