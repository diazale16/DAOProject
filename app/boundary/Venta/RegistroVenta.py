import customtkinter as ctk
from tkinter import ttk
from ...entities.AutoModel import Auto
from ...entities.ClienteModel import Cliente
from ...entities.VendedorModel import Vendedor

from ...control.GestorVenta import GestorVenta
from ...control.GestorVendedor import GestorVendedor
from ...control.GestorAuto import GestorAuto
from ...control.GestorCliente import GestorCliente



class RegistroVenta:
    def __init__(self, home_instance):
        self.gestor_venta = GestorVenta()
        self.gestor_vendedor = GestorVendedor()
        self.gestor_auto = GestorAuto()
        self.gestor_cliente = GestorCliente()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()

        self.ventana.geometry(f"1280x720")
        ctk.set_appearance_mode("dark")
        self.ventana.attributes("-zoomed", True)
        
        self.auto_selecc = None
        self.cliente_selecc = None
        self.vendedores_selecc = None

        self.header()
        self.initialize_autos()
        self.initialize_registro()
        self.initialize_clientes()
        self.initialize_vendedores()
        

    def ventas(self):
        self.ventana.destroy()
        self.home_instance.ventana.deiconify()

    def show(self):
        self.ventana.mainloop()

    def header(self):
        line1_frame = ctk.CTkFrame(self.ventana)
        line1_frame.pack(side="top", fill="x", pady=5)

        # Botón para volver a la pantalla principal
        self.boton_home = ctk.CTkButton(
            line1_frame, text="Ventas", command=self.ventas)
        self.boton_home.pack(side="left", fill="y")

    def initialize_autos(self):
        self.frame_autos = ctk.CTkFrame(self.ventana)
        self.frame_autos.pack(side="top", fill="both",
                              padx=10, pady=10, expand=True)
        self.label_auto = ctk.CTkLabel(self.frame_autos, text="Autos:")
        self.label_auto.pack(side="top", padx=10, pady=10)
        self.tree_autos = ttk.Treeview(
            self.frame_autos,
            columns=("VIN", "Marca", "Modelo", "Año", "Precio", "Estado"),
            show="headings",
        )
        self.tree_autos.heading("VIN", text="VIN")
        self.tree_autos.heading("Marca", text="Marca")
        self.tree_autos.heading("Modelo", text="Modelo")
        self.tree_autos.heading("Año", text="Año")
        self.tree_autos.heading("Precio", text="Precio")
        self.tree_autos.heading("Estado", text="Estado")
        self.tree_autos.pack(side="top", fill="both", expand=True)
        self.tree_autos.bind("<<TreeviewSelect>>", self.selecc_auto)
        self.rellenar_tabla_autos()

    def initialize_clientes(self):
        self.frame_bajo = ctk.CTkFrame(self.ventana)
        self.frame_bajo.pack(side="bottom", fill="both",
                              padx=10, pady=10, expand=True)
        self.frame_clientes = ctk.CTkFrame(self.frame_bajo)
        self.frame_clientes.pack(side="left", fill="both",
                              padx=10, pady=10, expand=True)
        self.label_cliente = ctk.CTkLabel(self.frame_clientes, text="Clientes:")
        self.label_cliente.pack(side="top", padx=10, pady=10)
        self.tree_clientes = ttk.Treeview(
            self.frame_clientes,
            columns=("ID", "Nombre", "Apellido", "Telefono", "Direccion"),
            show="headings",
        )
        self.tree_clientes.heading("ID", text="ID")
        self.tree_clientes.heading("Nombre", text="Nombre")
        self.tree_clientes.heading("Apellido", text="Apellido")
        self.tree_clientes.heading("Telefono", text="Telefono")
        self.tree_clientes.heading("Direccion", text="Direccion")
        self.tree_clientes.pack(side="left", fill="both", expand=True)
        self.tree_clientes.bind("<<TreeviewSelect>>", self.selecc_cliente)
        self.rellenar_tabla_clientes()
        
    def initialize_vendedores(self):
        self.frame_vendedores = ctk.CTkFrame(self.frame_bajo)
        self.frame_vendedores.pack(side="right", fill="both",
                              padx=10, pady=10, expand=True)
        self.label_vendedor = ctk.CTkLabel(self.frame_vendedores, text="Vendedores:")
        self.label_vendedor.pack(side="top", padx=10, pady=10)
        self.tree_vendedores = ttk.Treeview(
            self.frame_vendedores,
            columns=("ID", "Nombre", "Apellido", "Porcentaje Comision"),
            show="headings",
        )
        self.tree_vendedores.heading("ID", text="ID")
        self.tree_vendedores.heading("Nombre", text="Nombre")
        self.tree_vendedores.heading("Apellido", text="Apellido")
        self.tree_vendedores.heading("Porcentaje Comision", text="Porcentaje Comision")
        self.tree_vendedores.pack(side="left", fill="both", expand=True)
        self.tree_vendedores.bind("<<TreeviewSelect>>", self.selecc_vendedor)
        self.rellenar_tabla_vendedores()
    
    def selecc_auto(self, event):
        item_selecc = self.tree_autos.selection()
        if item_selecc:
            selection_data = self.tree_autos.item(item_selecc, "values")
            self.auto_selecc = self.autos[selection_data[0]]

    def selecc_cliente(self, event):
        item_selecc = self.tree_clientes.selection()
        if item_selecc:
            selection_data = self.tree_clientes.item(item_selecc, "values")
            self.cliente_selecc = self.clientes[selection_data[0]]
            
    def selecc_vendedor(self, event):
        item_selecc = self.tree_vendedores.selection()
        if item_selecc:
            selection_data = self.tree_vendedores.item(item_selecc, "values")
            self.vendedores_selecc = self.vendedores[selection_data[0]]
    
    def rellenar_tabla_autos(self):
        self.listar_autos()
        self.tree_autos.delete(*self.tree_autos.get_children())
        for auto in self.datos_autos:
            self.tree_autos.insert("", "end", values=auto)
            
    def rellenar_tabla_clientes(self):
        self.listar_clientes()
        self.tree_clientes.delete(*self.tree_clientes.get_children())
        for cliente in self.datos_clientes:
            self.tree_clientes.insert("", "end", values=cliente)
            
    def rellenar_tabla_vendedores(self):
        self.listar_vendedores()
        self.tree_vendedores.delete(*self.tree_vendedores.get_children())
        for vendedor in self.datos_vendedores:
            self.tree_vendedores.insert("", "end", values=vendedor)

    def initialize_registro(self):
        self.frame_registro = ctk.CTkFrame(self.ventana)
        self.frame_registro.pack(
            side="bottom", fill="x", padx=10, pady=10, expand=True)

        self.boton_registrar = ctk.CTkButton(
            self.frame_registro, text="Registrar Venta", command=self.registrar_venta)
        self.boton_registrar.pack(fill="both", pady=10, padx=10)

    def registrar_venta(self):
        if not self.auto_selecc:
            self.mostrar_modal_confirmacion(
                f"Seleccione un auto a vender")
            return
        if not self.cliente_selecc: 
            self.mostrar_modal_confirmacion(
                f"Seleccione un cliente")
            return
        if not self.vendedores_selecc:
            self.mostrar_modal_confirmacion(
                f"Seleccione un vendedor")
            return
        
        # Llamada al gestor para registrar la venta
        try:
            self.gestor_venta.registrar_venta(auto=self.auto_selecc, cliente=self.cliente_selecc, vendedor=self.vendedores_selecc)
            self.mostrar_modal_confirmacion(
                f"Venta guardada con exito.")
        except Exception as e:
            self.mostrar_modal_confirmacion(
                f"Error al registrar la venta.\n{e}")


    def listar_autos(self):
        data:list[Auto] = self.gestor_auto.listar_autos_no_vendidos()
        self.autos = {auto.vin: auto for auto in data}
        print(self.autos)
        self.datos_autos = []
        for auto in self.autos.values():
            if isinstance(auto, Auto):
                    tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado.nombre)
                    self.datos_autos.append(tupla)
        
                
    def listar_clientes(self):
        data:list[Cliente] = self.gestor_cliente.listar_clientes()
        self.clientes = {cliente.id: cliente for cliente in data}
        # print(self.clientes)
        self.datos_clientes = []
        for cliente in self.clientes.values():
            if isinstance(cliente, Cliente):
                    tupla = (cliente.id, cliente.nombre, cliente.apellido, cliente.telefono, cliente.direccion)
                    self.datos_clientes.append(tupla)
    
    def listar_vendedores(self):
        data:list[Vendedor] = self.gestor_vendedor.listar_vendedors()
        self.vendedores = {vendedor.id: vendedor for vendedor in data}
        # print(self.autos)
        self.datos_vendedores = []
        for vendedor in self.vendedores.values():
            if isinstance(vendedor, Vendedor):
                    tupla = (vendedor.id, vendedor.nombre, vendedor.apellido, vendedor.porc_comision)
                    self.datos_vendedores.append(tupla)
                    
    def mostrar_modal_confirmacion(self, mensaje):
        self.modal = ctk.CTkToplevel(self.ventana)
        self.modal.title("Regisro de venta")
        self.modal.geometry("600x150")
        self.modal.transient(self.ventana)
        self.modal.update()
        self.modal.grab_set()

        label = ctk.CTkLabel(self.modal, text=mensaje)
        label.pack(pady=20)
        cerrar_btn = ctk.CTkButton(self.modal, text="Cerrar", command=self.modal.destroy)
        cerrar_btn.pack(side="bottom", pady=10, padx=20, fill="x")