from abc import ABC, abstractmethod
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image




class ReporteBase(ABC):
    def generar_reporte(self):
        self.report_path = "resources/reports"
        self.pagesize = A4
        self.contenido = self.obtener_contenido()
        self.doc, filename = self.crear_reporte(self.report_path, self.contenido["nom_doc"])
        self.guardar_reporte(self.contenido["datos"])
        return filename
        # self.exponer_reporte()

    @abstractmethod
    def obtener_contenido(self):
        pass

    @abstractmethod
    def get_data(self):
        pass
    
    @abstractmethod
    def construccion_contenido(self):
        pass

    def crear_reporte(self, path, nom_doc):
        filename = f"{path}/{nom_doc}.pdf"
        doc = SimpleDocTemplate(filename, pagesize=self.pagesize)
        return doc, filename

    def guardar_reporte(self, contenido):
        self.doc.build(contenido)

    # def exponer_reporte(self):
    #     # Exponer o imprimir el reporte
    #     print(f"Reporte '{self.nombre}' generado y guardado exitosamente en formato PDF.")
