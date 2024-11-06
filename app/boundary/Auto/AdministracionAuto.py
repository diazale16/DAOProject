import customtkinter as ctk
from tkinter import ttk
from ...entities.AutoModel import Auto
from ...control.GestorAuto import GestorAuto
# from ..Home.Home import Home
from . import ModificacionAuto


class AdministracionAuto:
    def __init__(self, home_instance):
        self.gestor_auto = GestorAuto()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()
        
        self.ventana.geometry(f"1280x720")
        ctk.set_appearance_mode("dark")
        self.ventana.attributes("-zoomed", True)
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
        self.boton_home = ctk.CTkButton(
            line1_frame, text="Home", command=self.home
        )
        self.boton_home.pack(side="left", fill="y")
        self.boton_refrescar = ctk.CTkButton(
            line1_frame, text="Refrescar", command=self.rellenar_tabla
        )
        self.boton_refrescar.pack(side="right", fill="y")

    def initialize_consulta(self):
        self.frame_lista = ctk.CTkFrame(self.ventana)
        self.frame_lista.pack(side="top", fill="both",
                              padx=10, pady=10, expand=True)
        self.tree = ttk.Treeview(
            self.frame_lista,
            columns=("VIN", "Marca", "Modelo", "Año",
                     "Precio", "Estado", "Cliente"),
            show="headings",
        )
        self.tree.heading("VIN", text="VIN")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Modelo", text="Modelo")
        self.tree.heading("Año", text="Año")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Cliente", text="Cliente")
        self.tree.pack(side="top", fill="both", expand=True)
        self.rellenar_tabla()

    def rellenar_tabla(self):
        self.listar_autos()
        self.tree.delete(*self.tree.get_children())
        for auto in self.datos_autos:
            self.tree.insert("", "end", values=auto)

    def initialize_alta(self):
        self.frame_alta = ctk.CTkFrame(self.ventana)
        self.frame_alta.pack(side="left", fill="both",
                             padx=10, pady=10, expand=True)

        self.label_vin = ctk.CTkLabel(self.frame_alta, text="Código VIN:").grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        self.entry_vin = ctk.CTkEntry(self.frame_alta)
        self.entry_vin.grid(row=1, column=1, padx=10, pady=10)

        self.label_marca = ctk.CTkLabel(self.frame_alta, text="Marca:").grid(
            row=1, column=2, padx=10, pady=10, sticky="w"
        )
        self.entry_marca = ctk.CTkEntry(self.frame_alta)
        self.entry_marca.grid(row=1, column=3, padx=10, pady=10)

        self.label_modelo = ctk.CTkLabel(self.frame_alta, text="Modelo:").grid(
            row=1, column=4, padx=10, pady=10, sticky="w"
        )
        self.entry_modelo = ctk.CTkEntry(self.frame_alta)
        self.entry_modelo.grid(row=1, column=5, padx=10, pady=10)

        self.label_año = ctk.CTkLabel(self.frame_alta, text="Año:").grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        self.entry_año = ctk.CTkEntry(self.frame_alta)
        self.entry_año.grid(row=2, column=1, padx=10, pady=10)

        self.label_precio = ctk.CTkLabel(self.frame_alta, text="Precio:").grid(
            row=2, column=2, padx=10, pady=10, sticky="w"
        )
        self.entry_precio = ctk.CTkEntry(self.frame_alta)
        self.entry_precio.grid(row=2, column=3, padx=10, pady=10)

        self.label_estado = ctk.CTkLabel(self.frame_alta, text="Estado:").grid(
            row=2, column=4, padx=10, pady=10, sticky="w"
        )
        self.estado_var = ctk.StringVar(value="Nuevo")

        self.radio_nuevo = ctk.CTkRadioButton(
            self.frame_alta, text="Nuevo", variable=self.estado_var, value="Nuevo"
        )
        self.radio_nuevo.grid(row=2, column=5, padx=10, pady=10, sticky="w")
        self.radio_usado = ctk.CTkRadioButton(
            self.frame_alta, text="Usado", variable=self.estado_var, value="Usado"
        )
        self.radio_usado.grid(row=2, column=6, padx=10, pady=10, sticky="e")

        self.label_cliente = ctk.CTkLabel(
            self.frame_alta, text="Cliente ID (opcional):"
        ).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_cliente = ctk.CTkEntry(self.frame_alta)
        self.entry_cliente.grid(row=3, column=1, padx=10, pady=10)

        self.boton_registrar = ctk.CTkButton(
            self.frame_alta, text="Registrar Auto", command=self.registrar_auto
        ).grid(row=5, column=0, columnspan=2, padx=10, pady=20)

    def initialize_detalle(self):
        self.frame_detalle = ctk.CTkFrame(self.ventana)
        self.frame_detalle.pack(
            side="right", fill="both", padx=10, pady=10, expand=True
        )
        self.tree.bind("<<TreeviewSelect>>", self.mostrar_detalles)
        
    def mostrar_detalles(self, event):
        item_selecc = self.tree.selection()
        if item_selecc:
            selection_data = self.tree.item(item_selecc, "values")
            self.auto_selecc = self.autos[selection_data[0]]
        self.label_det_vin = ctk.CTkLabel(
            self.frame_detalle, text=f"Código VIN: {self.auto_selecc.vin}"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.label_det_marca = ctk.CTkLabel(
            self.frame_detalle, text=f"Marca: {self.auto_selecc.marca}"
        ).grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.label_det_modelo = ctk.CTkLabel(
            self.frame_detalle, text=f"Modelo: {self.auto_selecc.modelo}"
        ).grid(row=1, column=4, padx=10, pady=10, sticky="w")
        self.label_det_año = ctk.CTkLabel(
            self.frame_detalle, text=f"Año: {self.auto_selecc.año}"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.label_det_precio = ctk.CTkLabel(
            self.frame_detalle, text=f"Precio: {self.auto_selecc.precio}"
        ).grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.label_det_estado = ctk.CTkLabel(
            self.frame_detalle, text=f"Estado: {self.auto_selecc.estado.nombre}"
        ).grid(row=2, column=4, padx=10, pady=10, sticky="w")
        if self.auto_selecc.cliente_id:
            self.label_det_cliente = ctk.CTkLabel(
                self.frame_detalle, text=f"Cliente ID: {self.auto_selecc.cliente_id} ({self.auto_selecc.cliente.nombre} {self.auto_selecc.cliente.apellido})"
            ).grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.boton_modificar = ctk.CTkButton(
            self.frame_detalle, text="Modificar Auto", command=self.modificar_auto
        ).grid(row=5, column=0, columnspan=2, padx=10, pady=20)
        self.boton_eliminar = ctk.CTkButton(
            self.frame_detalle, text="Eliminar Auto", command=self.eliminar_auto
        ).grid(row=5, column=1, columnspan=2, padx=10, pady=20)


    def registrar_auto(self):
        self.vin = self.entry_vin.get()
        self.marca = self.entry_marca.get()
        self.modelo = self.entry_modelo.get()
        self.año = self.entry_año.get()
        self.precio = self.entry_precio.get()
        self.estado = self.estado_var.get()
        self.cliente = self.entry_cliente.get() if self.entry_cliente.get() else None
        self.gestor_auto.registrar_auto(vin=self.vin, marca=self.marca, modelo=self.modelo, año=self.año, precio=self.precio, nom_estado=self.estado, cliente=self.cliente)
        self.rellenar_tabla()

    def modificar_auto(self):
        mod_auto = ModificacionAuto.ModificacionAuto(self.ventana, self.auto_selecc) 
        mod_auto.show()
        # auto = Auto(vin=self.auto_selecc[0], marca=self.auto_selecc[1], modelo=self.auto_selecc[2], año=self.auto_selecc[3], precio=self.auto_selecc[4], estado_id=self.auto_selecc[5], cliente_id=self.auto_selecc[6])
        # print(auto)
        # mod_auto = ModificacionAuto.ModificacionAuto(auto)
        # print(self.auto_selecc)

    def eliminar_auto(self):
        self.gestor_auto.eliminar_auto(self.auto_selecc.vin)
        self.rellenar_tabla()
    
    def listar_autos(self):
        data:list[Auto] = self.gestor_auto.listar_autos()
        self.autos = {auto.vin: auto for auto in data}
        self.datos_autos = []
        for auto in self.autos.values():
            if isinstance(auto, Auto):
                if not (auto.cliente):
                    tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado.nombre, "")
                else:
                    tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado.nombre, auto.cliente_id)
                    # tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado.nombre, f"{auto.cliente.nombre} {auto.cliente.apellido}", auto)
                self.datos_autos.append(tupla)

