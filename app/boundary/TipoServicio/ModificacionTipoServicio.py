import customtkinter as ctk
from tkinter import ttk
from ...control.GestorTipoServicio import GestorTipoServicio

class ModificacionTipoServicio:
    def __init__(self, adm_tipo_servicio_instance, data):
        self.gestor_tipo_servicio = GestorTipoServicio()
        self.adm_tipo_servicio_instance = adm_tipo_servicio_instance
        self.data = data
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTkToplevel(adm_tipo_servicio_instance.ventana)
        self.ventana.geometry("300x200")
        self.ventana.resizable(False, False)
        self.initialize_modificacion()
        self.create_widgets()
        self.ventana.grab_set()

    def initialize_modificacion(self):
        self.frame_modif = ctk.CTkFrame(self.ventana)
        self.frame_modif.pack(fill="both", expand=True)

    def create_widgets(self):
        # Etiqueta y entrada para el nombre del tipo de servicio
        self.label_nombre = ctk.CTkLabel(self.frame_modif, text="Nombre del Tipo:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_modif)
        self.entry_nombre.insert(0, self.data[1])  # Cargar el nombre actual en el campo de entrada
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        # Botón para modificar el tipo de servicio
        self.boton_modificar = ctk.CTkButton(self.frame_modif, text="Modificar Tipo Servicio", command=self.modificar_tipo_servicio)
        self.boton_modificar.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

    def modificar_tipo_servicio(self):
        nombre = self.entry_nombre.get()

        try:
            self.gestor_tipo_servicio.modificar_tipo_servicio(self.data[0], nombre)
            print("Tipo de servicio modificado con éxito.")
            self.ventana.destroy()
            self.adm_tipo_servicio_instance.rellenar_tabla()  # Refrescar la tabla en la administración
        except Exception as e:
            print(f"Error al modificar el tipo de servicio: {e}")

    def show(self):
        self.ventana.mainloop()
