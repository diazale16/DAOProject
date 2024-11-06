import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from ...control.GestorVenta import GestorVenta

class ModificacionVenta:
    def __init__(self, adm_venta_instance, data):
        self.gestor_venta = GestorVenta()
        self.adm_venta_instance = adm_venta_instance
        self.data = data
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTkToplevel(adm_venta_instance.ventana)
        self.ventana.geometry("300x400")
        self.ventana.resizable(False, False)
        self.initialize_modificacion()
        self.create_widgets()
        self.ventana.grab_set()

    def initialize_modificacion(self):
        self.frame_modif = ctk.CTkFrame(self.ventana)
        self.frame_modif.pack(fill="both", expand=True)

    def create_widgets(self):
        # Entrada para la fecha
        self.label_fecha = ctk.CTkLabel(self.frame_modif, text="Fecha:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_fecha = ctk.CTkEntry(self.frame_modif)
        self.entry_fecha.insert(0, self.data[1])
        self.entry_fecha.grid(row=0, column=1, padx=10, pady=10)

        # Entrada para el código VIN
        self.label_auto = ctk.CTkLabel(self.frame_modif, text="Código VIN:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_auto = ctk.CTkEntry(self.frame_modif)
        self.entry_auto.insert(0, self.data[2])
        self.entry_auto.grid(row=1, column=1, padx=10, pady=10)

        # Entrada para el ID Cliente
        self.label_cliente = ctk.CTkLabel(self.frame_modif, text="ID Cliente:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_cliente = ctk.CTkEntry(self.frame_modif)
        self.entry_cliente.insert(0, self.data[3])
        self.entry_cliente.grid(row=2, column=1, padx=10, pady=10)

        # Entrada para el ID Vendedor
        self.label_vendedor = ctk.CTkLabel(self.frame_modif, text="ID Vendedor:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_vendedor = ctk.CTkEntry(self.frame_modif)
        self.entry_vendedor.insert(0, self.data[4])
        self.entry_vendedor.grid(row=3, column=1, padx=10, pady=10)

        # Botón para modificar la venta
        self.boton_modificar = ctk.CTkButton(self.frame_modif, text="Modificar Venta", command=self.modificar_venta)
        self.boton_modificar.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

    def modificar_venta(self):
        # Obtener valores ingresados
        fecha_str = self.entry_fecha.get()
        vin = self.entry_auto.get()
        cliente_id = self.entry_cliente.get()
        vendedor_id = self.entry_vendedor.get()

        try:
            # Convertir la fecha
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()

            # Verificar que IDs existan
            self.gestor_venta.validar_ids(cliente_id, vendedor_id, vin)

            # Llamar al método de modificación
            self.gestor_venta.modificar_venta(self.data[0], fecha, cliente_id, vendedor_id)
            messagebox.showinfo("Éxito", "Venta modificada con éxito.")
            
            # Cerrar la ventana y refrescar la tabla
            self.ventana.destroy()
            self.adm_venta_instance.rellenar_tabla()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Error al modificar la venta: {e}")

    def show(self):
        self.ventana.mainloop()
