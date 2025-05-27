from datetime import datetime, timedelta
from src.models.log import Log

class CacheLogs:
    def __init__(self):
        self.logs = []

    # En tests se puede pasar un "ahora" simulado.
    # Si no se pasa, se usa datetime.now() (producción)
    def agregar_log(self, log: Log, ahora: datetime = None):
        if ahora is None:
            ahora = datetime.now()

        limite = ahora - timedelta(minutes=5)

        if log.timestamp >= limite:
            self.logs.append(log)

        # Limpiar logs viejos fuera de rango
        self.logs = [l for l in self.logs if l.timestamp >= limite]

    def obtener_por_sala(self, sala: str) -> list[Log]:
        return [log for log in self.logs if log.sala == sala]

    def obtener_por_timestamp(self, ts: datetime) -> list[Log]:
        return [log for log in self.logs if log.timestamp == ts]

    def __str__(self):
        return f"Cache con {len(self.logs)} logs en los últimos 5 minutos"
