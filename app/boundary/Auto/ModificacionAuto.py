import customtkinter as ctk
from ...entities.AutoModel import Auto
from ...control.GestorAuto import GestorAuto

class ModificacionAuto:
    def __init__(self, adm_auto_instance, auto:Auto):
        self.gestor_auto = GestorAuto()
        self.adm_auto_instance = adm_auto_instance
        self.auto = auto
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTkToplevel(adm_auto_instance)
        self.ventana.geometry("300x500")
        self.ventana.resizable(False, False)
        self.initialize_modificacion()
        self.create_widgets()
        self.ventana.grab_set()
    
    def initialize_modificacion(self):
        self.frame_modif = ctk.CTkFrame(self.ventana)
        self.frame_modif.pack(fill="both", expand=True)        

    def create_widgets(self):
        # Etiqueta y entrada para el código VIN
        self.label_vin = ctk.CTkLabel(self.frame_modif, text="Código VIN:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_vin = ctk.CTkEntry(self.frame_modif)
        self.entry_vin.insert(0, self.auto.vin)
        self.entry_vin.configure(state="disabled")
        self.entry_vin.grid(row=0, column=1, padx=10, pady=10)
        # Etiqueta y entrada para la marca
        self.label_marca = ctk.CTkLabel(self.frame_modif, text="Marca:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_marca = ctk.CTkEntry(self.frame_modif)
        self.entry_marca.insert(0, self.auto.marca)
        self.entry_marca.grid(row=1, column=1, padx=10, pady=10)
        # Etiqueta y entrada para el modelo
        self.label_modelo = ctk.CTkLabel(self.frame_modif, text="Modelo:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_modelo = ctk.CTkEntry(self.frame_modif)
        self.entry_modelo.insert(0, self.auto.modelo)
        self.entry_modelo.grid(row=2, column=1, padx=10, pady=10)
        # Etiqueta y entrada para el año
        self.label_año = ctk.CTkLabel(self.frame_modif, text="Año:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_año = ctk.CTkEntry(self.frame_modif)
        self.entry_año.insert(0, self.auto.año)
        self.entry_año.grid(row=3, column=1, padx=10, pady=10)
        # Etiqueta y entrada para el precio
        self.label_precio = ctk.CTkLabel(self.frame_modif, text="Precio:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_precio = ctk.CTkEntry(self.frame_modif)
        self.entry_precio.insert(0, self.auto.precio)
        self.entry_precio.grid(row=4, column=1, padx=10, pady=10)
        # Etiqueta y opción para el estado (nuevo/usado)
        self.label_estado = ctk.CTkLabel(self.frame_modif, text="Estado:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.estado_var = ctk.StringVar(value=f"{self.auto.estado.nombre}")
        self.radio_nuevo = ctk.CTkRadioButton(self.frame_modif, text="Nuevo", variable=self.estado_var, value="Nuevo").grid(row=5, column=1, padx=10, pady=10, sticky="w")
        self.radio_usado = ctk.CTkRadioButton(self.frame_modif, text="Usado", variable=self.estado_var, value="Usado").grid(row=5, column=1, padx=10, pady=10, sticky="e")
        # Etiqueta y entrada para el cliente (opcional)
        self.label_cliente = ctk.CTkLabel(self.frame_modif, text="Cliente (opcional):").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.entry_cliente = ctk.CTkEntry(self.frame_modif)
        if self.auto.cliente_id:
            self.entry_cliente.insert(0, self.auto.cliente_id)
        self.entry_cliente.grid(row=6, column=1, padx=10, pady=10)
        # Botón para registrar el auto
        self.boton_registrar = ctk.CTkButton(self.frame_modif, text="Modificar Auto", command=self.modificar_auto)
        self.boton_registrar.grid(row=7, column=0, columnspan=2, padx=10, pady=20)

    def modificar_auto(self):
        self.vin = self.entry_vin.get()
        self.marca = self.entry_marca.get()
        self.modelo = self.entry_modelo.get()
        self.año = self.entry_año.get()
        self.precio = self.entry_precio.get()
        self.estado = self.estado_var.get()
        self.cliente_id = self.entry_cliente.get() if self.entry_cliente.get() else None
        self.gestor_auto.modificar_auto(self.vin, self.marca, self.modelo, self.año, self.precio, self.estado, self.cliente_id)
        self.ventana.destroy()
        
    def show(self):
        self.ventana.mainloop()