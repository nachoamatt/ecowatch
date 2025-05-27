from datetime import datetime

class Log:
    def __init__(self, timestamp: str, sala: str, temperatura: float, humedad: float, co2: float):
        self.timestamp = self._validar_timestamp(timestamp)
        self.sala = sala
        self.temperatura = temperatura
        self.humedad = humedad
        self.co2 = co2

    def _validar_timestamp(self, ts: str) -> datetime:
        try:
            return datetime.fromisoformat(ts)
        except ValueError:
            raise ValueError(f"Timestamp inválido: {ts}")

    def __str__(self):
        return (
            f"[{self.timestamp}] Sala: {self.sala} - "
            f"Temp: {self.temperatura}°C, Humedad: {self.humedad}%, CO₂: {self.co2}ppm"
        )
