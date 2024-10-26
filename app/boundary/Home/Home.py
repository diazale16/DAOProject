import customtkinter as ctk
from tkinter import ttk
from ...control import GestorAuto
from ..Auto.AdministracionAuto import AdministracionAuto

class Home:
    def __init__(self):    
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.attributes("-fullscreen", True)
        self.initialize_widgets()
        
    def initialize_widgets(self):
        self.adm_autos = ctk.CTkButton(self.root, text="Administrar Auto", command=self.adm_autos).pack(side="top", fill="x", padx=200, pady=20)
        self.adm_clientes = ctk.CTkButton(self.root, text="Administrar Clientes").pack(side="top", fill="x", padx=200, pady=20)
        self.adm_ventas = ctk.CTkButton(self.root, text="Administrar Ventas").pack(side="top", fill="x", padx=200, pady=20)
        self.adm_servicios = ctk.CTkButton(self.root, text="Administrar Servicios").pack(side="top", fill="x", padx=200, pady=20)
    
    def show_home(self):
        self.root.mainloop()
    
    def adm_autos(self):
        adm_autos = AdministracionAuto()
        adm_autos.show()
        