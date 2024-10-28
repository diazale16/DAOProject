import customtkinter as ctk
from tkinter import ttk
from ...control.GestorTipoServicio import GestorTipoServicio
from .ModificacionTipoServicio import ModificacionTipoServicio

class AdministracionTipoServicio:
    def __init__(self, home_instance):
        self.gestor_tipo_servicio = GestorTipoServicio()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()
        
        self.ventana.geometry("600x400")
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
        
        # Botón para volver a la pantalla principal
        self.boton_home = ctk.CTkButton(line1_frame, text="Home", command=self.home)
        self.boton_home.pack(side="left", fill="y")
        
        # Botón para refrescar la lista de tipos de servicio
        self.boton_refrescar = ctk.CTkButton(line1_frame, text="Refrescar", command=self.rellenar_tabla)
        self.boton_refrescar.pack(side="right", fill="y")

    def initialize_consulta(self):
        self.frame_lista = ctk.CTkFrame(self.ventana)
        self.frame_lista.pack(side="top", fill="both", padx=10, pady=10, expand=True)
        
        # Configuración de la tabla de tipos de servicio
        self.tree = ttk.Treeview(
            self.frame_lista,
            columns=("ID", "Nombre"),
            show="headings",
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.pack(side="top", fill="both", expand=True)
        
        self.rellenar_tabla()

    def rellenar_tabla(self):
        self.listar_tipos_servicio()  # Llamada al nuevo método que corregimos
        self.tree.delete(*self.tree.get_children())
        
        # Relleno de la tabla con los datos de los tipos de servicio
        for tipo in self.tipos_servicio:
            self.tree.insert("", "end", values=(tipo.id, tipo.nombre))

    def initialize_registro(self):
        self.frame_registro = ctk.CTkFrame(self.ventana)
        self.frame_registro.pack(side="left", fill="both", padx=10, pady=10, expand=True)
        
        # Configuración de campos para el registro de un nuevo tipo de servicio
        self.label_nombre = ctk.CTkLabel(self.frame_registro, text="Nombre del Tipo:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_registro)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        # Botón para registrar un nuevo tipo de servicio
        self.boton_registrar = ctk.CTkButton(self.frame_registro, text="Registrar Tipo Servicio", command=self.registrar_tipo_servicio)
        self.boton_registrar.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

        # Botón para modificar un tipo de servicio existente
        self.boton_modificar = ctk.CTkButton(self.frame_registro, text="Modificar Tipo Servicio", command=self.modificar_tipo_servicio)
        self.boton_modificar.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

        # Botón para eliminar un tipo de servicio
        self.boton_eliminar = ctk.CTkButton(self.frame_registro, text="Eliminar Tipo Servicio", command=self.eliminar_tipo_servicio, fg_color="red")
        self.boton_eliminar.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

    def listar_tipos_servicio(self):
        self.tipos_servicio = self.gestor_tipo_servicio.listar_tipos_servicio()

    def registrar_tipo_servicio(self):
        nombre = self.entry_nombre.get()
        if nombre:
            self.gestor_tipo_servicio.registrar_tipo_servicio(nombre)
            self.rellenar_tabla()
            print("Tipo de servicio registrado con éxito.")
        else:
            print("El nombre del tipo de servicio no puede estar vacío.")

    def modificar_tipo_servicio(self):
        item = self.tree.selection()
        if item:
            tipo_seleccionado = self.tree.item(item, "values")
            mod_tipo_servicio = ModificacionTipoServicio(self, tipo_seleccionado)
            mod_tipo_servicio.show()
        else:
            print("Por favor, seleccione un tipo de servicio para modificar.")

    def eliminar_tipo_servicio(self):
        item = self.tree.selection()
        if item:
            tipo_seleccionado = self.tree.item(item, "values")
            self.gestor_tipo_servicio.eliminar_tipo_servicio(tipo_seleccionado[0])
            self.rellenar_tabla()
            print("Tipo de servicio eliminado con éxito.")
        else:
            print("Por favor, seleccione un tipo de servicio para eliminar.")
