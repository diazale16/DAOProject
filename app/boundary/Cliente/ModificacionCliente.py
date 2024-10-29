import customtkinter as ctk
from tkinter import ttk
from ...control.GestorCliente import GestorCliente

class ModificacionCliente:
    def __init__(self, adm_cliente_instance, data):
        self.gestor_cliente = GestorCliente()
        self.adm_cliente_instance = adm_cliente_instance
        self.data = data
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTkToplevel(adm_cliente_instance)
        self.ventana.geometry("400x400")
        self.ventana.resizable(False, False)
        self.initialize_modificacion()
        self.create_widgets()
        self.ventana.grab_set()

    def initialize_modificacion(self):
        self.frame_modif = ctk.CTkFrame(self.ventana)
        self.frame_modif.pack(fill="both", expand=True)

    def create_widgets(self):
        # Etiqueta y entrada para el ID (no modificable)
        self.label_id = ctk.CTkLabel(self.frame_modif, text="ID:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_id = ctk.CTkEntry(self.frame_modif, state='disabled')
        self.entry_id.insert(0, self.data[0])
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y entrada para el nombre
        self.label_nombre = ctk.CTkLabel(self.frame_modif, text="Nombre:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_modif)
        self.entry_nombre.insert(0, self.data[1])
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        # Etiqueta y entrada para el apellido
        self.label_apellido = ctk.CTkLabel(self.frame_modif, text="Apellido:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_apellido = ctk.CTkEntry(self.frame_modif)
        self.entry_apellido.insert(0, self.data[2])
        self.entry_apellido.grid(row=2, column=1, padx=10, pady=10)

        # Etiqueta y entrada para la dirección
        self.label_direccion = ctk.CTkLabel(self.frame_modif, text="Dirección:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_direccion = ctk.CTkEntry(self.frame_modif)
        self.entry_direccion.insert(0, self.data[3])
        self.entry_direccion.grid(row=3, column=1, padx=10, pady=10)

        # Etiqueta y entrada para el teléfono
        self.label_telefono = ctk.CTkLabel(self.frame_modif, text="Teléfono:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_telefono = ctk.CTkEntry(self.frame_modif)
        self.entry_telefono.insert(0, self.data[4])
        self.entry_telefono.grid(row=4, column=1, padx=10, pady=10)

        # Botón para modificar el cliente
        self.boton_modificar = ctk.CTkButton(self.frame_modif, text="Modificar Cliente", command=self.modificar_cliente)
        self.boton_modificar.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

    def modificar_cliente(self):
        id_cliente = self.entry_id.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()

        # Llamada al gestor para modificar el cliente
        self.gestor_cliente.modificar_cliente(id_cliente, nombre, apellido, direccion, telefono)
        print("Cliente modificado con éxito.")
        self.ventana.destroy()
        self.adm_cliente_instance.rellenar_tabla()  # Refrescar la tabla de clientes

    def show(self):
        self.ventana.mainloop()