from src.reports.base import ReporteBase

class ReporteLogsRecientes(ReporteBase):
    def generar(self, cache, logs) -> str:
        salida = ["🕒 Logs recientes por sala (últimos 5 minutos)\n" + "=" * 40]
        salas = sorted(set(log.sala for log in logs))
        hay_logs = False

        for sala in salas:
            logs_recientes = cache.obtener_por_sala(sala)
            if logs_recientes:
                hay_logs = True
                salida.append(f"\nSala: {sala} - {len(logs_recientes)} logs encontrados:")
                for log in logs_recientes[:3]:
                    salida.append(f"  - {log}")

        if not hay_logs:
            salida.append("\nNo se encontraron logs recientes en ninguna sala.")

        return "\n".join(salida)
