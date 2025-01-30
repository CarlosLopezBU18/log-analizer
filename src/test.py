from os import listdir, mkdir
from os.path import exists, join
from typing import List

from shutil import rmtree

from parser import DataParser
from utils import load_json_files

LOGS_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/logs'
JSON_TEST_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/test/json'
OUTPUT_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/test/out'

# Obtener archivos con ruta completa
TEST_FILES: List[str] = [join(JSON_TEST_PATH, f) for f in listdir(JSON_TEST_PATH)]
INPUT_FILES: List[str] = [join(LOGS_PATH, f) for f in listdir(LOGS_PATH)]

if not TEST_FILES:
    raise FileNotFoundError("No se encontraron archivos JSON en la carpeta de tests")

if not INPUT_FILES:
    raise FileNotFoundError("No se encontraron archivos de log en la carpeta de logs")

# Crear output si no existe
if exists(OUTPUT_PATH):
    rmtree(OUTPUT_PATH)

mkdir(OUTPUT_PATH)

dp = DataParser(OUTPUT_PATH)
dp.load_sources(INPUT_FILES)

expected_results = load_json_files(TEST_FILES)
OUTPUT_FILES: str = [join(OUTPUT_PATH, f) for f in listdir(OUTPUT_PATH)]
my_results = load_json_files(OUTPUT_FILES)

assert expected_results == my_results

print('Han pasado todos los test')
