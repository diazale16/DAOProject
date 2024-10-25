import customtkinter as ctk
from tkinter import ttk

# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("1280x720")

# Frame para el listado de elementos
frame_lista = ctk.CTkFrame(root)
frame_lista.pack(side="right", fill="both", expand=True)

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
tree.pack(side="left", fill="both", expand=False)

# Definir una función para rellenar la tabla con una lista de elementos
def rellenar_tabla(lista_elementos):
    # Limpiar la tabla antes de insertar nuevos datos
    tree.delete(*tree.get_children())
    
    # Insertar los datos
    for item in lista_elementos:
        tree.insert("", "end", values=item)

# Datos de ejemplo
data = [("1", "Elemento 1"), ("2", "Elemento 2"), ("3", "Elemento 3")]
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
