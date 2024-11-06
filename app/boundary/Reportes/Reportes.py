import customtkinter as ctk
from ...reports import ReporteIngresosTotales, ReporteVentasAutos, ReporteVentasPeriodo


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
        # botones de reportes
        self.btn_rp_ventas_periodo = ctk.CTkButton(
            line2_frame, text="Reporte de ventas", command=self.mostrar_modal_fechas)
        self.btn_rp_ventas_periodo.grid(
            row=0, column=0, padx=20, pady=20, sticky="w")

        self.btn_rp_ingresos = ctk.CTkButton(
            line2_frame, text="Reporte de ingresos", command=self.rp_ingresos)
        self.btn_rp_ingresos.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        self.btn_rp_ventas_autos_marca = ctk.CTkButton(
            line2_frame, text="Reporte de marcas populares", command=self.rp_ventas_autos_marca)
        self.btn_rp_ventas_autos_marca.grid(
            row=0, column=2, padx=20, pady=20, sticky="e")

    def salir_fullscreen(self, event=None):
        self.ventana.attributes("-fullscreen", False)
        self.ventana.geometry("1280x720")

    def mostrar_modal_fechas(self):
        self.modal = ctk.CTkToplevel(self.ventana)
        self.modal.title("Seleccionar rango de fechas")
        self.modal.geometry("400x400")
        self.modal.transient(self.ventana)
        self.modal.update()
        self.modal.grab_set()

        ctk.CTkLabel(self.modal, text="Fecha Desde").pack(pady=5)
        self.dia_desde = ctk.CTkEntry(self.modal, placeholder_text="Día")
        self.dia_desde.pack(pady=2)
        self.mes_desde = ctk.CTkEntry(self.modal, placeholder_text="Mes")
        self.mes_desde.pack(pady=2)
        self.ano_desde = ctk.CTkEntry(self.modal, placeholder_text="Año")
        self.ano_desde.pack(pady=2)

        ctk.CTkLabel(self.modal, text="Fecha Hasta").pack(pady=5)
        self.dia_hasta = ctk.CTkEntry(self.modal, placeholder_text="Día")
        self.dia_hasta.pack(pady=2)
        self.mes_hasta = ctk.CTkEntry(self.modal, placeholder_text="Mes")
        self.mes_hasta.pack(pady=2)
        self.ano_hasta = ctk.CTkEntry(self.modal, placeholder_text="Año")
        self.ano_hasta.pack(pady=2)

        line1_frame = ctk.CTkFrame(self.modal)
        line1_frame.pack(side="bottom", fill="x", pady=10, padx=10)
        confirmar_btn = ctk.CTkButton(
            line1_frame, text="Generar Reporte", command=self.rp_ventas_periodo)
        confirmar_btn.pack(side="left", pady=20, padx=10)
        cerrar_btn = ctk.CTkButton(
            line1_frame, text="Cancelar", fg_color="red", command=self.modal.destroy)
        cerrar_btn.pack(side="right", pady=20, padx=10)

    def rp_ventas_periodo(self):
        dia_desde = self.dia_desde.get()
        mes_desde = self.mes_desde.get()
        ano_desde = self.ano_desde.get()
        dia_hasta = self.dia_hasta.get()
        mes_hasta = self.mes_hasta.get()
        ano_hasta = self.ano_hasta.get()
        self.modal.destroy()
        try:
            fecha_desde = f"{dia_desde}/{mes_desde}/{ano_desde}"
            fecha_hasta = f"{dia_hasta}/{mes_hasta}/{ano_hasta}"
            rp_ventas_periodo = ReporteVentasPeriodo.ReporteVentasPeriodo(
                fecha_desde, fecha_hasta)
            rp_location = rp_ventas_periodo.generar_reporte()
            self.mostrar_modal_confirmacion(
                f"Reporte generado exitosamente. \n Visible en: '{rp_location}'")
        except Exception:
            self.mostrar_modal_confirmacion("Error al generar el reporte.")
            print(Exception)

    def rp_ingresos(self):
        try:
            rp_ingresos = ReporteIngresosTotales.ReporteIngresosTotales()
            rp_location = rp_ingresos.generar_reporte()
            self.mostrar_modal_confirmacion(
                f"Reporte generado exitosamente. \n Visible en: '{rp_location}'")
        except Exception:
            self.mostrar_modal_confirmacion("Error al generar el reporte.")
            print(Exception)
            

    def rp_ventas_autos_marca(self):
        try:
            rp_ventas_autos_marca = ReporteVentasAutos.ReporteVentasAutos()
            rp_location = rp_ventas_autos_marca.generar_reporte()
            self.mostrar_modal_confirmacion(
                f"Reporte generado exitosamente. \n Visible en: '{rp_location}'")
        except Exception:
            self.mostrar_modal_confirmacion("Error al generar el reporte.")
            print(Exception)
            

    def mostrar_modal_confirmacion(self, mensaje):
        self.modal = ctk.CTkToplevel(self.ventana)
        self.modal.title("Generación de reporte")
        self.modal.geometry("600x150")
        self.modal.transient(self.ventana)
        self.modal.update()
        self.modal.grab_set()

        label = ctk.CTkLabel(self.modal, text=mensaje)
        label.pack(pady=20)
        cerrar_btn = ctk.CTkButton(self.modal, text="Cerrar", command=self.modal.destroy)
        cerrar_btn.pack(side="bottom", pady=10, padx=20, fill="x")
