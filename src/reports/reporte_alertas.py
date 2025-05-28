from src.models.sala import Sala
from src.models.log import Log

class ReporteAlertas:
    def __init__(self, temp_max=30.0, co2_max=1000.0):
        self.temp_max = temp_max
        self.co2_max = co2_max

    def generar(self, salas: dict) -> str:
        salida = ["🚨 Reporte de Alertas:\n"]

        for nombre, sala in salas.items():
            alertas = [
                log for log in sala.logs
                if log.temperatura > self.temp_max or log.co2 > self.co2_max
            ]

            if alertas:
                salida.append(f"Sala: {nombre} - {len(alertas)} alertas encontradas")
                for log in alertas[:3]:  # Solo mostramos las 3 primeras alertas por sala
                    salida.append(f"  {log}")
                salida.append("")

        if len(salida) == 1:
            salida.append("✅ No se encontraron alertas.")

        return "\n".join(salida)
