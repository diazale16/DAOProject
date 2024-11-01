import customtkinter as ctk
from customtkinter import CTkImage
from ...reports import ReporteIngresosTotales, ReporteVentasAutos, ReporteVentasPeriodo
from PIL import Image
import fitz


class Reportes:
    def __init__(self, home_instance):
        ctk.set_appearance_mode("dark")
        self.ventana = ctk.CTk()
        self.home_instance = home_instance
        self.ventana.geometry(f"1280x720")
        self.ventana.attributes("-zoomed", True)
        self.ventana.bind("<Escape>", self.salir_fullscreen)
        self.ventana.protocol("WM_DELETE_WINDOW", self.home)
        self.header()
        self.initialize_widgets()

    def home(self):
        self.ventana.destroy()
        self.home_instance.ventana.deiconify()

    def show(self):
        self.ventana.mainloop()

    def header(self):
        line1_frame = ctk.CTkFrame(self.ventana)
        line1_frame.pack(side="top", fill="x", pady=5)
        self.boton_home = ctk.CTkButton(
            line1_frame, text="Home", command=self.home
        )
        self.boton_home.pack(side="left", fill="y")

    def initialize_widgets(self):
        line2_frame = ctk.CTkFrame(self.ventana)
        line2_frame.pack(side="top", fill="x", pady=5)

        line2_frame.columnconfigure(0, weight=1)
        line2_frame.columnconfigure(1, weight=1)
        line2_frame.columnconfigure(2, weight=1)

        self.rp_ventas_periodo = ctk.CTkButton(
            line2_frame, text="Reporte de ventas", command=self.rp_ventas_periodo)
        self.rp_ventas_periodo.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.rp_ingresos = ctk.CTkButton(
            line2_frame, text="Reporte de ingresos", command=self.rp_ingresos)
        self.rp_ingresos.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        self.rp_ventas_autos_marca = ctk.CTkButton(
            line2_frame, text="Reporte de marcas populares", command=self.rp_ventas_autos_marca)
        self.rp_ventas_autos_marca.grid(row=0, column=2, padx=20, pady=20, sticky="e")

    def salir_fullscreen(self, event=None):
        self.ventana.attributes("-fullscreen", False)
        self.ventana.geometry("1280x720")

    def rp_ventas_periodo(self):
        rp_ventas_periodo = ReporteVentasPeriodo.ReporteVentasPeriodo()
        rp_location = rp_ventas_periodo.generar_reporte()
        # self.pdfviewer(rp_location)

    def rp_ingresos(self):
        rp_ingresos = ReporteIngresosTotales.ReporteIngresosTotales()
        rp_location = rp_ingresos.generar_reporte()
        # self.pdfviewer(rp_location)

    def rp_ventas_autos_marca(self):
        rp_ventas_autos_marca = ReporteVentasAutos.ReporteVentasAutos()
        rp_location = rp_ventas_autos_marca.generar_reporte()
        # self.pdfviewer(rp_location)

    # def pdfviewer(self, pdf_path):
    #     self.pdf_document = fitz.open(pdf_path)
    #     self.current_page = 0

    #     self.image_label = ctk.CTkLabel(self.ventana, text="")
    #     self.image_label.pack(expand=True, fill="both")

    #     self.prev_button = ctk.CTkButton(self.ventana, text="Página Anterior", command=self.previous_page)
    #     self.prev_button.pack(side="left", padx=10, pady=10)
    #     self.next_button = ctk.CTkButton(self.ventana, text="Página Siguiente", command=self.next_page)
    #     self.next_button.pack(side="right", padx=10, pady=10)

    #     self.display_page(self.current_page)

    # def display_page(self, page_num):
    #     page = self.pdf_document[page_num]
    #     pix = page.get_pixmap()
        
    #     # Asegúrate de que pix no sea None
    #     if pix is None:
    #         print("Error: No se pudo obtener la imagen de la página.")
    #         return

    #     img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    #     img.thumbnail((800, 600))

    #     # Crea la imagen de CustomTkinter
    #     self.photo = CTkImage(img)
        
    #     # Configura la etiqueta de imagen
    #     self.image_label.configure(image=self.photo)
    #     self.image_label.image = self.photo  # Mantén la referencia

    # def next_page(self):
    #     if self.current_page < self.pdf_document.page_count - 1:
    #         self.current_page += 1
    #         self.display_page(self.current_page)

    # def previous_page(self):
    #     if self.current_page > 0:
    #         self.current_page -= 1
    #         self.display_page(self.current_page)
