import customtkinter as ctk
from tkinter import ttk, messagebox
from ...entities.ClienteModel import Cliente
from ...control.GestorCliente import GestorCliente
from . import ModificacionCliente

class AdministracionCliente:
    def __init__(self, home_instance):
        self.gestor_cliente = GestorCliente()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()
        
        self.ventana.geometry("1280x720")  # Ajustar la geometría manualmente
        ctk.set_appearance_mode("dark")
        self.ventana.state("zoomed")  # Maximizar la ventana sin usar -zoomed
        
        self.header()
        self.initialize_consulta()
        self.initialize_alta()
        self.initialize_detalle()
        
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
            columns=("ID", "Nombre", "Apellido", "Dirección", "Telefono"),
            show="headings",
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Dirección", text="Dirección")
        self.tree.heading("Telefono", text="Teléfono")
        self.tree.pack(side="top", fill="both", expand=True)

        self.rellenar_tabla()

    def rellenar_tabla(self):
        self.listar_clientes()
        self.tree.delete(*self.tree.get_children())
        
        # Relleno de la tabla con los datos de los clientes
        for cliente in self.datos_cliente:
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

        # Campos para la dirección
        self.label_calle = ctk.CTkLabel(self.frame_alta, text="Calle:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_calle = ctk.CTkEntry(self.frame_alta)
        self.entry_calle.grid(row=2, column=1, padx=10, pady=10)

        self.label_numero = ctk.CTkLabel(self.frame_alta, text="Número:").grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.entry_numero = ctk.CTkEntry(self.frame_alta)
        self.entry_numero.grid(row=2, column=3, padx=10, pady=10)

        self.label_localidad = ctk.CTkLabel(self.frame_alta, text="Localidad:").grid(row=2, column=4, padx=10, pady=10, sticky="w")
        self.entry_localidad = ctk.CTkEntry(self.frame_alta)
        self.entry_localidad.grid(row=2, column=5, padx=10, pady=10)


        self.label_telefono = ctk.CTkLabel(self.frame_alta, text="Teléfono:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_telefono = ctk.CTkEntry(self.frame_alta)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=10)
        
        # Botón para registrar un nuevo cliente
        self.boton_registrar = ctk.CTkButton(self.frame_alta, text="Registrar Cliente", command=self.registrar_cliente)
        self.boton_registrar.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

    def initialize_detalle(self):
        self.frame_detalle = ctk.CTkFrame(self.ventana)
        self.frame_detalle.pack(
            side="right", fill="both", padx=10, pady=10, expand=True
        )
        self.tree.bind("<<TreeviewSelect>>", self.mostrar_detalles)

    def mostrar_detalles(self, event):
        item_selecc = self.tree.selection()
        if item_selecc:
            self.cliente_selecc = self.tree.item(item_selecc, "values")
        self.label_det_vin = ctk.CTkLabel(
            self.frame_detalle, text=f"Código VIN: {self.cliente_selecc[0]}"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.label_det_nombre = ctk.CTkLabel(
            self.frame_detalle, text=f"Nombre: {self.cliente_selecc[1]}"
        ).grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.label_det_apellido = ctk.CTkLabel(
            self.frame_detalle, text=f"Apellido: {self.cliente_selecc[2]}"
        ).grid(row=1, column=4, padx=10, pady=10, sticky="w")
        self.label_det_email = ctk.CTkLabel(
            self.frame_detalle, text=f"Calle: {self.cliente_selecc[3]}"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.label_det_telefono = ctk.CTkLabel(
            self.frame_detalle, text=f"Telefono: {self.cliente_selecc[4]}"
        ).grid(row=2, column=2, padx=10, pady=10, sticky="w")

        self.boton_modificar = ctk.CTkButton(
            self.frame_detalle, text="Modificar Cliente", command=self.modificar_cliente
        ).grid(row=5, column=0, columnspan=2, padx=10, pady=20)
        self.boton_eliminar = ctk.CTkButton(
            self.frame_detalle, text="Eliminar Cliente", command=self.eliminar_cliente
        ).grid(row=5, column=1, columnspan=2, padx=10, pady=20)

    def registrar_cliente(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        calle = self.entry_calle.get()
        numero = self.entry_numero.get()
        localidad = self.entry_localidad.get()
        telefono = self.entry_telefono.get()
        
        # Validación de campos vacíos
        if not nombre or not apellido or not calle or not numero or not localidad or not telefono:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos antes de registrar el cliente.")
            return

        # Concatenar la dirección
        direccion = f"{calle}, {numero}, {localidad}"

        # Llamada al gestor para registrar el cliente
        self.gestor_cliente.registrar_cliente(nombre, apellido, telefono, direccion)
        
         # Limpiar los campos de entrada solo si el registro fue exitoso
        self.entry_nombre.delete(0, 'end')
        self.entry_apellido.delete(0, 'end')
        self.entry_calle.delete(0, 'end')
        self.entry_numero.delete(0, 'end')
        self.entry_localidad.delete(0, 'end')
        self.entry_telefono.delete(0, 'end')

        # Refrescar la tabla después de registrar el cliente
        self.rellenar_tabla()

    def eliminar_cliente(self):
        confirm = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar este cliente?")
        if confirm:
            try:
                self.gestor_cliente.eliminar_cliente(self.cliente_selecc[0])
                self.rellenar_tabla() 
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el cliente: {str(e)}")
    
    def listar_clientes(self):
        data:list[Cliente] = self.gestor_cliente.listar_clientes()
        self.cliente = {cliente.id: cliente for cliente in data}
        self.datos_cliente = []
        for cliente in self.cliente.values():
            if isinstance(cliente, Cliente):
                    tupla = (cliente.id, cliente.nombre, cliente.apellido, cliente.direccion, cliente.telefono)
            self.datos_cliente.append(tupla)

    def modificar_cliente(self):
        mod_cliente = ModificacionCliente.ModificacionCliente(self.ventana, self.cliente_selecc) 
        mod_cliente.show()
