import pytest
from src.utils.validador import validar_log_dict

def test_validador_log_valido():
    data = {
        "timestamp": "2025-05-01 08:00:00",
        "sala": "Sala_1",
        "temperatura": "22.5",
        "humedad": "45.0",
        "co2": "800"
    }
    log = validar_log_dict(data)
    assert log.sala == "Sala_1"
    assert log.temperatura == 22.5
    assert log.humedad == 45.0
    assert log.co2 == 800.0

def test_validador_log_faltante():
    data = {
        "timestamp": "2025-05-01 08:00:00",
        "sala": "Sala_1",
        "temperatura": "22.5",
        "co2": "800"  # falta "humedad"
    }
    with pytest.raises(ValueError, match="Falta el campo obligatorio: humedad"):
        validar_log_dict(data)

def test_validador_log_invalido():
    data = {
        "timestamp": "2025-05-01 08:00:00",
        "sala": "Sala_1",
        "temperatura": "veintidos",
        "humedad": "45.0",
        "co2": "800"
    }
    with pytest.raises(ValueError, match="Los valores de temperatura, humedad y co2 deben ser numéricos."):
        validar_log_dict(data)
