import customtkinter as ctk
from tkinter import ttk
from ...entities.ClienteModel import Cliente
from ...entities.VentaModel import Venta

from ...control.GestorVenta import GestorVenta
from ...control.GestorAuto import GestorAuto
from ...control.GestorCliente import GestorCliente

from . import RegistroVenta


class AdministracionVenta:
    def __init__(self, home_instance):
        self.gestor_venta = GestorVenta()
        self.gestor_auto = GestorAuto()
        self.gestor_cliente = GestorCliente()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()

        self.ventana.geometry(f"1280x720")
        ctk.set_appearance_mode("dark")
        self.ventana.attributes("-zoomed", True)
        self.selected_client = None

        self.header()
        self.search()
        self.initialize_consulta()
        self.actions()

    def home(self):
        self.ventana.destroy()
        self.home_instance.ventana.deiconify()

    def show(self):
        self.ventana.mainloop()

    def header(self):
        line1_frame = ctk.CTkFrame(self.ventana)
        line1_frame.pack(side="top", fill="x", pady=5)

        # Botón para volver a la pantalla principal
        self.boton_home = ctk.CTkButton(
            line1_frame, text="Home", command=self.home)
        self.boton_home.pack(side="left", fill="y")

        # Botón para refrescar la lista de ventas
        self.boton_refrescar = ctk.CTkButton(
            line1_frame, text="Refrescar", command=self.rellenar_tabla)
        self.boton_refrescar.pack(side="right", fill="y")

    def search(self):
        line2_frame = ctk.CTkFrame(self.ventana)
        line2_frame.pack(side="top", fill="x", pady=5)
        self.listar_clientes()

        # Botón para volver a la pantalla principal
        self.dropdown_var = ctk.StringVar()
        self.dropdown = ctk.CTkComboBox(
            line2_frame, variable=self.dropdown_var, values=self.options, command=self.on_selection)
        self.dropdown.pack(fill="x", padx=10, pady=20)

        self.btn_reset = ctk.CTkButton(
            line2_frame, text="Resetear", command=self.reset_search)
        self.btn_reset.pack(side="right", fill="y", padx=10, pady=20)

        self.btn_search = ctk.CTkButton(
            line2_frame, text="Buscar", command=self.do_search)
        self.btn_search.pack(side="right", fill="y", padx=10, pady=20)

    def reset_search(self):
        self.selected_client = None
        self.dropdown_var = ctk.StringVar()
        self.rellenar_tabla()

    def do_search(self):
        print(self.selected_client)
        self.rellenar_tabla(self.selected_client)

    def on_selection(self, event):
        selected_cliente = self.dropdown_var.get()
        print(selected_cliente.split("|")[0])
        cliente = next((c for c in self.clientes if c.id == (
            selected_cliente.split("|")[0]).strip()), None)
        if cliente:
            self.selected_client = cliente

    def initialize_consulta(self):
        self.frame_lista = ctk.CTkFrame(self.ventana)
        self.frame_lista.pack(fill="both",
                              padx=10, pady=20, expand=True)

        self.label_tipo_servicio = ctk.CTkLabel(
            self.frame_lista, text="Ventas:")
        self.label_tipo_servicio.pack(side="top", fill="x",
                                      padx=10, pady=20)
        # Configuración de la tabla de ventas
        self.tree = ttk.Treeview(
            self.frame_lista,
            columns=("ID", "Fecha", "Auto", "Cliente", "Vendedor"),
            show="headings",
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Auto", text="Auto")
        self.tree.heading("Cliente", text="Cliente")
        self.tree.heading("Vendedor", text="Vendedor")
        self.tree.pack(side="top", fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_item)
        self.rellenar_tabla()

    def seleccionar_item(self, event):
        item_selecc = self.tree.selection()
        if item_selecc:
            selection_data = self.tree.item(item_selecc, "values")
            self.venta_selecc = self.ventas[selection_data[0]]

    def rellenar_tabla(self, cliente: Cliente = None):
        if cliente:
            self.listar_ventas(cliente)
        else:
            self.listar_ventas()
        self.tree.delete(*self.tree.get_children())
        for venta in self.ventas_datos:
            self.tree.insert("", "end", values=venta)

    def actions(self):
        self.frame_registro = ctk.CTkFrame(self.ventana)
        self.frame_registro.pack(
            side="bottom", fill="x", padx=10, pady=20, expand=True)

        # Botón para registrar una nueva venta
        self.boton_registrar = ctk.CTkButton(
            self.frame_registro, text="Registrar Venta", command=self.registrar_venta)
        self.boton_registrar.pack(side="left", fill="y", padx=10, pady=20)

        # Botón para eliminar una venta
        self.boton_eliminar = ctk.CTkButton(
            self.frame_registro, text="Eliminar Venta", command=self.eliminar_venta)
        self.boton_eliminar.pack(side="right", fill="y", padx=10, pady=20)

    def registrar_venta(self):
        reg_venta = RegistroVenta.RegistroVenta(self)
        self.ventana.withdraw()
        reg_venta.show()

    def eliminar_venta(self):
        if self.venta_selecc:
            self.gestor_venta.eliminar_venta(id=self.venta_selecc.id)
            self.rellenar_tabla()

    def listar_ventas(self, cliente: Cliente = None):
        data: list[Venta] = self.gestor_venta.listar_ventas()
        if cliente:
            self.ventas = {
                venta.id: venta for venta in data if venta.cliente_id == cliente.id}
        else:
            self.ventas = {venta.id: venta for venta in data}
        self.ventas_datos = []
        for venta in self.ventas.values():
            if isinstance(venta, Venta):
                self.ventas_datos.append((venta.id,  venta.fecha, f"{venta.auto.marca} {venta.auto.modelo} {venta.auto.año}",
                                         f"{venta.cliente.nombre} {venta.cliente.apellido}", f"{venta.vendedor.nombre} {venta.vendedor.apellido} ({venta.vendedor_id})"))

    def listar_clientes(self):
        self.clientes: list[Cliente] = self.gestor_cliente.listar_clientes()
        self.options = [
            f"{cliente.id} | {cliente.nombre} {cliente.apellido}" for cliente in self.clientes]
