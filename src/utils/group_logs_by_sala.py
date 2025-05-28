from src.loaders.load_logs import cargar_logs_desde_csv
from src.models.sala import Sala

def agrupar_logs_por_sala(logs: list) -> dict:
    salas = {}

    for log in logs:
        nombre_sala = log.sala

        if nombre_sala not in salas:
            salas[nombre_sala] = Sala(nombre_sala)

        salas[nombre_sala].agregar_log(log)

    return salas

if __name__ == "__main__":
    ruta = "data/logs_ambientales_ecowatch.csv"
    logs = cargar_logs_desde_csv(ruta)

    salas = agrupar_logs_por_sala(logs)

    print(f"✅ Se agruparon los logs en {len(salas)} salas.\n")

    for sala in salas.values():
        print(sala)
