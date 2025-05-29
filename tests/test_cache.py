import pytest
from datetime import timedelta
from src.cache.cache_logs import CacheLogs
from src.loaders.load_logs import cargar_logs_desde_csv

def test_cache_guarda_logs_recientes():
    logs = cargar_logs_desde_csv("data/logs_ambientales_ecowatch.csv")
    cache = CacheLogs()

    # Simulamos el "ahora" como el timestamp del último log
    ahora = logs[-1].timestamp

    for log in logs:
        cache.agregar_log(log, ahora=ahora)

    # Verificamos que solo hay logs dentro de los últimos 5 minutos
    for log in cache.logs:
        assert log.timestamp >= ahora - timedelta(minutes=5)

    # Verificamos que la caché no está vacía
    assert len(cache.logs) > 0

def test_cache_filtra_por_sala():
    logs = cargar_logs_desde_csv("data/logs_ambientales_ecowatch.csv")
    cache = CacheLogs()
    ahora = logs[-1].timestamp

    for log in logs:
        cache.agregar_log(log, ahora=ahora)

    sala = "Sala_1"
    logs_sala = cache.obtener_por_sala(sala)

    assert all(log.sala == sala for log in logs_sala)
