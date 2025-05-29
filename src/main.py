from src.loaders.load_logs import cargar_logs_desde_csv
from src.utils.group_logs_by_sala import agrupar_logs_por_sala
from src.models.cache import CacheLogs
from src.reports.reporte_por_sala import ReportePorSala
from src.reports.reporte_alertas import ReporteAlertas

if __name__ == "__main__":
    ruta = "data/logs_ambientales_ecowatch.csv"
    logs = cargar_logs_desde_csv(ruta)

    # Creamos y cargamos la caché con los logs de los últimos 5 minutos
    cache = CacheLogs()
    for log in logs:
        cache.agregar_log(log)

    # Agrupamos los logs por sala
    salas = agrupar_logs_por_sala(logs)

    # Reporte estadístico
    print("\n📊 Reporte Estadístico\n" + "=" * 22)
    print(ReportePorSala().generar(salas))

    # Reporte de alertas
    print("\n🚨 Reporte de Alertas\n" + "=" * 22)
    print(ReporteAlertas().generar(salas))

    # Estado de la caché
    print(f"\n🧠 Estado de la caché: {cache}")
