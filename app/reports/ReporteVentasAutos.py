from . import ReporteBase
from ..control.GestorVenta import GestorVenta
from ..entities.VentaModel import Venta
from datetime import datetime
from reportlab.lib import colors
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, Image
import matplotlib.pyplot as plt


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

   
    def crear_grafico_torta(self, data: dict, filename: str):
        labels = list(data.keys())
        sizes = list(data.values())

        plt.figure(figsize=(5, 5))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Distribución de autos vendidos por marca")
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

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
        filename = f"resources/images/pie_chart_marcas.png"
        self.crear_grafico_torta(marcas_cont, filename)
        image = Image(filename)
        image.hAlign = 'CENTER'
        rtn_content.append(image)

        return rtn_content
