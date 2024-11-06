# boundary/Servicio/AdministracionServicio.py

import customtkinter as ctk
from tkinter import ttk, messagebox
from ...control.GestorServicio import GestorServicio
from ...entities.ServicioModel import Servicio

class AdministracionServicio:
    def __init__(self, home_instance):
        self.gestor_servicio = GestorServicio()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()
        
        self.ventana.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        self.ventana.state("zoomed")
        
        self.header()
        self.initialize_consulta()
        self.initialize_registro()
        self.initialize_detalle()

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
            columns=("ID", "Fecha", "Auto VIN", "Tipo Servicio", "Costo"),
            show="headings",
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Auto VIN", text="Auto VIN")
        self.tree.heading("Tipo Servicio", text="Tipo Servicio")
        self.tree.heading("Costo", text="Costo")
        self.tree.pack(side="top", fill="both", expand=True)
        
        self.rellenar_tabla()

    def rellenar_tabla(self):
        self.listar_servicios()
        self.tree.delete(*self.tree.get_children())
        for servicio in self.servicios:
            self.tree.insert("", "end", values=servicio)

    def initialize_registro(self):
        self.frame_registro = ctk.CTkFrame(self.ventana)
        self.frame_registro.pack(side="left", fill="both", padx=10, pady=10, expand=True)
        
        self.label_fecha = ctk.CTkLabel(self.frame_registro, text="Fecha:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_fecha = ctk.CTkEntry(self.frame_registro)
        self.entry_fecha.grid(row=0, column=1, padx=10, pady=10)

        self.label_auto_vin = ctk.CTkLabel(self.frame_registro, text="Auto VIN:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_auto_vin = ctk.CTkEntry(self.frame_registro)
        self.entry_auto_vin.grid(row=1, column=1, padx=10, pady=10)

        self.label_tipo_servicio = ctk.CTkLabel(self.frame_registro, text="Tipo Servicio:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_tipo_servicio = ctk.CTkEntry(self.frame_registro)
        self.entry_tipo_servicio.grid(row=2, column=1, padx=10, pady=10)

        self.label_costo = ctk.CTkLabel(self.frame_registro, text="Costo:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_costo = ctk.CTkEntry(self.frame_registro)
        self.entry_costo.grid(row=3, column=1, padx=10, pady=10)
        
        self.boton_registrar = ctk.CTkButton(self.frame_registro, text="Registrar Servicio", command=self.registrar_servicio)
        self.boton_registrar.grid(row=4, column=0, columnspan=2, padx=10, pady=20)
    
    def initialize_detalle(self):
        self.frame_detalle = ctk.CTkFrame(self.ventana)
        self.frame_detalle.pack(side="right", fill="both", padx=10, pady=10, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.mostrar_detalles)
        
    def mostrar_detalles(self, event):
        item_selecc = self.tree.selection()
        if item_selecc:
            self.servicio_selecc = self.tree.item(item_selecc, "values")
        self.label_det_vin = ctk.CTkLabel(
            self.frame_detalle, text=f"Código VIN: {self.servicio_selecc[0]}"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.label_det_fecha = ctk.CTkLabel(
            self.frame_detalle, text=f"Fecha: {self.servicio_selecc[1]}"
        ).grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.label_det_cod_auto = ctk.CTkLabel(
            self.frame_detalle, text=f"Auto VIN: {self.servicio_selecc[2]}"
        ).grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.label_det_tip_servicio = ctk.CTkLabel(
            self.frame_detalle, text=f"Tipo de servicio: {self.servicio_selecc[3]}"
        ).grid(row=1, column=4, padx=10, pady=10, sticky="w")
        self.label_det_costo = ctk.CTkLabel(
            self.frame_detalle, text=f"Costo del servicio: {self.servicio_selecc[4]}"
        ).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        

        self.boton_modificar = ctk.CTkButton(
            self.frame_detalle, text="Modificar Servicio", command=self.modificar_servicio
        ).grid(row=5, column=0, columnspan=2, padx=10, pady=20)
        self.boton_eliminar = ctk.CTkButton(
            self.frame_detalle, text="Eliminar Servicio", command=self.eliminar_servicio
        ).grid(row=5, column=1, columnspan=2, padx=10, pady=20)

    def registrar_servicio(self):
        fecha = self.entry_fecha.get()
        auto_vin = self.entry_auto_vin.get()
        tipo_servicio = self.entry_tipo_servicio.get()
        costo = self.entry_costo.get()
        
        # Validación de campos vacíos
        if not fecha or not auto_vin or not tipo_servicio or not costo:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos antes de registrar el servicio.")
            return
        
        try:
            self.gestor_servicio.registrar_servicio(fecha, costo, auto_vin, tipo_servicio)
            self.rellenar_tabla()
            print("Servicio registrado con éxito.")
        except Exception as e:
            print(f"Error al registrar el servicio: {e}")
            
    def eliminar_servicio(self):
        confirm = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar este servicio?")
        if confirm:
            try:
                self.gestor_servicio.eliminar_servicio(self.servicio_selecc[0])
                self.rellenar_tabla() 
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el servicio: {str(e)}")

    def listar_servicios(self):
        data:list[Servicio] = self.gestor_servicio.listar_servicios()
        self.servicio = {servicio.id: servicio for servicio in data}
        self.datos_servicio = []
        for servicio in self.servicio.values():
            if isinstance(servicio, Servicio):
                    tupla = (servicio.id, servicio.fecha, servicio.costo, servicio.auto_vin, servicio.tipo_servicio_id)
            self.datos_servicio.append(tupla)