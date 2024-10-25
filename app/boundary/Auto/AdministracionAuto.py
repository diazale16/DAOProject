# from app.control.DBManager import DBManager 
# from app.control.GestorAuto import GestorAuto  
from typing import List
import customtkinter as ctk
from tkinter import ttk
from ...entities.AutoModel import Auto

class AltaAuto:
    def __init__(self, autos:list[Auto]):
        self.autos = autos
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTk()
        self.ventana.geometry("1280x720")
        self.ventana.resizable(False, False)
        self.initialize_consulta()
        self.initialize_alta()
        self.initialize_detalle()
        
    def initialize_consulta(self):
        self.frame_lista = ctk.CTkFrame(self.ventana)
        self.frame_lista.pack(side="top", fill="both", expand=True)
        tree = ttk.Treeview(self.frame_lista, columns=("VIN", "Marca", "Modelo", "Año", "Precio", "Estado", "Cliente"), show="headings")
        tree.heading("VIN", text="VIN")
        tree.heading("Marca", text="Marca")
        tree.heading("Modelo", text="Modelo")
        tree.heading("Año", text="Año")
        tree.heading("Precio", text="Precio")
        tree.heading("Estado", text="Estado")
        tree.heading("Cliente", text="Cliente")
        tree.pack(side="center", fill="both", expand=True)
    
    def initialize_alta(self):
        self.frame_alta = ctk.CTkFrame(self.ventana)
        self.frame_alta.pack(side="left", fill="both", expand=True)  
        self.create_widgets_alta()      
        
    def initialize_detalle(self):
        self.frame_detalles = ctk.CTkFrame(self.ventana)
        self.frame_detalles.pack(side="right", fill="both", expand=True)
        tree = ttk.Treeview(self.frame_lista, columns=("VIN", "Marca", "Modelo", "Año", "Precio", "Estado", "Cliente"), show="headings")
        tree.heading("VIN", text="VIN")
        tree.heading("Marca", text="Marca")
        tree.heading("Modelo", text="Modelo")
        tree.heading("Año", text="Año")
        tree.heading("Precio", text="Precio")
        tree.heading("Estado", text="Estado")
        tree.heading("Cliente", text="Cliente")
        tree.pack(side="center", fill="both", expand=True)

    def create_widgets_alta(self):
        self.label_vin = ctk.CTkLabel(self.ventana, text="Código VIN:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_vin = ctk.CTkEntry(self.ventana).grid(row=0, column=1, padx=10, pady=10)
        
        self.label_marca = ctk.CTkLabel(self.ventana, text="Marca:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_marca = ctk.CTkEntry(self.ventana).grid(row=1, column=1, padx=10, pady=10)
        
        self.label_modelo = ctk.CTkLabel(self.ventana, text="Modelo:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_modelo = ctk.CTkEntry(self.ventana).grid(row=2, column=1, padx=10, pady=10)
        
        self.label_año = ctk.CTkLabel(self.ventana, text="Año:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_año = ctk.CTkEntry(self.ventana).grid(row=3, column=1, padx=10, pady=10)
        
        self.label_precio = ctk.CTkLabel(self.ventana, text="Precio:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_precio = ctk.CTkEntry(self.ventana).grid(row=4, column=1, padx=10, pady=10)
        
        self.label_estado = ctk.CTkLabel(self.ventana, text="Estado:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.estado_var = ctk.StringVar(value="Nuevo")
        
        self.radio_nuevo = ctk.CTkRadioButton(self.ventana, text="Nuevo", variable=self.estado_var, value="Nuevo").grid(row=5, column=1, padx=10, pady=10, sticky="w")
        self.radio_usado = ctk.CTkRadioButton(self.ventana, text="Usado", variable=self.estado_var, value="Usado").grid(row=5, column=1, padx=10, pady=10, sticky="e")
        
        self.label_cliente = ctk.CTkLabel(self.ventana, text="Cliente (opcional):").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.entry_cliente = ctk.CTkEntry(self.ventana).grid(row=6, column=1, padx=10, pady=10)
        
        self.boton_registrar = ctk.CTkButton(self.ventana, text="Registrar Auto", command=self.registrar_auto).grid(row=7, column=0, columnspan=2, padx=10, pady=20)

    def registrar_auto(self):
        self.vin = self.entry_vin.get()
        self.marca = self.entry_marca.get()
        self.modelo = self.entry_modelo.get()
        self.año = self.entry_año.get()
        self.precio = self.entry_precio.get()
        self.estado = self.estado_var.get()
        self.cliente = self.entry_cliente.get() if self.entry_cliente.get() else None
        self.ventana.quit()
        
    def alta(self):
        self.ventana.mainloop()
        return self.vin, self.marca, self.modelo, self.año, self.precio, self.estado, self.cliente

# # Ejecutar la interfaz de alta de autos
# if __name__ == "__main__":
#     alta_auto = AltaAuto()
#     alta_auto.alta()