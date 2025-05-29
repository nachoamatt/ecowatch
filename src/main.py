from src.loaders.load_logs import cargar_logs_desde_csv
from src.utils.group_logs_by_sala import agrupar_logs_por_sala
from src.models.cache import CacheLogs
from src.reports.reporte_por_sala import ReportePorSala
from src.reports.reporte_alertas import ReporteAlertas

def mostrar_menu():
    print("\n📋 Bienvenido a EcoWatch")
    print("\nSeleccione una opción:")
    print("1. Ver reporte estadístico")
    print("2. Ver reporte de alertas")
    print("3. Ver estado de la caché")
    print("4. Salir")

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
        opcion = input("\nIngrese una opción (1-4): ")

        if opcion == "1":
            print("\n📊 Reporte Estadístico\n" + "=" * 22)
            print(ReportePorSala().generar(salas))

        elif opcion == "2":
            print("\n🚨 Reporte de Alertas\n" + "=" * 22)
            print(ReporteAlertas().generar(salas))

        elif opcion == "3":
            print(f"\n🧠 Estado de la caché: {cache}")

        elif opcion == "4":
            print("\n👋 Gracias por usar EcoWatch. ¡Hasta luego!\n")
            break

        else:
            print("❌ Opción inválida. Por favor, elija una opción entre 1 y 4.")
