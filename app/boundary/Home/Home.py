import customtkinter as ctk
from tkinter import PhotoImage
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
        self.ventana.attributes("-zoomed", True)
        self.ventana.bind("<Escape>", self.salir_fullscreen)
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)
        
        self.initialize_widgets()
        
    def initialize_widgets(self):
        # Botones de administración
        self.adm_autos = ctk.CTkButton(self.ventana, text="Administrar Auto", command=self.adm_autos)
        self.adm_autos.pack(side="top", fill="x", padx=200, pady=20)

        self.adm_clientes = ctk.CTkButton(self.ventana, text="Administrar Clientes", command=self.adm_clientes)
        self.adm_clientes.pack(side="top", fill="x", padx=200, pady=20)

        self.adm_servicios = ctk.CTkButton(self.ventana, text="Administrar Servicios", command=self.adm_servicios)
        self.adm_servicios.pack(side="top", fill="x", padx=200, pady=20)

        self.adm_vendedores = ctk.CTkButton(self.ventana, text="Administrar Vendedores", command=self.adm_vendedores)
        self.adm_vendedores.pack(side="top", fill="x", padx=200, pady=20)

        self.adm_tipos_servicio = ctk.CTkButton(self.ventana, text="Administrar Tipos de Servicio", command=self.adm_tipos_servicio)
        self.adm_tipos_servicio.pack(side="top", fill="x", padx=200, pady=20)

        # Botón de "Administrar Ventas" con estilo mejorado
        self.adm_ventas = ctk.CTkButton(
            self.ventana, 
            text="Administrar Ventas", 
            command=self.adm_ventas,
            fg_color="#4CAF50",  # Color distintivo para el botón
            hover_color="#388E3C",  # Color al pasar el mouse
            text_color="#FFFFFF",
            height=50,  # Altura del botón
            width=50,  # Ancho del botón
            corner_radius=15  # Bordes redondeados
        )
        self.adm_ventas.pack(side="top", pady=(100, 30), padx=600, fill="x")

        # Botón de salida, en la parte inferior
        self.boton_salir = ctk.CTkButton(self.ventana, text="Salir", command=self.salir, fg_color="red")
        self.boton_salir.pack(side="bottom", pady=20, fill="x", padx=200)
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
    
    # Métodos para abrir las ventanas de administración
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