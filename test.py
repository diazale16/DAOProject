import customtkinter as ctk
from tkinter import ttk
from app.persistency.DBManager import DBManager
from app.services.AutoService import AutoService
from app.entities.AutoModel import Auto
import DBLoader

# Configuración de la ventana principal
root = ctk.CTk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Frame para el listado de elementos
frame_lista = ctk.CTkFrame(root)
frame_lista.pack(side="top", padx=10, pady=10,  fill="both", expand=True)
# frame_lista.grid_columnconfigure()

# Crear el Treeview con columnas
# tree = ttk.Treeview(frame_lista, columns=("ID", "Nombre"), show="headings")
# tree.heading("ID", text="ID")
# tree.heading("Nombre", text="Nombre")
# tree.pack(side="left", fill="both", expand=True)
tree = ttk.Treeview(frame_lista, columns=("VIN", "Marca", "Modelo", "Año", "Precio", "Estado", "Cliente"), show="headings")
tree.heading("VIN", text="VIN")
tree.heading("Marca", text="Marca")
tree.heading("Modelo", text="Modelo")
tree.heading("Año", text="Año")
tree.heading("Precio", text="Precio")
tree.heading("Estado", text="Estado")
tree.heading("Cliente", text="Cliente")
tree.pack(side="top", fill="both", expand=True)

# Definir una función para rellenar la tabla con una lista de elementos
def rellenar_tabla(lista_elementos):
    # Limpiar la tabla antes de insertar nuevos datos
    tree.delete(*tree.get_children())
    # Insertar los datos
    for item in lista_elementos:
        tree.insert("", "end", values=item)

# Datos de ejemplo
# DBLoader.main()
data = []
auto_service = AutoService()
autos = auto_service.listar_autos()
for auto in autos:
    if isinstance(auto, Auto):
        if not (auto.cliente_relacion):
            tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado_relacion.nombre, None)
        else:
            tupla = (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado_relacion.nombre, f"{auto.cliente_relacion.nombre} {auto.cliente_relacion.apellido}")
        data.append(tupla)
rellenar_tabla(data)

# Frame para los detalles del elemento seleccionado
frame_detalles = ctk.CTkFrame(root)
frame_detalles.pack(side="bottom", fill="both", expand=True)

# Función para mostrar detalles
def mostrar_detalles(event):
    item_seleccionado = tree.selection()
    if item_seleccionado:
        valores = tree.item(item_seleccionado, "values")
        detalles.configure(text=f"Detalles de: {valores[1]}")

# Cuadro de detalles
detalles = ctk.CTkLabel(frame_detalles, text="Selecciona un elemento para ver los detalles")
detalles.pack(pady=10)

# Vincular evento de selección a la función de mostrar detalles
tree.bind("<<TreeviewSelect>>", mostrar_detalles)

root.mainloop()
