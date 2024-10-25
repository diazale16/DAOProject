# from app.control.DBManager import DBManager 
# from app.control.GestorAuto import GestorAuto  
import customtkinter as ctk
from tkinter import ttk
from ...entities.AutoModel import Auto

class ModificacionAuto:
    def __init__(self, auto:Auto):
        self.auto = auto
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTk()
        self.ventana.geometry("480x720")
        self.ventana.resizable(False, False)
        self.initialize_modificacion()
        self.create_widgets(auto)
    
    def initialize_modificacion(self):
        self.frame_alta = ctk.CTkFrame(self.ventana)
        self.frame_alta.pack(side="left", fill="both", expand=True)        

    def create_widgets(self, auto:Auto):
        # Etiqueta y entrada para el código VIN
        self.label_vin = ctk.CTkLabel(self.ventana, text="Código VIN:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_vin = ctk.CTkEntry(self.ventana, textvariable=auto.vin)
        self.entry_vin.grid(row=0, column=1, padx=10, pady=10)
        # Etiqueta y entrada para la marca
        self.label_marca = ctk.CTkLabel(self.ventana, text="Marca:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_marca = ctk.CTkEntry(self.ventana, textvariable=auto.marca)
        self.entry_marca.grid(row=1, column=1, padx=10, pady=10)
        # Etiqueta y entrada para el modelo
        self.label_modelo = ctk.CTkLabel(self.ventana, text="Modelo:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_modelo = ctk.CTkEntry(self.ventana, textvariable=auto.modelo)
        self.entry_modelo.grid(row=2, column=1, padx=10, pady=10)
        # Etiqueta y entrada para el año
        self.label_año = ctk.CTkLabel(self.ventana, text="Año:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_año = ctk.CTkEntry(self.ventana, textvariable=auto.año)
        self.entry_año.grid(row=3, column=1, padx=10, pady=10)
        # Etiqueta y entrada para el precio
        self.label_precio = ctk.CTkLabel(self.ventana, text="Precio:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_precio = ctk.CTkEntry(self.ventana, textvariable=auto.precio)
        self.entry_precio.grid(row=4, column=1, padx=10, pady=10)
        # Etiqueta y opción para el estado (nuevo/usado)
        self.label_estado = ctk.CTkLabel(self.ventana, text="Estado:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.estado_var = ctk.StringVar(value=f"{auto.estado_relacion.nombre}")
        self.radio_nuevo = ctk.CTkRadioButton(self.ventana, text="Nuevo", variable=self.estado_var, value="Nuevo").grid(row=5, column=1, padx=10, pady=10, sticky="w")
        self.radio_usado = ctk.CTkRadioButton(self.ventana, text="Usado", variable=self.estado_var, value="Usado").grid(row=5, column=1, padx=10, pady=10, sticky="e")
        # Etiqueta y entrada para el cliente (opcional)
        self.label_cliente = ctk.CTkLabel(self.ventana, text="Cliente (opcional):").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.entry_cliente = ctk.CTkEntry(self.ventana, textvariable=auto.cliente_relacion.id)
        self.entry_cliente.grid(row=6, column=1, padx=10, pady=10)
        # Botón para registrar el auto
        self.boton_registrar = ctk.CTkButton(self.ventana, text="Modificar Auto", command=self.modificar_auto)
        self.boton_registrar.grid(row=7, column=0, columnspan=2, padx=10, pady=20)

    def modificar_auto(self):
        self.vin = self.entry_vin.get()
        self.marca = self.entry_marca.get()
        self.modelo = self.entry_modelo.get()
        self.año = self.entry_año.get()
        self.precio = self.entry_precio.get()
        self.estado = self.estado_var.get()
        self.cliente = self.entry_cliente.get() if self.entry_cliente.get() else None
        self.ventana.quit()
        
    def modificacion(self):
        self.ventana.mainloop()
        return self.vin, self.marca, self.modelo, self.año, self.precio, self.estado, self.cliente

# # Ejecutar la interfaz de alta de autos
# if __name__ == "__main__":
#     alta_auto = AltaAuto()
#     alta_auto.alta()