from src.reports.base import ReporteBase

class ReportePorSala(ReporteBase):
    def generar(self, salas: dict) -> str:
        salida = ["📊 Reporte por Sala:\n"]
        for nombre in sorted(salas.keys()):
            sala = salas[nombre]
            salida.append(f"Sala: {sala.nombre}")
            salida.append(f"  - Temperatura promedio: {sala.temperatura_promedio():.2f}°C")
            salida.append(f"  - Humedad promedio: {sala.humedad_promedio():.2f}%")
            salida.append(f"  - CO₂ promedio: {sala.co2_promedio():.2f} ppm\n")
        return "\n".join(salida)
