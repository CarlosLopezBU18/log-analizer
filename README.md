# 📝 Analizador de Logs Distribuido

## 📌 Descripción  
Este proyecto es un analizador avanzado de logs diseñado para procesar múltiples archivos de logs en paralelo y extraer estadísticas clave sobre eventos generados en sistemas distribuidos.  

El analizador es capaz de:  
1. **Procesar múltiples archivos de logs simultáneamente** utilizando concurrencia para mejorar el rendimiento.  
2. **Extraer estadísticas clave**, como:  
   - Cantidad total de logs por nivel (`ERROR`, `INFO`, `WARNING`, etc.).  
   - Los 5 mensajes de error más frecuentes.  
   - El timestamp del primer y último log procesado.  
3. **Optimizar el procesamiento** mediante `threading` o `multiprocessing` para manejar grandes volúmenes de datos sin sobrecargar la memoria.  
4. **Opcional**: Implementar una API REST con `FastAPI` para consultar estadísticas en tiempo real.  

```plaintext
┌───────────────┐       ┌──────────────────────┐       ┌───────────────┐
│  Usuario/API  │ --->  │  Servidor FastAPI    │ --->  │  Analizador   │
│ (Cliente)     │       │ (uvicorn)            │       │  de Logs      │
└───────────────┘       └──────────────────────┘       └───────────────┘
        │                          │                          │
        │   GET /logs/stats        │                          │
        ├─────────────────────────>│                          │
        │                          │                          │
        │   Procesa archivos       │                          │
        │                          ├────────────────────────> │
        │                          │                          │
        │   Devuelve estadísticas  │                          │
        │<──────────────────────── │                          │
        │                          │                          │
        │  JSON con métricas       │                          │
        ├────────────────────────> │                          │
        │                          │                          │
        │  Visualiza datos         │                          │
        └──────────────────────────┘                          │
                                                              │
```

---

## 🏰️ Estructura del Proyecto  

```
log-analyzer/
│── logs/                     # Carpeta donde se almacenan los archivos de logs
│── src/
│   ├── analyzer.py           # Módulo principal para analizar los logs
│   ├── parser.py             # Módulo para procesar y extraer datos de los logs
│   ├── utils.py              # Funciones auxiliares
│   ├── api.py                # API REST con FastAPI (opcional)
│── tests/                    # Pruebas unitarias
│── requirements.txt          # Dependencias del proyecto
│── README.md                 # Documentación del proyecto
```

---

## 🛠️ Instalación  

### 1⃣ Clonar el repositorio  
```bash
git clone https://github.com/tu_usuario/log-analyzer.git
cd log-analyzer
```

### 2⃣ Crear un entorno virtual (opcional pero recomendado)  
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3⃣ Instalar dependencias  
```bash
pip install -r requirements.txt
```

---

## 📚 Librerías utilizadas  

| Librería         | Descripción |
|-----------------|-------------|
| `multiprocessing` | Para procesamiento en paralelo de archivos grandes. |
| `threading` | Para manejar múltiples tareas de lectura concurrentemente. |
| `collections.Counter` | Para contar la frecuencia de los mensajes de error. |
| `heapq` | Para encontrar los mensajes más frecuentes eficientemente. |
| `re` | Para procesar y extraer información de los logs usando expresiones regulares. |
| `fastapi` | (Opcional) Para crear una API REST para consultar estadísticas. |
| `uvicorn` | (Opcional) Para correr el servidor FastAPI. |

Para instalar todas las dependencias, ejecuta:  
```bash
pip install -r requirements.txt
```

---

## 🚀 Uso  

### 1⃣ Ejecutar el analizador de logs  
Para procesar todos los archivos de logs en la carpeta `logs/`, ejecuta:  
```bash
python src/analyzer.py
```

### 2⃣ (Opcional) Levantar la API REST  
Si implementaste la API con FastAPI, puedes iniciarla con:  
```bash
uvicorn main:app --reload
```
Luego, accede a `http://127.0.0.1:8000/docs` para ver la documentación interactiva.

---

## 📊 Ejemplo de salida  

```bash
Procesando archivos de logs...
✔ Logs procesados con éxito.

📈 Estadísticas:
- Total de logs por nivel:
  - INFO: 12,340
  - WARNING: 5,678
  - ERROR: 2,345

- 5 mensajes de error más frecuentes:
  1. "Database connection failed" (432 veces)
  2. "User authentication failed" (321 veces)
  3. "Timeout while connecting to API" (198 veces)
  4. "Server overload detected" (134 veces)
  5. "File not found" (76 veces)

- Primer log registrado: 2025-01-30 12:00:00
- Último log registrado: 2025-01-30 23:59:59
```

---

## ✅ TODO  
✔ Procesar archivos en paralelo.  
✔ Extraer estadísticas clave.  
✔ Optimizar uso de memoria y procesamiento.  
❌ Implementar la API REST para consultar estadísticas.  
❌ Agregar pruebas unitarias con `pytest`.  

---

## 🐝 Extras  
Si quieres agregar más funcionalidades, aquí hay algunas ideas:
- **Soporte para streaming de logs en tiempo real.**
- **Análisis de tendencias a lo largo del tiempo.**
- **Integración con un sistema de alertas basado en patrones detectados en los logs.**

---

## 🐝 Contribuciones  
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, abre un Pull Request o reporta un Issue.  

---

## 🐜 Licencia  
MIT License. ¡Siéntete libre de contribuir! 🚀  
