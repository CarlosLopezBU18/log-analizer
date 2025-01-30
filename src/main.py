from fastapi import FastAPI, File, UploadFile
from typing import List
import os
from shutil import rmtree
from parser import DataParser

app = FastAPI()

# Carpeta temporal para guardar los logs subidos
TEMP_LOGS_DIR = "temp_logs"
OUTPUT_DIR = "output_json"

# Crear carpetas si no existen
os.makedirs(TEMP_LOGS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/upload-logs/")
async def upload_logs(files: List[UploadFile] = File(...)):
    """
    Recibe múltiples archivos de log, los guarda temporalmente,
    los procesa con `DataParser` y devuelve los resultados.
    """
    file_paths = []  # Lista de rutas de archivos guardados temporalmente

    for file in files:
        if not file.filename.endswith(".log"):
            return {"error": f"El archivo {file.filename} no es un .log válido"}
        
        file_path = os.path.join(TEMP_LOGS_DIR, file.filename)
        
        with open(file_path, "wb") as f:
            f.write(await file.read())  # Guardar el archivo en el sistema

        file_paths.append(file_path)

    # Procesar archivos con `DataParser`
    dp = DataParser(OUTPUT_DIR)
    dp.load_sources(file_paths)

    rmtree(TEMP_LOGS_DIR)
    os.makedirs(TEMP_LOGS_DIR, exist_ok=True)
    return {"message": "Archivos procesados", "results": dp.results}


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Log Analyzer"}