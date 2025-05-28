from src.reports.base import ReporteBase

class ReporteAlertas(ReporteBase):
    def generar(self, salas: dict) -> str:
        salida = ["🚨 Reporte de Alertas:\n"]
        for sala in salas.values():
            alertas = sala.alertas()
            if alertas:
                salida.append(f"Sala: {sala.nombre} - {len(alertas)} alertas encontradas")
                for alerta in alertas[:3]:  # Mostramos solo las primeras 3 por sala
                    salida.append(f"  [{alerta.timestamp}] Sala: {alerta.sala} - Temp: {alerta.temperatura}°C, Humedad: {alerta.humedad}%, CO₂: {alerta.co2}ppm")
                salida.append("")
        return "\n".join(salida)
