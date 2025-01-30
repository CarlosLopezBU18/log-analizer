from os import listdir, mkdir, remove
from os.path import exists
from typing import List
import sys
import os
import shutil
# Agregar 'src/' al sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from parser import DataParser
from utils import load_json_files

LOGS_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/logs'
JSON_TEST_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/test/json'
OUTPUT_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/test/out'

# Obtener archivos con ruta completa
TEST_FILES: List[str] = [os.path.join(JSON_TEST_PATH, f) for f in listdir(JSON_TEST_PATH)]
INPUT_FILES: List[str] = [os.path.join(LOGS_PATH, f) for f in listdir(LOGS_PATH)]

if not TEST_FILES:
    raise FileNotFoundError("No se encontraron archivos JSON en la carpeta de tests")

if not INPUT_FILES:
    raise FileNotFoundError("No se encontraron archivos de log en la carpeta de logs")

# Crear output si no existe
if exists(OUTPUT_PATH):
    shutil.rmtree(OUTPUT_PATH)
mkdir(OUTPUT_PATH)

dp = DataParser(OUTPUT_PATH)
dp.load_sources(INPUT_FILES)

expected_results = load_json_files(TEST_FILES)
OUTPUT_FILES: str = [os.path.join(OUTPUT_PATH, f) for f in listdir(OUTPUT_PATH)]
my_results = load_json_files(OUTPUT_FILES)

assert expected_results == my_results, 'Han pasado todos los test'
