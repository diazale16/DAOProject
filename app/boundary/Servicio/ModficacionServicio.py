# boundary/Servicio/ModificacionServicio.py

import customtkinter as ctk
from tkinter import ttk
from ...control.GestorServicio import GestorServicio

class ModificacionServicio:
    def __init__(self, adm_servicio_instance, data):
        self.gestor_servicio = GestorServicio()
        self.adm_servicio_instance = adm_servicio_instance
        self.data = data
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTkToplevel(adm_servicio_instance.ventana)
        self.ventana.geometry("300x400")
        self.ventana.resizable(False, False)
        self.initialize_modificacion()
        self.create_widgets()
        self.ventana.grab_set()

    def initialize_modificacion(self):
        self.frame_modif = ctk.CTkFrame(self.ventana)
        self.frame_modif.pack(fill="both", expand=True)

    def create_widgets(self):
        self.label_fecha = ctk.CTkLabel(self.frame_modif, text="Fecha:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_fecha = ctk.CTkEntry(self.frame_modif)
        self.entry_fecha.insert(0, self.data[1])
        self.entry_fecha.grid(row=0, column=1, padx=10, pady=10)

        self.label_auto_vin = ctk.CTkLabel(self.frame_modif, text="Auto VIN:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_auto_vin = ctk.CTkEntry(self.frame_modif)
        self.entry_auto_vin.insert(0, self.data[2])
        self.entry_auto_vin.grid(row=1, column=1, padx=10, pady=10)

        self.label_tipo_servicio = ctk.CTkLabel(self.frame_modif, text="Tipo Servicio:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_tipo_servicio = ctk.CTkEntry(self.frame_modif)
        self.entry_tipo_servicio.insert(0, self.data[3])
        self.entry_tipo_servicio.grid(row=2, column=1, padx=10, pady=10)

        self.label_costo = ctk.CTkLabel(self.frame_modif, text="Costo:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_costo = ctk.CTkEntry(self.frame_modif)
        self.entry_costo.insert(0, self.data[4])
        self.entry_costo.grid(row=3, column=1, padx=10, pady=10)

        self.boton_modificar = ctk.CTkButton(self.frame_modif, text="Modificar Servicio", command=self.modificar_servicio)
        self.boton_modificar.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

    def modificar_servicio(self):
        fecha = self.entry_fecha.get()
        auto_vin = self.entry_auto_vin.get()
        tipo_servicio = self.entry_tipo_servicio.get()
        costo = self.entry_costo.get()

        try:
            self.gestor_servicio.modificar_servicio(self.data[0], fecha, costo, auto_vin, tipo_servicio)
            print("Servicio modificado con éxito.")
            self.ventana.destroy()
            self.adm_servicio_instance.rellenar_tabla()
        except Exception as e:
            print(f"Error al modificar el servicio: {e}")

    def show(self):
        self.ventana.mainloop()
