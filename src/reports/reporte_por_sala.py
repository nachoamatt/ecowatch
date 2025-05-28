from src.models.sala import Sala

class ReportePorSala:
    def generar(self, salas: dict) -> str:
        salida = ["📊 Reporte por Sala:\n"]

        for nombre, sala in salas.items():
            salida.append(f"Sala: {nombre}")
            salida.append(f"  - Temperatura promedio: {sala.temperatura_promedio():.2f}°C")
            salida.append(f"  - Humedad promedio: {sala.humedad_promedio():.2f}%")
            salida.append(f"  - CO₂ promedio: {sala.co2_promedio():.2f} ppm")
            salida.append("")

        return "\n".join(salida)
