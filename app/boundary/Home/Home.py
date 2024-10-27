import customtkinter as ctk
from tkinter import ttk
from ...control import GestorAuto
from ..Auto.AdministracionAuto import AdministracionAuto

class Home:
    def __init__(self):    
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTk()
        
        self.ventana.geometry(f"1280x720")
        self.ventana.attributes("-zoomed", True)
        self.initialize_widgets()
        
    def initialize_widgets(self):
        self.adm_autos = ctk.CTkButton(self.ventana, text="Administrar Auto", command=self.adm_autos).pack(side="top", fill="x", padx=200, pady=20)
        self.adm_clientes = ctk.CTkButton(self.ventana, text="Administrar Clientes").pack(side="top", fill="x", padx=200, pady=20)
        self.adm_ventas = ctk.CTkButton(self.ventana, text="Administrar Ventas").pack(side="top", fill="x", padx=200, pady=20)
        self.adm_servicios = ctk.CTkButton(self.ventana, text="Administrar Servicios").pack(side="top", fill="x", padx=200, pady=20)
        self.adm_servicios = ctk.CTkButton(self.ventana, text="Salir", command=self.salir, fg_color="red").pack(side="bottom", fill="x", padx=200, pady=20)
    
    def show_home(self):
        self.ventana.mainloop()
    
    def salir(self):
        import sys
        sys.exit()
    
    def adm_autos(self):
        self.ventana.withdraw()
        adm_autos = AdministracionAuto(self)
        adm_autos.show()
        