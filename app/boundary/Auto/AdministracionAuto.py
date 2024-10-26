import customtkinter as ctk
from tkinter import ttk
from ...entities.AutoModel import Auto
from ...control.GestorAuto import GestorAuto
# from ..Home.Home import Home
from . import ModificacionAuto


class AdministracionAuto:
    def __init__(self):
        self.gestor_auto = GestorAuto()
        # screen_width = self.ventana.winfo_screenwidth()
        # screen_height = self.ventana.winfo_screenheight()
        # self.ventana.geometry(f"{screen_width}x{screen_height}")
        # self.ventana.geometry(f"1920x1080")
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTk()
        self.ventana.attributes("-fullscreen", True)
        self.ventana.resizable(False, False)
        self.header()
        self.initialize_consulta()
        self.initialize_alta()
        self.initialize_detalle()
        
    def home(self):
        self.ventana.destroy()
        
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
        for auto in self.autos:
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
        self.radio_usado.grid(row=2, column=5, padx=10, pady=10, sticky="e")

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
        self.item_selecc = self.tree.selection()
        if self.item_selecc:
            self.auto_selecc = self.tree.item(self.item_selecc, "values")

        print(self.auto_selecc)
        self.label_det_vin = ctk.CTkLabel(
            self.frame_detalle, text=f"Código VIN: {self.auto_selecc[0]}"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.label_det_marca = ctk.CTkLabel(
            self.frame_detalle, text=f"Marca: {self.auto_selecc[1]}"
        ).grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.label_det_modelo = ctk.CTkLabel(
            self.frame_detalle, text=f"Modelo: {self.auto_selecc[2]}"
        ).grid(row=1, column=4, padx=10, pady=10, sticky="w")
        self.label_det_año = ctk.CTkLabel(
            self.frame_detalle, text=f"Año: {self.auto_selecc[3]}"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.label_det_precio = ctk.CTkLabel(
            self.frame_detalle, text=f"Precio: {self.auto_selecc[4]}"
        ).grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.label_det_estado = ctk.CTkLabel(
            self.frame_detalle, text=f"Estado: {self.auto_selecc[5]}"
        ).grid(row=2, column=4, padx=10, pady=10, sticky="w")
        self.label_det_cliente = ctk.CTkLabel(
            self.frame_detalle, text=f"Cliente ID: {self.auto_selecc[6]}"
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
        self.gestor_auto.registrar_auto(self.vin, self.marca, self.modelo, self.año, self.precio, self.estado, self.cliente)
        self.rellenar_tabla()

    def modificar_auto(self):
        auto = Auto(vin=self.auto_selecc[0], marca=self.auto_selecc[1], modelo=self.auto_selecc[2], año=self.auto_selecc[3], precio=self.auto_selecc[4], estado_id=self.auto_selecc[5], cliente_id=self.auto_selecc[6])
        print(auto)
        # mod_auto = ModificacionAuto.ModificacionAuto(auto)
        # print(self.auto_selecc)

    def eliminar_auto(self):
        self.gestor_auto.eliminar_auto(self.auto_selecc[0])
        self.rellenar_tabla()
    
    def listar_autos(self):
        self.autos = self.gestor_auto.listar_autos()

