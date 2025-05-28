from abc import ABC, abstractmethod

class ReporteBase(ABC):
    @abstractmethod
    def generar(self, salas: dict) -> str:
        pass
