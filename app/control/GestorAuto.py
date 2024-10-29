from ..persistency.DBManager import DBManager
from . import GestorEstado, GestorCliente
from ..entities.AutoModel import Auto
from ..entities.ClienteModel import Cliente


class GestorAuto():
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_auto(self, vin, marca, modelo, año, precio, nom_estado, cliente):
        gestor_estado = GestorEstado.GestorEstado()
        estado = gestor_estado.registrar_estado(nombre_estado=nom_estado)
        auto = Auto(vin=vin, marca=marca, modelo=modelo, año=año,
                    precio=precio, estado_id=estado.id, cliente_id=cliente)
        self.db_manager.register(entity=auto)
        return auto

    def modificar_auto(self, vin, marca, modelo, año, precio, estado, cliente):
        auto: Auto = self.obtener_auto(vin=vin)

        gestor_estado = GestorEstado.GestorEstado()
        gestor_estado.modificar_estado(id=auto.estado_id, nom_estado=estado)

        auto.marca = marca
        auto.modelo = modelo
        auto.año = año
        auto.precio = precio
        # auto.estado_relacion.nombre = estado
        auto.cliente_id = cliente
        self.db_manager.update(entity=auto)

    def obtener_auto(self, vin):
        auto = self.db_manager.get_by_id(entity_class=Auto, entity_id=vin)
        return auto

    def eliminar_auto(self, vin):
        auto = self.obtener_auto(vin=vin)
        self.db_manager.delete(entity=auto)

    def listar_autos(self):
        # autos_source = self.db_manager.get_all(Auto)
        # datos_autos = []
        # for auto in autos_source:
        #     if isinstance(auto, Auto):
        #         if not (auto.cliente_relacion):
        #             tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado_relacion.nombre, "", auto)
        #         else:
        #             tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado_relacion.nombre, auto.cliente_id, auto)
        #             # tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado_relacion.nombre, f"{auto.cliente_relacion.nombre} {auto.cliente_relacion.apellido}", auto)
        #         datos_autos.append(tupla)
        # return datos_autos
        return self.db_manager.get_all(entity_class=Auto)

    def asignar_cliente(self, vin, id):
        auto: Auto = self.db_manager.get_by_id(
            entity_class=Auto, entity_id=vin)
        cliente: Cliente = self.db_manager.get_by_id(
            entity_class=Cliente, entity_id=id)
        auto.cliente_id = cliente.id
        self.db_manager.update(entity=auto)
