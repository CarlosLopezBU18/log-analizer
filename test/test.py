# from src.parser import DataParser
from os import listdir, mkdir, rmdir
from os.path import exists

INPUT_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/logs'
OUTPUT_PATH: str = '/Users/more/Desktop/code/DailyPython/log-analizer/test/out'

print(listdir(INPUT_PATH))

if exists(OUTPUT_PATH):
    rmdir(OUTPUT_PATH)
else: 
    mkdir(OUTPUT_PATH)
