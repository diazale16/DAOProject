import customtkinter as ctk
from tkinter import ttk
from ...control import Gestor, GestorAuto

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
        # self.adm_clientes = ctk.CTkButton(self.root, text="Administrar Clientes", command=self.adm_clientes).pack(side="left", fill="y", padx=10, pady=50)
        # self.adm_ventas = ctk.CTkButton(self.root, text="Administrar Ventas", command=self.adm_ventas).pack(side="left", fill="y", padx=10, pady=50)
        # self.adm_servicios = ctk.CTkButton(self.root, text="Administrar Servicios", command=self.adm_servicios).pack(side="left", fill="y", padx=10, pady=50)
    
    def show_home(self):
        self.root.mainloop()
    
    def adm_autos(self):
        gestor_alta = GestorAuto.GestorAuto()
        self.root.destroy()
        gestor_alta.registrar_auto()
        