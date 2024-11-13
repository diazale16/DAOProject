import customtkinter as ctk
from ...control.GestorCliente import GestorCliente

class ModificacionCliente:
    def __init__(self, adm_cliente_instance, data):
        self.gestor_cliente = GestorCliente()
        self.adm_cliente_instance = adm_cliente_instance
        self.data = data
        self.cliente_id = data[0]
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTkToplevel(adm_cliente_instance)
        self.ventana.geometry("300x500")
        self.ventana.resizable(False, False)
        self.initialize_modificacion()
        self.create_widgets()
        self.ventana.grab_set()
    
    def initialize_modificacion(self):
        self.frame_modif = ctk.CTkFrame(self.ventana)
        self.frame_modif.pack(fill="both", expand=True)        

    def create_widgets(self):
        # Etiqueta y entrada para el nombre
        self.label_nombre = ctk.CTkLabel(self.frame_modif, text="Nombre:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_modif)
        self.entry_nombre.insert(0, self.data[1])
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)
        # Etiqueta y entrada para el apellido
        self.label_apellido = ctk.CTkLabel(self.frame_modif, text="Apellido:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_apellido = ctk.CTkEntry(self.frame_modif)
        self.entry_apellido.insert(0, self.data[2])
        self.entry_apellido.grid(row=2, column=1, padx=10, pady=10)
       
        # Campos para la dirección
        self.label_calle = ctk.CTkLabel(self.frame_modif, text="Calle:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_calle = ctk.CTkEntry(self.frame_modif)
        self.entry_calle.insert(0, self.data[3].split(',')[0])
        self.entry_calle.grid(row=3, column=1, padx=10, pady=10)

        self.label_numero = ctk.CTkLabel(self.frame_modif, text="Número:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_numero = ctk.CTkEntry(self.frame_modif)
        self.entry_numero.insert(0, self.data[3].split(',')[1])
        self.entry_numero.grid(row=4, column=1, padx=10, pady=10)

        self.label_localidad = ctk.CTkLabel(self.frame_modif, text="Localidad:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.entry_localidad = ctk.CTkEntry(self.frame_modif)
        longitud = len(self.data[3].split(','))
        if(longitud > 2):
            self.entry_localidad.insert(0, self.data[3].split(',')[2])
        else:
           self.entry_localidad.insert(0, '')
         #agregar metodo split
        self.entry_localidad.grid(row=5, column=1, padx=10, pady=10)

        # Etiqueta y entrada para el telefono
        self.label_telefono = ctk.CTkLabel(self.frame_modif, text="Telefono:").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.entry_telefono = ctk.CTkEntry(self.frame_modif)
        self.entry_telefono.insert(0, self.data[4])
        self.entry_telefono.grid(row=7, column=1, padx=10, pady=10)
        
        # Botón para registrar el cliente
        self.boton_registrar = ctk.CTkButton(self.frame_modif, text="Modificar Cliente", command=self.modificar_cliente)
        self.boton_registrar.grid(row=8, column=0, columnspan=2, padx=10, pady=20)

    def modificar_cliente(self):
        self.nombre = self.entry_nombre.get()
        self.apellido = self.entry_apellido.get()
        self.calle = self.entry_calle.get()
        self.numero = self.entry_numero.get()
        self.localidad = self.entry_localidad.get()
        self.telefono = self.entry_telefono.get()
        self.direccion = f"{self.calle}, {self.numero}, {self.localidad}"
        # self.cliente_id = self.entry_cliente.get() if self.entry_cliente.get() else None
        self.gestor_cliente.modificar_cliente(self.cliente_id, self.nombre, self.apellido, self.direccion, self.telefono)
        self.ventana.destroy()
        
    def show(self):
        self.ventana.mainloop()