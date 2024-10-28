import customtkinter as ctk
from tkinter import ttk
from ...control import GestorAuto
from ..Auto.AdministracionAuto import AdministracionAuto
from ..Venta.AdministracionVenta import AdministracionVenta
from ..Cliente.AdministracionCliente import AdministracionCliente  # Importar la administración de clientes
from ..Servicio.AdministracionServicio import AdministracionServicio  # Importar la administración de servicios
from ..Vendedor.AdministracionVendedor import AdministracionVendedor  # Importar la administración de vendedores

class Home:
    def __init__(self):    
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTk()
        
        # Establece la ventana en pantalla completa
        self.ventana.attributes("-fullscreen", True)
        
        # Opción para salir de pantalla completa
        self.ventana.bind("<Escape>", self.salir_fullscreen)

        # Vincula el evento de cierre de la ventana al método salir
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)
        
        self.initialize_widgets()
        
    def initialize_widgets(self):
        self.adm_autos = ctk.CTkButton(self.ventana, text="Administrar Auto", command=self.adm_autos).pack(side="top", fill="x", padx=200, pady=20)
        self.adm_clientes = ctk.CTkButton(self.ventana, text="Administrar Clientes", command=self.adm_clientes).pack(side="top", fill="x", padx=200, pady=20)  # Agregado el botón para clientes
        self.adm_ventas = ctk.CTkButton(self.ventana, text="Administrar Ventas", command=self.adm_ventas).pack(side="top", fill="x", padx=200, pady=20)
        self.adm_servicios = ctk.CTkButton(self.ventana, text="Administrar Servicios", command=self.adm_servicios).pack(side="top", fill="x", padx=200, pady=20)  # Agregado el botón para servicios
        self.adm_vendedores = ctk.CTkButton(self.ventana, text="Administrar Vendedores", command=self.adm_vendedores).pack(side="top", fill="x", padx=200, pady=20)  # Agregado el botón para vendedores
        self.boton_salir = ctk.CTkButton(self.ventana, text="Salir", command=self.salir, fg_color="red").pack(side="bottom", fill="x", padx=200, pady=20)
    
    def show_home(self):
        self.ventana.mainloop()
    
    def salir(self):
        import sys
        sys.exit()
    
    def salir_fullscreen(self, event=None):
        self.ventana.attributes("-fullscreen", False)
        self.ventana.geometry("1280x720")
    
    def adm_autos(self):
        self.ventana.withdraw()
        adm_autos = AdministracionAuto(self)
        adm_autos.show()

    def adm_clientes(self):  # Método para la administración de clientes
        self.ventana.withdraw()
        adm_clientes = AdministracionCliente(self)  # Integrar la administración de clientes
        adm_clientes.show()

    def adm_ventas(self):
        self.ventana.withdraw()
        adm_ventas = AdministracionVenta(self)
        adm_ventas.show()

    def adm_servicios(self):  # Método para la administración de servicios
        self.ventana.withdraw()
        adm_servicios = AdministracionServicio(self)  # Integrar la administración de servicios
        adm_servicios.show()

    def adm_vendedores(self):  # Método para la administración de vendedores
        self.ventana.withdraw()
        adm_vendedores = AdministracionVendedor(self)  # Integrar la administración de vendedores
        adm_vendedores.show()
