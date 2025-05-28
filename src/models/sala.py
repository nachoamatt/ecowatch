from src.models.log import Log

class Sala:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.logs = []

    def agregar_log(self, log: Log):
        if log.sala == self.nombre:
            self.logs.append(log)

    def __str__(self):
        return f"Sala: {self.nombre} - {len(self.logs)} logs cargados"

    def temperatura_promedio(self) -> float:
        if not self.logs:
            return 0.0
        return sum(log.temperatura for log in self.logs) / len(self.logs)

    def humedad_promedio(self) -> float:
        if not self.logs:
            return 0.0
        return sum(log.humedad for log in self.logs) / len(self.logs)

    def co2_promedio(self) -> float:
        if not self.logs:
            return 0.0
        return sum(log.co2 for log in self.logs) / len(self.logs)
