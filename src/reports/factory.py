from src.reports.reporte_por_sala import ReportePorSala
from src.reports.reporte_alertas import ReporteAlertas

def crear_reporte(tipo: str):
    if tipo == "estadisticas":
        return ReportePorSala()
    elif tipo == "alertas":
        return ReporteAlertas()
    else:
        raise ValueError(f"Tipo de reporte desconocido: {tipo}")
