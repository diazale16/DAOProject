from . import ReporteBase
from ..control import GestorVenta, GestorServicio, GestorComision
from ..entities.VentaModel import Venta
from ..entities.ServicioModel import Servicio
from ..entities.ComisionModel import Comision
from ..entities.VentaModel import Venta
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics import renderPDF
from reportlab.platypus import Flowable
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.graphics import renderPM
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors
from io import BytesIO


class ReporteIngresosTotales(ReporteBase.ReporteBase):
    def __init__(self):
        self.fecha_hoy = datetime.today().strftime("%d / %m / %Y")
        self.nom_doc = "reporte_ingresos_totales"
        self.title = f"Reporte de ventas"

    def obtener_contenido(self):
        self.contenido = {}
        self.contenido["datos"] = []
        self.styles = getSampleStyleSheet()
        # Agregar el nombre del documento
        self.contenido["nom_doc"] = self.nom_doc
        # Agregar un título
        self.contenido["datos"].append(Paragraph(self.title, self.styles['Title']))
        self.contenido["datos"].append(Spacer(10, 10))

        text = f"Fecha de emisión: [ {self.fecha_hoy} ] "
        self.contenido["datos"].append(Paragraph(text, self.styles['Heading2']))

        text = f"Reporte de ingresos provenientes de ventas de autos y servicios post-venta para los mismos."
        self.contenido["datos"].append(Paragraph(text, self.styles['Normal']))

        self.contenido["datos"].append(Spacer(10, 10))
        rt_content = self.construccion_contenido()
        for c in rt_content:
            self.contenido["datos"].append(c)

        return self.contenido

    def segregated_data_template(self, ventas: list[Venta], servicios: list[Servicio]):
        template = {}

        años_ventas = {v.fecha.year for v in ventas}
        años_servicios = {s.fecha.year for s in servicios}
        años = años_ventas.union(años_servicios)

        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        months_dict = {m: 0 for m in months}

        for año in años:
            template[año] = months_dict

        return template

    def get_data(self):
        # data
        gestor_ventas = GestorVenta.GestorVenta()
        ventas: list[Venta] = gestor_ventas.listar_ventas()
        gestor_servicio = GestorServicio.GestorServicio()
        servicios: list[Servicio] = gestor_servicio.listar_servicios()
        data_segregada = self.segregated_data_template(ventas, servicios)
        # vars
        ingreso_total = ingreso_ventas = ingreso_servicios = total_comisiones = 0
        # ventas
        for v in ventas:
            ingreso_ventas += v.monto
            ingreso_total += v.monto
            data_segregada[v.fecha.year][v.fecha.month] += int(v.monto)
        # servicios
        for s in servicios:
            ingreso_servicios += s.costo
            ingreso_total += s.costo
            data_segregada[s.fecha.year][s.fecha.month] += int(s.costo)
        # comisiones
        gestor_comisiones = GestorComision.GestorComision()
        comisiones: list[Comision] = gestor_comisiones.listar_comisiones()
        for c in comisiones:
            total_comisiones += c.monto
        return {
            "Ventas": round(ingreso_ventas, 3),
            "Servicios": round(ingreso_servicios, 3),
            "Total neto": round(ingreso_total, 3),
            " --- ": " --- ",
            "Comisiones": round(total_comisiones, 3),
            "Total bruto": round(ingreso_total + total_comisiones, 3)
        }, data_segregada

    def crear_grafico_barras(self, año: int, data_mes: dict):
        valores = [v for v in data_mes.values()]

        grafico = Drawing(400, 300)
        chart = VerticalBarChart()
        chart.x = 50
        chart.y = 50
        chart.height = 200
        chart.width = 300

        # Configuración de los datos del gráfico
        chart.data = [list(data_mes.values())]  # Convertir a lista
        chart.categoryAxis.categoryNames = [
            'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        chart.valueAxis.valueMin = 0  # Valor mínimo del eje Y
        chart.valueAxis.valueMax = max(data_mes.values()) + (max(data_mes.values()) * 0.1)
        chart.valueAxis.valueStep = max(data_mes.values()) // 10
        chart.barWidth = 10
        chart.groupSpacing = 10

        # Asignar colores a las barras
        for index in range(len(chart.data[0])):
            chart.bars[index].fillColor = colors.Color(index / len(chart.data[0]), 0.5, 0.5)  # Color dinámico

        grafico.add(chart)

        # Agregar valores sobre las barras
        for index, value in enumerate(valores):
            x = chart.x + (chart.barWidth + chart.groupSpacing) * index + chart.barWidth / 2  # Calcular la posición X
            y = chart.y + chart.height + 5  # Posición Y para el texto (un poco arriba de la barra)
            grafico.add(String(x, y, str(value), textAnchor='middle', fontSize=10, fillColor=colors.black))

        return grafico
    

    def construccion_contenido(self):
        rtn_content = []
        montos, graf_source = self.get_data()

        # tabla
        data = [["Categoria", "Total"]]
        for c, v in montos.items():
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
        rtn_content.append(PageBreak())
        

        # graficos
        for año, data_mes in graf_source.items():
            text = f"Ingresos mensuales para el año {año}"
            rtn_content.append(Paragraph(text, self.styles['Heading5']))
            graf = self.crear_grafico_barras(año, data_mes)
            renderPM.drawToFile(graf, f"resources/images/bar_chart_ingresos_{año}.png", fmt='PNG')
            image = Image(f"resources/images/bar_chart_ingresos_{año}.png")
            image.hAlign = 'CENTER'
            rtn_content.append(graf)
            rtn_content.append(Spacer(10, 10))
            

        return rtn_content
