import csv
from src.utils.validador import validar_log_dict
from src.models.log import Log

def cargar_logs_desde_csv(ruta_csv: str) -> list[Log]:
    logs = []
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                log = validar_log_dict(fila)
                logs.append(log)
            except Exception as e:
                print(f"❌ Error al procesar fila: {fila}\n   Motivo: {e}")
    return logs

if __name__ == "__main__":
    ruta = "data/logs_ambientales_ecowatch.csv"
    logs = cargar_logs_desde_csv(ruta)

    print(f"✅ Se cargaron {len(logs)} logs válidos.\n")
    for log in logs[:5]:
        print(log)
