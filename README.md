
# Proyecto EcoWatch 🌱

Este proyecto simula el sistema de procesamiento de datos de una red de sensores ambientales distribuidos en distintas salas. Cada sensor mide temperatura, humedad y niveles de CO₂, y envía registros minuto a minuto.

---

## ✅ Funcionalidades implementadas

### 1. Lectura y validación de logs
- Se implementó la clase `Log`, que representa una medición ambiental individual.
- Los registros se cargan desde un archivo CSV mediante `cargar_logs_desde_csv`.
- Cada entrada se valida usando `validar_log_dict`, que verifica la existencia y el tipo de los campos obligatorios (`timestamp`, `sala`, `temperatura`, `humedad`, `co2`).
- Si un dato está mal formado, se ignora y se muestra un error sin interrumpir la ejecución.

### 2. Agrupación por sala
- Se creó la clase `Sala`, que agrupa los logs según su lugar de origen (`Sala_1`, `Sala_2`, etc.).
- La función `agrupar_logs_por_sala` organiza los registros en un diccionario.
- Cada sala calcula sus promedios de temperatura, humedad y CO₂.

### 3. Caché de últimos 5 minutos
- Se implementó la clase `CacheLogs`, que mantiene en memoria solo los registros recientes.
- El método `agregar_log` descarta automáticamente los que exceden los 5 minutos.
- Se puede consultar la caché por sala o timestamp.
- El método `__str__` resume el estado de la caché.

### 4. Reportes por consola (menú interactivo)
- El script `main.py` presenta un menú con opciones:
  1. Ver reporte estadístico por sala (promedios)
  2. Ver reporte de alertas por sala
  3. Ver cantidad de logs por sala
  4. Ver logs recientes (últimos 5 minutos)
  0. Salir
- Los reportes están implementados usando clases que heredan de `ReporteBase`, respetando una estructura orientada a objetos.

### 5. Tests con `pytest`
- Se escribieron tests unitarios para:
  - Validación de logs (`test_validador_log_valido`, `test_validador_log_faltante`, etc.)
  - Funcionamiento de la caché (`test_agregar_y_limpiar_logs`, etc.)

---

## 🗂️ Estructura del proyecto

```
ecowatch/
├── data/                  ← archivo CSV de entrada
├── src/
│   ├── loaders/           ← carga de datos desde CSV
│   ├── models/            ← clases Log, Sala, CacheLogs
│   ├── reports/           ← reportes estadísticos y alertas
│   └── utils/             ← validadores y agrupadores
├── tests/                 ← tests unitarios con pytest
├── main.py                ← menú interactivo
├── requirements.txt       ← librerías
└── README.md              ← este archivo
```

---

## ▶️ Cómo ejecutar el proyecto

Desde la raíz del proyecto, en un entorno virtual:

```bash
source venv/bin/activate
PYTHONPATH=. python3 src/main.py
```

---

## 🧪 Cómo correr los tests

```bash
pytest tests/
```

---

## 📌 Requisitos

- Python 3.10+
- pytest

---

## 🧠 Justificación técnica

Durante el desarrollo del sistema EcoWatch, se tomaron decisiones técnicas con foco en **modularidad**, **rendimiento**, y **extensibilidad**:

### 🔹 Estructuras de datos
- **Listas**: Se usaron listas (`list`) para almacenar los logs, ya que permiten orden cronológico y recorridos eficientes con volumen acotado. En la caché (`CacheLogs`), se filtran dinámicamente los registros vencidos cada vez que se inserta un nuevo log. Esto evita estructuras más complejas como heaps o árboles, que no eran necesarias por el volumen y ventana temporal limitada (5 minutos).
- **Diccionarios (`dict`)**: Se agruparon logs por sala usando diccionarios para obtener acceso rápido (`O(1)`) a cada agrupación.

### 🔹 Programación orientada a objetos
- Se modelaron entidades del dominio como clases (`Log`, `Sala`, `CacheLogs`, `Reporte`) para encapsular datos y comportamientos. Esto mejora la legibilidad y permite que el sistema crezca fácilmente (por ejemplo, agregando nuevos sensores o nuevas métricas sin modificar la estructura existente).

### 🔹 Patrones de diseño
- **Factory**: Usado para instanciar diferentes tipos de reportes sin acoplar el código principal a una clase específica. Esto permite que los reportes sean configurables y se puedan agregar nuevos sin modificar el `main`.
- **Strategy**: Aplicado dentro de los reportes para encapsular distintas lógicas de generación, por ejemplo: estadísticas por sala vs. alertas. Cada reporte implementa su propia estrategia de procesamiento.

### 🔹 Optimización y extensibilidad
- Se priorizó la **legibilidad** y la **modularidad** por sobre micro-optimizaciones, ya que el sistema está diseñado para ser mantenido y escalado por otros equipos.
- El diseño permite agregar nuevas fuentes de datos (como JSON o APIs) o nuevos tipos de reportes con mínimo esfuerzo y sin alterar el núcleo del sistema.
- La inclusión de un parámetro `ahora` en `CacheLogs` permite testear comportamientos con datos históricos o eventos fuera de orden.

---

## ✍️ Autor

**Ignacio Amatt**  
Proyecto de Ingeniería de Datos – Henry  
Mayo 2025
