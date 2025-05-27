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
