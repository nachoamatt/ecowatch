from datetime import datetime, timedelta
from loaders.load_logs import cargar_logs_desde_csv
from src.cache.cache_logs import CacheLogs

if __name__ == "__main__":
    logs = cargar_logs_desde_csv("data/logs_ambientales_ecowatch.csv")
    cache = CacheLogs()

    # Simulamos el "ahora" como el timestamp del último log para probar la caché
    # En producción, CacheLogs usa datetime.now() automáticamente
    ahora = logs[-1].timestamp

    for log in logs:
        if log.timestamp >= ahora - timedelta(minutes=5):
            cache.agregar_log(log, ahora=ahora)

    print(cache)
    print()

    sala = "Sala_1"
    logs_sala = cache.obtener_por_sala(sala)
    print(f"Logs en {sala}: {len(logs_sala)} encontrados.\n")

    for log in logs_sala[:3]:
        print(log)

    # Para usar en producción (sin simular el "ahora"):
    # for log in logs:
    #     cache.agregar_log(log)
