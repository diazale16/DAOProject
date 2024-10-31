from app.reports.ReporteVentasPeriodo import ReporteVentasPeriodo
from app.reports.ReporteIngresosTotales import ReporteIngresosTotales
from app.reports.ReporteVentasAutos import ReporteVentasAutos
from datetime import datetime


# reporte ventas
fecha_desde = "1/1/2024"
fecha_hasta = "11/11/2024"

fecha_desde = datetime.strptime(fecha_desde, "%d/%m/%Y").date()
fecha_hasta = datetime.strptime(fecha_hasta, "%d/%m/%Y").date()

reporte = ReporteVentasPeriodo(fecha_desde=fecha_desde, fecha_hasta=fecha_hasta)
reporte.generar_reporte()


# reporte ingresos
reporte = ReporteIngresosTotales()
reporte.generar_reporte()


# reporte venta de autos por marca
reporte = ReporteVentasAutos()
reporte.generar_reporte()

