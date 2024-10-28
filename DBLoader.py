from app.entities import (
    AutoModel,
    ClienteModel,
    # DireccionModel,
    EstadoModel,
    ServicioModel,
    TipoServicioModel,
    VendedorModel,
    VentaModel,
)
from app.control import (
    GestorAuto,
    GestorCliente,
    # GestorDireccion,
    # GestorServicio,
    # GestorTipoServicio,
    # GestorVendedor,
    GestorVenta,
    GestorEstado,
)
from app.persistency.DBManager import DBManager
import random

# global db manager
db_manager = DBManager()

# VARS
#autos
MARCAS = [
    "Toyota",
    "Ford",
    "Chevrolet",
    "Honda",
    "Nissan",
    "Volkswagen",
    "BMW",
    "Mercedes-Benz",
    "Audi",
    "Hyundai",
    "Kia",
    "Mazda",
    "Subaru",
    "Lexus",
    "Jaguar",
    "Porsche",
    "Ferrari",
    "Lamborghini",
    "Tesla",
    "Mitsubishi",
]
MARCA_MODELOS = {
    "Toyota": ["Corolla", "Camry", "RAV4"],
    "Ford": ["Fiesta", "Focus", "Mustang"],
    "Chevrolet": ["Spark", "Malibu", "Equinox"],
    "Honda": ["Civic", "Accord", "CR-V"],
    "Nissan": ["Sentra", "Altima", "X-Trail"],
    "Volkswagen": ["Golf", "Passat", "Tiguan"],
    "BMW": ["Series 3", "Series 5", "X5"],
    "Mercedes-Benz": ["C-Class", "E-Class", "GLC"],
    "Audi": ["A3", "A4", "Q5"],
    "Hyundai": ["Elantra", "Sonata", "Tucson"],
    "Kia": ["Rio", "Forte", "Sorento"],
    "Mazda": ["Mazda3", "Mazda6", "CX-5"],
    "Subaru": ["Impreza", "Outback", "Forester"],
    "Lexus": ["IS", "ES", "RX"],
    "Jaguar": ["XE", "XF", "F-Pace"],
    "Porsche": ["Cayenne", "Macan", "911"],
    "Ferrari": ["488", "F8", "Portofino"],
    "Lamborghini": ["Huracan", "Aventador", "Urus"],
    "Tesla": ["Model S", "Model 3", "Model X"],
    "Mitsubishi": ["Mirage", "Outlander", "Eclipse Cross"],
}
VIN_CODES = [
    "1HGCM82633A123456",
    "JH4KA9650MC012345",
    "2T1BU4EE9DC123456",
    "WBA3A5C51DF123456",
    "4T1BF1FK9EU123456",
    "1FAHP2E85EG123456",
    "3VW2K7AJ5DM123456",
    "JM1BL1VG8D1123456",
    "3N1AB7AP7HY123456",
    "2HGFB2F57DH123456",
    "1C4RJFAG9FC123456",
    "5UXWX9C56F0D12345",
    "1FTFW1EF1EKD12345",
    "2C3CCARG1EH123456",
    "1G6AB5SX0D0123456",
    "SALGS2TFXEA123456",
    "5NPEB4AC5DH123456",
    "WAUHGAFC6DN123456",
    "JN8AS5MVXDW123456",
    "KM8JT3AB6EU123456",
]
NOMBRES = [
    "Alejandro",
    "Beatriz",
    "Carlos",
    "Daniela",
    "Eduardo",
    "Fernanda",
    "Gabriel",
    "Helena",
    "Ignacio",
    "Juliana",
    "Kevin",
    "Laura",
    "Manuel",
    "Natalia",
    "Óscar",
    "Patricia",
    "Rafael",
    "Sofía",
    "Tomás",
    "Valentina"
]
APELLIDOS = [
    "González",
    "Rodríguez",
    "Pérez",
    "López",
    "Martínez",
    "Sánchez",
    "García",
    "Romero",
    "Torres",
    "Díaz",
    "Hernández",
    "Castro",
    "Mendoza",
    "Ríos",
    "Vargas",
    "Silva",
    "Medina",
    "Jiménez",
    "Ortega",
    "Cruz"
]
DIRECCIONES = [
    "Calle 1, No. 123",
    "Avenida Central, No. 456",
    "Calle 10, No. 789",
    "Boulevard de la Paz, No. 101",
    "Calle del Sol, No. 202",
    "Calle de la Luna, No. 303",
    "Avenida del Libertador, No. 404",
    "Calle 15, No. 505",
    "Avenida Principal, No. 606",
    "Calle 5, No. 707",
    "Calle del Río, No. 808",
    "Calle de los Jardines, No. 909",
    "Calle 20, No. 111",
    "Calle de la Esperanza, No. 121",
    "Avenida de los Olivos, No. 131",
    "Calle 7, No. 141",
    "Calle de la Amistad, No. 151",
    "Avenida del Parque, No. 161",
    "Calle 3, No. 171",
    "Calle de la Libertad, No. 181"
]


def main():
    # Gestores
    auto_gestor = GestorAuto.GestorAuto()
    estado_gestor = GestorEstado.GestorEstado()
    cliente_gestor = GestorCliente.GestorCliente()
    venta_gestor = GestorVenta.GestorVenta()

    
    sup_limit = len(VIN_CODES)
    for i in range(sup_limit):
        rand1 = lambda:random.randint(0, sup_limit-1)
        rand2 = lambda:random.randint(0, 2)
        
        # Estados
        nom_estado = "Nuevo" if i%2 == 0 else "Usado"
        # estado = estado_gestor.registrar_estado(nom_estado)
       
        # Auto
        vin=VIN_CODES[i]
        marca=MARCAS[rand1()]
        modelo=MARCA_MODELOS[MARCAS[rand1()]][rand2()]
        año=random.randint(1970, 2023)
        precio=random.randrange(5000000, 20000000, 1)
        auto:AutoModel.Auto = auto_gestor.registrar_auto(vin=vin, marca=marca, modelo=modelo, año=año, precio=precio, nom_estado=nom_estado, cliente=None)
        
        if i%2 == 0:
            # Vendedores
            nom_vend = NOMBRES[rand1()]
            apell_vend = APELLIDOS[rand1()]
            comision = random.randint(1,25)
            vendedor = VendedorModel.Vendedor(nombre=nom_vend, apellido=apell_vend, comision=comision)
            db_manager.register(vendedor)
        
        if i%3 == 0:
            # Clientes
            nom_cli = NOMBRES[rand1()]
            apell_cli = APELLIDOS[rand1()]
            telefono = random.randint(3000000000, 3900000000)
            direccion = DIRECCIONES[i]
            cliente:ClienteModel.Cliente = cliente_gestor.registrar_cliente(nombre=nom_cli, apellido=apell_cli, telefono=telefono, direccion=direccion)
            
            # Venta
            # fecha = Column(Date, nullable=False)
            # auto_vin = Column(String, ForeignKey('autos.vin'), nullable=False)
            # cliente_id = Column(String, ForeignKey('clientes.id'), nullable=False)
            # vendedor_id = Column(String, ForeignKey('vendedores.id'), nullable=False)
            # monto = Column(Float, nullable=False)
            venta:VentaModel.Vendedor = venta_gestor.registrar_venta(auto=auto, cliente=cliente, vendedor=vendedor)
            
            # auto_gestor.asignar_cliente(auto.vin, cliente.id)

main()
