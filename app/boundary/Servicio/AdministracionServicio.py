# boundary/Servicio/AdministracionServicio.py

import customtkinter as ctk
from tkcalendar import DateEntry
from tkinter import ttk
from ...control.GestorServicio import GestorServicio
from ...control.GestorAuto import GestorAuto
from ...control.GestorTipoServicio import GestorTipoServicio
from ...entities.ServicioModel import Servicio
from ...control.GestorVenta import GestorVenta
from ...control.GestorVendedor import GestorVendedor
from decimal import Decimal
class AdministracionServicio:
    def __init__(self, home_instance):
        self.gestor_servicio = GestorServicio()
        self.gestor_auto = GestorAuto() 
        self.gestor_tipo_servicio = GestorTipoServicio()
        self.gestor_venta = GestorVenta()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()
        self.gestor_vendedor = GestorVendedor()
        
        self.ventana.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        self.ventana.state("zoomed")
        
        self.header()
        self.initialize_consulta()
        self.initialize_registro()

    def home(self):
        self.ventana.destroy()
        self.home_instance.ventana.deiconify()
        
    def show(self):
        self.ventana.mainloop()

    def header(self):
        line1_frame = ctk.CTkFrame(self.ventana)
        line1_frame.pack(side="top", fill="x", pady=5)
        
        self.boton_home = ctk.CTkButton(line1_frame, text="Home", command=self.home)
        self.boton_home.pack(side="left", fill="y")
        
        self.boton_refrescar = ctk.CTkButton(line1_frame, text="Refrescar", command=self.rellenar_tabla)
        self.boton_refrescar.pack(side="right", fill="y")

    def initialize_consulta(self):
        self.frame_lista = ctk.CTkFrame(self.ventana)
        self.frame_lista.pack(side="top", fill="both", padx=10, pady=10, expand=True)
        
        self.tree = ttk.Treeview(
            self.frame_lista,
            columns=("ID", "Fecha", "Auto VIN", "Tipo Servicio", "Costo", "Vendedor ID"),
            show="headings",
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Auto VIN", text="Auto VIN")
        self.tree.heading("Tipo Servicio", text="Tipo Servicio")
        self.tree.heading("Costo", text="Costo")
        self.tree.heading("Vendedor ID", text="Vendedor ID")
        self.tree.pack(side="top", fill="both", expand=True)

        label_titulo = ctk.CTkLabel(self.frame_lista, text="Servicios por Auto", font=("Arial", 14, "bold"))
        label_titulo.pack(pady=10)
        
        self.tree_consulta = ttk.Treeview(
        self.frame_lista,
        columns=("ID", "Fecha", "Auto VIN", "Tipo Servicio", "Costo", "Vendedor ID"),
        show="headings",
    )
        self.tree_consulta.heading("ID", text="ID")
        self.tree_consulta.heading("Fecha", text="Fecha")
        self.tree_consulta.heading("Auto VIN", text="Auto VIN")
        self.tree_consulta.heading("Tipo Servicio", text="Tipo Servicio")
        self.tree_consulta.heading("Costo", text="Costo")
        self.tree_consulta.heading("Vendedor ID", text="Vendedor ID")
        self.tree_consulta.pack(side="top", fill="both", expand=True)

        
        self.rellenar_tabla()

    def rellenar_tabla(self):
        self.listar_servicios()
        self.tree.delete(*self.tree.get_children())
        for servicio in self.datos_servicios:
            self.tree.insert("", "end", values=servicio)

    def initialize_registro(self):
        self.frame_registro = ctk.CTkFrame(self.ventana)
        self.frame_registro.pack(side="left", fill="both", padx=10, pady=10, expand=True)

        # Frame para los elementos de consulta (VIN y botón)
        self.frame_consulta = ctk.CTkFrame(self.ventana)
        self.frame_consulta.pack(side="right", padx=10, pady=10, expand=True)

        # Campos de registro de servicio
        self.label_fecha = ctk.CTkLabel(self.frame_registro, text="Fecha:")
        self.label_fecha.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_fecha = DateEntry(self.frame_registro, date_pattern='yyyy-mm-dd')
        self.entry_fecha.grid(row=0, column=1, padx=10, pady=10)

        self.label_auto_vin = ctk.CTkLabel(self.frame_registro, text="Auto VIN:")
        self.label_auto_vin.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_auto_vin = ttk.Combobox(self.frame_registro)
        self.entry_auto_vin['values'] = self.obtener_lista_autos_vendidos()  # Llenar con la lista de VINs
        self.entry_auto_vin.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.label_tipo_servicio = ctk.CTkLabel(self.frame_registro, text="Tipo de Servicio:")
        self.label_tipo_servicio.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_tipo_servicio = ttk.Combobox(self.frame_registro)
        self.entry_tipo_servicio['values'] = ["Mantenimiento", "Reparación"]  # Opciones de la lista
        self.entry_tipo_servicio.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.label_costo = ctk.CTkLabel(self.frame_registro, text="Costo:")
        self.label_costo.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_costo = ctk.CTkEntry(self.frame_registro)
        self.entry_costo.grid(row=3, column=1, padx=10, pady=10)

        self.label_vendedor = ctk.CTkLabel(self.frame_registro, text="Vendedor:")
        self.label_vendedor.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_vendedor = ttk.Combobox(self.frame_registro)
        self.entry_vendedor['values'] = self.obtener_vendedores() 
        self.entry_vendedor.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        self.boton_registrar = ctk.CTkButton(self.frame_registro, text="Registrar Servicio", command=self.registrar_servicio)
        self.boton_registrar.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

        # Campos de consulta (VIN y botón)
        self.label_auto_vin_consulta = ctk.CTkLabel(self.frame_consulta, text="Ingrese VIN del Auto:")
        self.label_auto_vin_consulta.pack(side="top", padx=10, pady=10)

        self.entry_auto_vin_consulta = ttk.Combobox(self.frame_consulta)
        self.entry_auto_vin_consulta['values'] = self.listar_autos()  # Llenar con la lista de VINs
        self.entry_auto_vin_consulta.pack(side="top", padx=10, pady=10)

        self.boton_consultar = ctk.CTkButton(self.frame_consulta, text="Consultar Servicios", command=self.consultar_servicios)
        self.boton_consultar.pack(side="top", padx=10, pady=10)


    def registrar_servicio(self):
        fecha = self.entry_fecha.get()
        auto_vin = self.entry_auto_vin.get()
        tipo_servicio = self.entry_tipo_servicio.get()
        costo = float(self.entry_costo.get())
        vendedor = self.entry_vendedor.get()
        print(f"Registrando servicio con costo: {costo}")        

        self.gestor_servicio.registrar_servicio(costo, auto_vin, tipo_servicio, vendedor, fecha)
        self.rellenar_tabla()


    def listar_servicios(self):
        data:list[Servicio] = self.gestor_servicio.listar_servicios()
        self.servicios = {servicio.id: servicio for servicio in data}
        self.datos_servicios = []
        for servicio in self.servicios.values():
            if isinstance(servicio, Servicio):
                tipo_servicio = self.gestor_tipo_servicio.obtener_tipo_servicio(servicio.tipo_servicio_id)
                vendedor = self.gestor_vendedor.obtener_vendedor(servicio.vendedor_id) 
 
                tupla = (servicio.id, servicio.fecha, servicio.auto_vin, tipo_servicio.nombre, servicio.costo, vendedor.nombre)
                self.datos_servicios.append(tupla)

    def obtener_lista_autos_vendidos(self):
        autos = self.gestor_venta.listar_autos_vendidos()
        return [auto.vin for auto in autos]
    
    def listar_autos(self):
        autos = self.gestor_auto.listar_autos()
        return [auto.vin for auto in autos]

    def obtener_vendedores(self):
        vendedor = self.gestor_vendedor.listar_vendedors()
        return [vendedor.id for vendedor in vendedor]
    
    def consultar_servicios(self):
   
        auto_vin = self.entry_auto_vin_consulta.get()
        servicios = self.gestor_servicio.obtener_servicios_por_auto(auto_vin)

        # Limpiar la segunda tabla antes de llenarla con los nuevos resultados
        for item in self.tree_consulta.get_children():
            self.tree_consulta.delete(item)

        for servicio in servicios:
            tipo_servicio = self.gestor_tipo_servicio.obtener_tipo_servicio(servicio.tipo_servicio_id) 
            vendedor = self.gestor_vendedor.obtener_vendedor(servicio.vendedor_id) 

            self.tree_consulta.insert("", "end", values=(
                servicio.id,
                servicio.fecha,
                servicio.auto_vin,
                tipo_servicio.nombre, 
                servicio.costo,
                vendedor.nombre
            ))