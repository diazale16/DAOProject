import customtkinter as ctk
from tkinter import ttk
from ...control import GestorAuto
from ..Auto.AdministracionAuto import AdministracionAuto
from ..Venta.AdministracionVenta import AdministracionVenta
from ..Cliente.AdministracionCliente import AdministracionCliente
from ..Servicio.AdministracionServicio import AdministracionServicio
from ..Reportes.Reportes import Reportes

class Home:
    def __init__(self):    
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTk()
        self.ventana.geometry(f"1280x720")
        ctk.set_appearance_mode("dark")
        self.ventana.attributes("-fullscreen", True)
        self.ventana.bind("<Escape>", self.salir_fullscreen)
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)
        
        self.initialize_widgets()
        
    def initialize_widgets(self):
        self.adm_autos = ctk.CTkButton(self.ventana, text="Administrar Auto", command=self.adm_autos).pack(side="top", fill="x", padx=200, pady=20)
        self.adm_clientes = ctk.CTkButton(self.ventana, text="Administrar Clientes", command=self.adm_clientes).pack(side="top", fill="x", padx=200, pady=20)
        self.adm_ventas = ctk.CTkButton(self.ventana, text="Administrar Ventas", command=self.adm_ventas).pack(side="top", fill="x", padx=200, pady=20)
        self.adm_servicios = ctk.CTkButton(self.ventana, text="Administrar Servicios", command=self.adm_servicios).pack(side="top", fill="x", padx=200, pady=20)
        self.boton_salir = ctk.CTkButton(self.ventana, text="Salir", command=self.salir, fg_color="red").pack(side="bottom", fill="x", padx=200, pady=20)
        self.reportes = ctk.CTkButton(self.ventana, text="Reportes", command=self.reportes_opt).pack(side="bottom", fill="x", padx=200, pady=20)
    
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

    def adm_clientes(self):
        self.ventana.withdraw()
        adm_clientes = AdministracionCliente(self)
        adm_clientes.show()

    def adm_ventas(self):
        self.ventana.withdraw()
        adm_ventas = AdministracionVenta(self)
        adm_ventas.show()

    def adm_servicios(self):
        self.ventana.withdraw()
        adm_servicios = AdministracionServicio(self)
        adm_servicios.show()
        
    def reportes_opt(self):
        self.ventana.withdraw()
        reportes_opt = Reportes(self)
        reportes_opt.show()

