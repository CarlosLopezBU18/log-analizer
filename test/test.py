# from src.parser import DataParser
from os import listdir, mkdir, rmdir
from os.path import exists
from typing import List

from src.parser import DataParser
from src.utils import load_json_files

LOGS_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/logs'
JSON_TEST_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/test/json'
OUTPUT_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/test/out'

TEST_FILES: List[str] = listdir(JSON_TEST_PATH)
INPUT_FILES: List[str] = listdir(LOGS_PATH)

if exists(OUTPUT_PATH):
    rmdir(OUTPUT_PATH)
else: 
    mkdir(OUTPUT_PATH)

dp = DataParser(OUTPUT_PATH)
dp.load_sources(INPUT_FILES)

expected_results = load_json_files(TEST_FILES)
my_results = load_json_files(OUTPUT_PATH)

assert expected_results == my_results, 'Han pasado todos los test'