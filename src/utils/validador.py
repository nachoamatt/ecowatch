from models.log import Log

def validar_log_dict(data: dict) -> Log:
    """
    Recibe un diccionario con datos de log y devuelve una instancia de Log validada.
    Lanza ValueError si faltan campos o los valores no son válidos.
    """
    campos_esperados = ['timestamp', 'sala', 'temperatura', 'humedad', 'co2']

    for campo in campos_esperados:
        if campo not in data:
            raise ValueError(f"Falta el campo obligatorio: {campo}")

    try:
        temperatura = float(data['temperatura'])
        humedad = float(data['humedad'])
        co2 = float(data['co2'])
    except ValueError:
        raise ValueError("Los valores de temperatura, humedad y co2 deben ser numéricos.")

    return Log(
        timestamp=data['timestamp'],
        sala=data['sala'],
        temperatura=temperatura,
        humedad=humedad,
        co2=co2
    )
