from app.entities import (
    AutoModel,
    ClienteModel,
    DireccionModel,
    EstadoModel,
    ServicioModel,
    TipoServicioModel,
    VendedorModel,
    VentaModel,
)
from app.services import (
    AutoService,
    # ClienteService,
    # DireccionService,
    # ServicioService,
    # TipoServicioService,
    # VendedorService,
    # VentaService,
    EstadoService,
)
from app.persistency.DBManager import DBManager

import random

# VARS
#autos
marca = [
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
marca_modelo = {
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
vin_codes = [
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

def main():
    # Servicios
    auto_service = AutoService.AutoService()
    estado_service = EstadoService.EstadoService()

    # Auto
    sup_limit = len(vin_codes)
    for i in range(sup_limit):
        rand1 = random.randint(0, sup_limit-1)
        rand2 = random.randint(0, 2)
        estado = EstadoModel.Estado(nombre="Nuevo" if i%2 == 0 else "Usado")
        estado_service.registrar_estado(estado)
        
        auto = AutoModel.Auto(
            vin=vin_codes[i],
            marca=marca[rand1],
            modelo=marca_modelo[marca[rand1]][rand2],
            año=random.randint(1970, 2023),
            precio=random.randrange(5000000, 20000000, 1),
            estado_id=estado.id,
            cliente_id=None,
        )
        auto_service.registrar_auto(auto)
        
    listado_autos = auto_service.listar_autos()
    print()

main()
