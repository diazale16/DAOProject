from . import ReporteBase
from ..control.GestorVenta import GestorVenta
from ..entities.VentaModel import Venta
from datetime import datetime
from reportlab.lib import colors
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer


class ReporteVentasPeriodo(ReporteBase.ReporteBase):
    def __init__(self, fecha_desde, fecha_hasta):
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.fecha_hoy = datetime.today().strftime("%d / %m / %Y")
        self.nom_doc = "reporte_ventas_periodo"
        self.title = f"Reporte de ventas"

    def obtener_contenido(self):
        self.contenido = {}
        self.contenido["datos"] = []
        styles = getSampleStyleSheet()
        # Agregar el nombre del documento
        self.contenido["nom_doc"] = self.nom_doc
        # Agregar un título
        self.contenido["datos"].append(Paragraph(self.title, styles['Title']))
        self.contenido["datos"].append(Spacer(10, 10))

        text = f"Fecha de emisión: [ {self.fecha_hoy} ] "
        self.contenido["datos"].append(Paragraph(text, styles['Heading2']))

        fecha_desde_formated = self.fecha_desde.strftime("%d / %m / %Y")
        fecha_hasta_formated = self.fecha_hasta.strftime("%d / %m / %Y")
        text = f"Periodo de búsqueda: [ {fecha_desde_formated} ] - [ {fecha_hasta_formated} ]"
        self.contenido["datos"].append(Paragraph(text, styles['Heading2']))

        text = f"Reporte de ventas realizadas en un periodo de tiempo definido."
        self.contenido["datos"].append(Paragraph(text, styles['Normal']))

        self.contenido["datos"].append(Spacer(10, 10))
        table = self.construccion_contenido()
        self.contenido["datos"].append(table)

        return self.contenido

    def get_data(self):
        gestor_ventas = GestorVenta()
        ventas: list[Venta] = gestor_ventas.listar_ventas()
        ventas_en_periodo = [venta for venta in ventas if (
            venta.fecha >= self.fecha_desde and venta.fecha <= self.fecha_hasta)]
        return ventas_en_periodo

    def construccion_contenido(self):
        ventas: list[Venta] = self.get_data()
        # tabla
        data = [["Venta ID", "Fecha", "Cliente", "Vendedor", "Auto", "Monto"]]
        for venta in ventas:
            data.append([
                f"{venta.id}",
                f"{venta.fecha}",
                f"{venta.cliente.nombre} {venta.cliente.apellido}",
                f"{venta.vendedor.nombre} {venta.vendedor.apellido}",
                f"{venta.auto.marca} {venta.auto.modelo} {venta.auto.año}",
                f"{venta.monto}"
            ])
        table = Table(data, colWidths=[
                      1 * inch, 1 * inch, 1.2 * inch, 1.2 * inch, 2 * inch, 1.2 * inch])
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                   ('BACKGROUND', (0, 1),
                                    (-1, -1), colors.whitesmoke),
                                   ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        return table
