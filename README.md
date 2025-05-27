# Proyecto EcoWatch 🌱

Este proyecto simula el sistema de procesamiento de datos de una red de sensores ambientales distribuidos en distintas salas. Cada sensor mide temperatura, humedad y niveles de CO₂, y envía registros minuto a minuto.

## ✅ Funcionalidades implementadas

### 1. Lectura y validación de logs
- Se implementó la clase `Log`, que representa una medición ambiental individual.
- Se cargan registros desde un archivo CSV y se validan campos clave como `timestamp`, `sala`, `temperatura`, `humedad`, y `co2`.
- Si el dato está mal formado, se muestra un error sin interrumpir la carga.

### 2. Agrupación por sala
- Se creó la clase `Sala`, que agrupa los logs según el lugar de origen (`Sala_1`, `Sala_2`, etc.).
- Cada sala contiene los logs que le corresponden y puede expandirse con métodos propios en el futuro.

### 3. Caché temporal de 5 minutos
- Se diseñó la clase `CacheLogs` que mantiene en memoria solo los registros de los últimos 5 minutos.
- Permite consultar logs por nombre de sala o timestamp.
- En entornos de prueba, puede recibir un `ahora` simulado para validar su comportamiento con datos históricos.
- En producción, se comporta dinámicamente con `datetime.now()`.

### 4. Estructura del proyecto
```
ecowatch/
├── data/            ← archivo CSV de entrada
├── src/
│   ├── models/      ← clases Log y Sala
│   ├── cache/       ← lógica de caché temporal
│   └── load_logs.py ← carga y validación de datos
├── tests/           ← carpeta reservada para tests (a integrar)
├── requirements.txt ← librerías (a completar)
└── README.md        ← este archivo
```

## 🧪 Ejecución de scripts

Desde el entorno virtual, y estando en la raíz del proyecto:

```bash
source venv/bin/activate
PYTHONPATH=. python3 src/load_logs.py
PYTHONPATH=. python3 src/group_logs_by_sala.py
PYTHONPATH=. python3 src/test_cache.py
```

## 🔧 Pendientes para próximas entregas

- Reportes (por sala, por alerta) usando patrones de diseño (Factory + Strategy)
- Tests con `pytest`
- Documentación técnica final (justificación de decisiones)

---

## ✍️ Autor

Ignacio Amatt - Proyecto Data Engineering - Henry
