from enum import Enum
from typing import List

import json

class Level(Enum):
    ERROR = 0
    INFO = 1
    WARNING = 2

def load_json_files(json_files: List[str]):
    dicts = []
    for json_file in json_files:
        dicts.append(json.load(json_file))

    return dicts