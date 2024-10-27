import customtkinter as ctk
from tkinter import ttk
from ...control.GestorCliente import GestorCliente
from . import ModificacionCliente

class AdministracionCliente:
    def __init__(self, home_instance):
        self.gestor_cliente = GestorCliente()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()
        
        self.ventana.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        self.ventana.attributes("-zoomed", True)
        
        self.header()
        self.initialize_consulta()
        self.initialize_alta()
        
    def home(self):
        self.ventana.destroy()
        self.home_instance.ventana.deiconify()
        
    def show(self):
        self.ventana.mainloop()

    def header(self):
        line1_frame = ctk.CTkFrame(self.ventana)
        line1_frame.pack(side="top", fill="x", pady=5)
        
        # Botón para volver a la pantalla principal
        self.boton_home = ctk.CTkButton(line1_frame, text="Home", command=self.home)
        self.boton_home.pack(side="left", fill="y")
        
        # Botón para refrescar la lista de clientes
        self.boton_refrescar = ctk.CTkButton(line1_frame, text="Refrescar", command=self.rellenar_tabla)
        self.boton_refrescar.pack(side="right", fill="y")

    def initialize_consulta(self):
        self.frame_lista = ctk.CTkFrame(self.ventana)
        self.frame_lista.pack(side="top", fill="both", padx=10, pady=10, expand=True)
        
        # Configuración de la tabla de clientes
        self.tree = ttk.Treeview(
            self.frame_lista,
            columns=("ID", "Nombre", "Apellido", "Email", "Telefono"),
            show="headings",
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Telefono", text="Teléfono")
        self.tree.pack(side="top", fill="both", expand=True)
        
        self.rellenar_tabla()

    def rellenar_tabla(self):
        self.listar_clientes()
        self.tree.delete(*self.tree.get_children())
        
        # Relleno de la tabla con los datos de los clientes
        for cliente in self.clientes:
            self.tree.insert("", "end", values=cliente)

    def initialize_alta(self):
        self.frame_alta = ctk.CTkFrame(self.ventana)
        self.frame_alta.pack(side="left", fill="both", padx=10, pady=10, expand=True)
        
        # Configuración de campos para el registro de un nuevo cliente
        self.label_nombre = ctk.CTkLabel(self.frame_alta, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_alta)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_apellido = ctk.CTkLabel(self.frame_alta, text="Apellido:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_apellido = ctk.CTkEntry(self.frame_alta)
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10)

        self.label_email = ctk.CTkLabel(self.frame_alta, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_email = ctk.CTkEntry(self.frame_alta)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        self.label_telefono = ctk.CTkLabel(self.frame_alta, text="Teléfono:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_telefono = ctk.CTkEntry(self.frame_alta)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=10)
        
        # Botón para registrar un nuevo cliente
        self.boton_registrar = ctk.CTkButton(self.frame_alta, text="Registrar Cliente", command=self.registrar_cliente)
        self.boton_registrar.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

    def registrar_cliente(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        
        # Llamada al gestor para registrar el cliente
        self.gestor_cliente.registrar_cliente(nombre, apellido, email, telefono)
        
        # Refrescar la tabla después de registrar el cliente
        self.rellenar_tabla()

    def listar_clientes(self):
        self.clientes = self.gestor_cliente.listar_clientes()

    def modificar_cliente(self):
        # Obtiene el cliente seleccionado
        item = self.tree.selection()
        if item:
            cliente_selecc = self.tree.item(item, "values")
            mod_cliente = ModificacionCliente.ModificacionCliente(self.ventana, cliente_selecc)
            mod_cliente.show()
