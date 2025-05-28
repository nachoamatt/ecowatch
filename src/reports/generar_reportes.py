from src.loaders.load_logs import cargar_logs_desde_csv
from src.utils.group_logs_by_sala import agrupar_logs_por_sala
from src.reports.factory import crear_reporte

if __name__ == "__main__":
    ruta = "data/logs_ambientales_ecowatch.csv"

    logs = cargar_logs_desde_csv(ruta)
    salas = agrupar_logs_por_sala(logs)

    print("\U0001F4CA Reporte Estadístico")
    print("======================")
    print(crear_reporte("estadisticas").generar(salas))

    print("\n🚨 Reporte de Alertas")
    print("======================")
    print(crear_reporte("alertas").generar(salas))
