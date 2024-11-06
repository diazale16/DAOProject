import customtkinter as ctk
from tkinter import ttk, messagebox
from ...control.GestorVenta import GestorVenta
from ...control.GestorAuto import GestorAuto
from ...control.GestorCliente import GestorCliente
from .ModificacionVenta import ModificacionVenta
from datetime import datetime

class AdministracionVenta:
    def __init__(self, home_instance):
        self.gestor_venta = GestorVenta()
        self.gestor_auto = GestorAuto()
        self.gestor_cliente = GestorCliente()
        self.home_instance = home_instance
        self.ventana = ctk.CTkToplevel()
        
        # Configuraciones generales de la ventana
        self.ventana.geometry("1280x720")  
        ctk.set_appearance_mode("dark")
        self.ventana.state("zoomed")
        
        # Inicializar los componentes de la interfaz
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
        
        # Botón para refrescar la lista de ventas
        self.boton_refrescar = ctk.CTkButton(line1_frame, text="Refrescar", command=self.rellenar_tabla)
        self.boton_refrescar.pack(side="right", fill="y")

    def initialize_consulta(self):
        self.frame_lista = ctk.CTkFrame(self.ventana)
        self.frame_lista.pack(side="top", fill="both", padx=10, pady=10, expand=True)
        
        # Configuración de la tabla de ventas
        self.tree = ttk.Treeview(
            self.frame_lista,
            columns=("Id Venta", "Fecha Venta", "VIN Auto", "Id Cliente", "Id Vendedor"),
            show="headings",
        )
        self.tree.heading("Id Venta", text="Id Venta")
        self.tree.heading("Fecha Venta", text="Fecha Venta")
        self.tree.heading("VIN Auto", text="VIN Auto")
        self.tree.heading("Id Cliente", text="Id Cliente")
        self.tree.heading("Id Vendedor", text="Id Vendedor")
        self.tree.pack(side="top", fill="both", expand=True)
        
        # Botón de modificación ubicado debajo de la tabla
        self.boton_modificar = ctk.CTkButton(self.frame_lista, text="Modificar Venta", command=self.modificar_venta)
        self.boton_modificar.pack(side="bottom", fill="x", padx=10, pady=5)

        self.rellenar_tabla()

    def rellenar_tabla(self):
        self.listar_ventas()
        self.tree.delete(*self.tree.get_children())
        
        # Relleno de la tabla con los datos de las ventas
        for venta in self.ventas:
            venta_id = venta.id
            fecha = venta.fecha.strftime("%d/%m/%Y")  # Formateo de la fecha si es necesario
            auto = venta.auto_vin  # VIN del auto
            cliente = venta.cliente_id  # ID del cliente
            vendedor = venta.vendedor_id  # ID del vendedor
            
            self.tree.insert("", "end", values=(venta_id, fecha, auto, cliente, vendedor))

    def initialize_registro(self):
        self.frame_registro = ctk.CTkFrame(self.ventana)
        self.frame_registro.pack(side="left", fill="both", padx=10, pady=10, expand=True)
        
        # Configuración de campos para el registro de una nueva venta
        self.label_vin = ctk.CTkLabel(self.frame_registro, text="Código VIN:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_vin = ctk.CTkEntry(self.frame_registro)
        self.entry_vin.grid(row=0, column=1, padx=10, pady=10)

        self.label_cliente = ctk.CTkLabel(self.frame_registro, text="ID Cliente:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_cliente = ctk.CTkEntry(self.frame_registro)
        self.entry_cliente.grid(row=1, column=1, padx=10, pady=10)

        self.label_vendedor = ctk.CTkLabel(self.frame_registro, text="ID Vendedor:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_vendedor = ctk.CTkEntry(self.frame_registro)
        self.entry_vendedor.grid(row=2, column=1, padx=10, pady=10)

        self.label_fecha = ctk.CTkLabel(self.frame_registro, text="Fecha:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_fecha = ctk.CTkEntry(self.frame_registro)
        self.entry_fecha.grid(row=3, column=1, padx=10, pady=10)

        # Frame para los botones de "Eliminar" y "Registrar" debajo de los campos de entrada
        self.frame_botones = ctk.CTkFrame(self.frame_registro)
        self.frame_botones.grid(row=4, column=0, columnspan=2, pady=10)

        # Botón "Eliminar Venta"
        self.boton_eliminar = ctk.CTkButton(
            self.frame_botones,
            text="Eliminar Venta",
            command=self.eliminar_venta,
            fg_color="red",
            height=40,
            width=120,
            corner_radius=10
        )
        self.boton_eliminar.grid(row=0, column=0, padx=10)

        # Botón "Registrar Venta" al lado de "Eliminar Venta"
        self.boton_registrar = ctk.CTkButton(
            self.frame_botones,
            text="Registrar Venta",
            command=self.registrar_venta,
            fg_color="#FF5733",
            height=40,
            width=120,
            corner_radius=10,
            text_color="#FFFFFF"
        )
        self.boton_registrar.grid(row=0, column=1, padx=10)

    def registrar_venta(self):
        # Obtén el valor de la fecha desde el campo de entrada
        fecha = self.entry_fecha.get()
        vin = self.entry_vin.get()
        cliente = self.entry_cliente.get()
        vendedor = self.entry_vendedor.get()

        if not fecha:
            messagebox.showerror("Error", "La fecha no puede estar vacía.")
            return
        
        try:
            fecha_venta = datetime.strptime(fecha, "%d/%m/%Y").date()
            self.gestor_venta.registrar_venta(cliente, vendedor, vin, fecha_venta)
            self.rellenar_tabla()  # Refresca la tabla después de registrar la venta
            messagebox.showinfo("Éxito", "Venta registrada con éxito.")
            
        except ValueError as e:
            messagebox.showerror("Error en la fecha", f"Error en el formato de la fecha: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar la venta: {e}")

    def listar_ventas(self):
        self.ventas = self.gestor_venta.listar_ventas()

    def modificar_venta(self):
        item = self.tree.selection()
        if item:
            venta_seleccionada = self.tree.item(item, "values")
            mod_venta = ModificacionVenta(self, venta_seleccionada)
            mod_venta.show()
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una venta para modificar.")
    
    def eliminar_venta(self):
        item = self.tree.selection()
        if item:
            venta_seleccionada = self.tree.item(item, "values")
            venta_id = venta_seleccionada[0]
            try:
                self.gestor_venta.eliminar_venta(venta_id)
                self.rellenar_tabla()
                messagebox.showinfo("Éxito", "Venta eliminada con éxito.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar la venta: {e}")
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una venta para eliminar.")
