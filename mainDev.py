from app.persistency.DBManager import DBManager
from app.control.GestorAuto import GestorAuto
from app.control.Gestor import Gestor
from app.boundary.Home.Home import Home

def main():
    # db_manager = DBManager()
    # print(db_manager)
    # auto_manager = GestorAuto()
    # auto_manager.registrar_auto()
    gestor = Gestor()
    gestor.home()

if __name__ == "__main__":
    main()
