# boundary/Vendedor/AdministracionVendedor.py

import customtkinter as ctk
from tkinter import ttk
from ...control.GestorVendedor import GestorVendedor

class AdministracionVendedor:
    def __init__(self, home_instance):
        self.gestor_vendedor = GestorVendedor()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()
        
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
            columns=("ID", "Nombre", "Teléfono", "Email", "Ventas"),
            show="headings",
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Ventas", text="Ventas")
        self.tree.pack(side="top", fill="both", expand=True)
        
        self.rellenar_tabla()

    def rellenar_tabla(self):
        self.listar_vendedores()
        self.tree.delete(*self.tree.get_children())
        for vendedor in self.vendedores:
            self.tree.insert("", "end", values=vendedor)

    def initialize_registro(self):
        self.frame_registro = ctk.CTkFrame(self.ventana)
        self.frame_registro.pack(side="left", fill="both", padx=10, pady=10, expand=True)
        
        self.label_nombre = ctk.CTkLabel(self.frame_registro, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_registro)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_telefono = ctk.CTkLabel(self.frame_registro, text="Teléfono:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_telefono = ctk.CTkEntry(self.frame_registro)
        self.entry_telefono.grid(row=1, column=1, padx=10, pady=10)

        self.label_email = ctk.CTkLabel(self.frame_registro, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_email = ctk.CTkEntry(self.frame_registro)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        self.label_ventas = ctk.CTkLabel(self.frame_registro, text="Ventas:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_ventas = ctk.CTkEntry(self.frame_registro)
        self.entry_ventas.grid(row=3, column=1, padx=10, pady=10)
        
        self.boton_registrar = ctk.CTkButton(self.frame_registro, text="Registrar Vendedor", command=self.registrar_vendedor)
        self.boton_registrar.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

    def registrar_vendedor(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()
        email = self.entry_email.get()
        ventas = self.entry_ventas.get()
        
        try:
            self.gestor_vendedor.registrar_vendedor(nombre, telefono, email, ventas)
            self.rellenar_tabla()
            print("Vendedor registrado con éxito.")
        except Exception as e:
            print(f"Error al registrar el vendedor: {e}")

    def listar_vendedores(self):
        self.vendedores = self.gestor_vendedor.listar_vendedores()
