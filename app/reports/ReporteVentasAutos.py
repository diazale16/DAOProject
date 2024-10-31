from . import ReporteBase
from ..control.GestorVenta import GestorVenta
from ..entities.VentaModel import Venta
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import renderPM
from reportlab.lib import colors
import os
from io import BytesIO


class ReporteVentasAutos(ReporteBase.ReporteBase):
    def __init__(self):
        self.fecha_hoy = datetime.today().strftime("%d / %m / %Y")
        self.nom_doc = "reporte_ventas_autos_marca"
        self.title = f"Reporte de autos vendidos por marca"

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

        text = f"Reporte de autos mas vendidos por marca."
        self.contenido["datos"].append(Paragraph(text, styles['Normal']))

        self.contenido["datos"].append(Spacer(10, 10))
        rt_content = self.construccion_contenido()
        for c in rt_content:
            self.contenido["datos"].append(c)

        return self.contenido

    def segregated_data_template(self, ventas: list[Venta]):
        template = {}
        marcas = {v.auto.marca for v in ventas}
        for m in marcas:
            template[m] = 0
        return template

    def get_data(self):
        # data
        gestor_ventas = GestorVenta()
        ventas: list[Venta] = gestor_ventas.listar_ventas()
        data_segregada = self.segregated_data_template(ventas)
        # ventas
        for v in ventas:
            data_segregada[v.auto.marca] += 1
        return data_segregada

    def hsl_to_rgb(self, h, s, l):
        r, g, b = 0, 0, 0
        if s == 0:  # Achromatic
            r = g = b = l  # grey
        else:
            def hue_to_rgb(p, q, t):
                if t < 0: t += 1
                if t > 1: t -= 1
                if t < 1/6: return p + (q - p) * 6 * t
                if t < 1/2: return q
                if t < 2/3: return p + (q - p) * (2/3 - t) * 6
                return p
            
            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            r = hue_to_rgb(p, q, h + 1/3)
            g = hue_to_rgb(p, q, h)
            b = hue_to_rgb(p, q, h - 1/3)
        
        return colors.Color(r, g, b)

    def crear_grafico_torta(self, data):
        labels = list(data.keys())
        values = list(data.values())
        
        grafico = Drawing(200, 200)
        pie = Pie()
        pie.x = 50
        pie.y = 50
        pie.data = values
        pie.labels = labels
        
        pie.slices.strokeWidth = 0.5

        # Generar colores dinámicamente
        num_colors = len(pie.data)
        for index in range(num_colors):
            # Calcular el color usando HSL
            h = index / num_colors  # Matiz basado en el índice
            s = 0.7  # Saturación
            l = 0.5  # Luminosidad
            pie.slices[index].fillColor = self.hsl_to_rgb(h, s, l)

        grafico.add(pie)

        return grafico

    def construccion_contenido(self):
        rtn_content = []
        marcas_cont = self.get_data()

        # tabla
        data = [["Categoria", "Total"]]
        for c, v in marcas_cont.items():
            data.append([c, v])
        table = Table(data, colWidths=[1.5 * inch, 1.5 * inch])
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                   ('BACKGROUND', (0, 1),
                                    (-1, -1), colors.whitesmoke),
                                   ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        rtn_content.append(table)
        rtn_content.append(Spacer(10, 10))
        

        # graficos
        graf = self.crear_grafico_torta(marcas_cont)
        renderPM.drawToFile(graf, "resources/images/pie_chart_marcas.png", fmt='PNG')
        image = Image("resources/images/pie_chart_marcas.png")
        image.hAlign = 'CENTER'
        rtn_content.append(image)

        return rtn_content