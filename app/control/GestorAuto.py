from ..persistency.DBManager import DBManager
from . import GestorEstado, GestorCliente
from ..entities.AutoModel import Auto
from ..entities.ClienteModel import Cliente


class GestorAuto():
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_auto(self, vin, marca, modelo, año, precio, nom_estado, cliente=None):
        auto = self.db_manager.get_by_id(entity_class=Auto, entity_id=vin)
        if auto:
            return
        # estado
        gestor_estado = GestorEstado.GestorEstado()
        estado = gestor_estado.registrar_estado(nombre_estado=nom_estado)
        # auto
        auto = Auto(vin=vin, marca=marca, modelo=modelo, año=año,
                    precio=precio, estado_id=estado.id, cliente_id=cliente)
        self.db_manager.register(entity=auto)
        return auto

    def modificar_auto(self, vin, marca=None, modelo=None, año=None, precio=None, estado=None, cliente=None):
        auto: Auto = self.obtener_auto(vin=vin)
        if auto:
            # estado
            gestor_estado = GestorEstado.GestorEstado()
            gestor_estado.modificar_estado(
                id=auto.estado_id, nom_estado=estado)
            # auto
            if marca:
                auto.marca = marca
            if modelo:
                auto.modelo = modelo
            if año:
                auto.año = año
            if precio:
                auto.precio = precio
            if cliente:
                auto.cliente_id = cliente
            self.db_manager.update(entity=auto)

    def obtener_auto(self, vin):
        return self.db_manager.get_by_id(entity_class=Auto, entity_id=vin)

    def eliminar_auto(self, vin):
        auto: Auto = self.obtener_auto(vin=vin)
        if auto:
            gestor_estado = GestorEstado.GestorEstado()
            gestor_estado.eliminar_estado(id=auto.estado_id)
            self.db_manager.delete(entity=auto)

    def listar_autos(self):
        return self.db_manager.get_all(entity_class=Auto)
    
    def listar_autos_no_vendidos(self):
        return [auto for auto in self.db_manager.get_all(entity_class=Auto) if not auto.venta]

    def asignar_cliente(self, vin, id):
        auto: Auto = self.db_manager.get_by_id(
            entity_class=Auto, entity_id=vin)
        cliente: Cliente = self.db_manager.get_by_id(
            entity_class=Cliente, entity_id=id)
        auto.cliente_id = cliente.id
        self.db_manager.update(entity=auto)
