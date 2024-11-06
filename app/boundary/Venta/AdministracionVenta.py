import customtkinter as ctk
from tkinter import ttk
from ...entities.AutoModel import Auto
from ...entities.ClienteModel import Cliente
from ...entities.VendedorModel import Vendedor
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

        self.header()
        self.initialize_consulta()
        self.footer()

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

    def initialize_consulta(self):
        self.frame_lista = ctk.CTkFrame(self.ventana)
        self.frame_lista.pack(side="top", fill="both",
                              padx=10, pady=10, expand=True)

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
        # self.footer()

    def rellenar_tabla(self):
        self.listar_ventas()
        self.tree.delete(*self.tree.get_children())
        for venta in self.ventas_datos:
            self.tree.insert("", "end", values=venta)

    def footer(self):
        self.frame_registro = ctk.CTkFrame(self.ventana)
        self.frame_registro.pack(
            side="bottom", fill="x", padx=10, pady=10, expand=True)

        # Botón para registrar una nueva venta
        self.boton_registrar = ctk.CTkButton(
            self.frame_registro, text="Registrar Venta", command=self.registrar_venta)
        self.boton_registrar.pack(side="left", fill="y")
        
        # Botón para eliminar una venta
        self.boton_eliminar = ctk.CTkButton(
            self.frame_registro, text="Eliminar Venta", command=self.eliminar_venta)
        self.boton_eliminar.pack(side="right", fill="y")

    def registrar_venta(self):
        reg_venta = RegistroVenta.RegistroVenta(self)
        self.ventana.withdraw()
        reg_venta.show()

    def eliminar_venta(self):
        if self.venta_selecc:
            self.gestor_venta.eliminar_venta(id=self.venta_selecc.id)
            self.rellenar_tabla()

    def listar_ventas(self):
        data: list[Venta] = self.gestor_venta.listar_ventas()
        self.ventas = {venta.id: venta for venta in data}
        self.ventas_datos = []
        for venta in self.ventas.values():
            if isinstance(venta, Venta):
                self.ventas_datos.append((venta.id,  venta.fecha, f"{venta.auto.marca} {venta.auto.modelo} {venta.auto.año}",
                                         f"{venta.cliente.nombre} {venta.cliente.apellido}", f"{venta.vendedor.nombre} {venta.vendedor.apellido} ({venta.vendedor_id})"))

