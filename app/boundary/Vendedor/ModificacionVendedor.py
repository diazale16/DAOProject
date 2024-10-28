# boundary/Vendedor/ModificacionVendedor.py

import customtkinter as ctk
from tkinter import ttk
from ...control.GestorVendedor import GestorVendedor

class ModificacionVendedor:
    def __init__(self, adm_vendedor_instance, data):
        self.gestor_vendedor = GestorVendedor()
        self.adm_vendedor_instance = adm_vendedor_instance
        self.data = data
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTkToplevel(adm_vendedor_instance.ventana)
        self.ventana.geometry("300x400")
        self.ventana.resizable(False, False)
        self.initialize_modificacion()
        self.create_widgets()
        self.ventana.grab_set()

    def initialize_modificacion(self):
        self.frame_modif = ctk.CTkFrame(self.ventana)
        self.frame_modif.pack(fill="both", expand=True)

    def create_widgets(self):
        self.label_nombre = ctk.CTkLabel(self.frame_modif, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_modif)
        self.entry_nombre.insert(0, self.data[1])
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_telefono = ctk.CTkLabel(self.frame_modif, text="Teléfono:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_telefono = ctk.CTkEntry(self.frame_modif)
        self.entry_telefono.insert(0, self.data[2])
        self.entry_telefono.grid(row=1, column=1, padx=10, pady=10)

        self.label_email = ctk.CTkLabel(self.frame_modif, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_email = ctk.CTkEntry(self.frame_modif)
        self.entry_email.insert(0, self.data[3])
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        self.label_ventas = ctk.CTkLabel(self.frame_modif, text="Ventas:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_ventas = ctk.CTkEntry(self.frame_modif)
        self.entry_ventas.insert(0, self.data[4])
        self.entry_ventas.grid(row=3, column=1, padx=10, pady=10)

        self.boton_modificar = ctk.CTkButton(self.frame_modif, text="Modificar Vendedor", command=self.modificar_vendedor)
        self.boton_modificar.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

    def modificar_vendedor(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        email = self.entry_email.get()
        ventas = self.entry_ventas.get()

        try:
            self.gestor_vendedor.modificar_vendedor(self.data[0], nombre, telefono, email, ventas)
            print("Vendedor modificado con éxito.")
            self.ventana.destroy()
            self.adm_vendedor_instance.rellenar_tabla()
        except Exception as e:
            print(f"Error al modificar el vendedor: {e}")

    def show(self):
        self.ventana.mainloop()
