from src.loaders.load_logs import cargar_logs_desde_csv
from src.utils.group_logs_by_sala import agrupar_logs_por_sala
from src.models.cache import CacheLogs
from src.reports.reporte_por_sala import ReportePorSala
from src.reports.reporte_alertas import ReporteAlertas
from src.reports.reporte_logs_recientes import ReporteLogsRecientes

def mostrar_menu():
    print("\n===== Menú de Opciones =====")
    print("1. Ver reporte estadístico por sala")
    print("2. Ver reporte de alertas")
    print("3. Ver cantidad de logs por sala")
    print("4. Ver logs recientes (últimos 5 min) por sala")
    print("0. Salir")
    print("============================")

if __name__ == "__main__":
    ruta = "data/logs_ambientales_ecowatch.csv"
    logs = cargar_logs_desde_csv(ruta)

    # Creamos y cargamos la caché con los logs de los últimos 5 minutos
    cache = CacheLogs()
    for log in logs:
        cache.agregar_log(log)

    # Agrupamos los logs por sala
    salas = agrupar_logs_por_sala(logs)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n📊 Reporte Estadístico\n" + "=" * 22)
            print(ReportePorSala().generar(salas))
        elif opcion == "2":
            print("\n🚨 Reporte de Alertas\n" + "=" * 22)
            print(ReporteAlertas().generar(salas))
        elif opcion == "3":
            print("\n📦 Cantidad de logs por sala\n" + "=" * 30)
            for nombre, sala in salas.items():
                print(f"{nombre} - {len(sala.logs)} logs")
        elif opcion == "4":
            print(ReporteLogsRecientes().generar(cache, logs))
            print()
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")
