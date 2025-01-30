import json

from os.path import exists
from analizer import analize, th, List

class DataParser:
    def __init__(self, output_path: str):
        self.lock = th.Lock()
        self.results = []
        self.output_path = output_path

    def parse(self, path: str):
        parsed = []
        with open(path, 'r') as file:
            for line in file:
                date, hour, level, message = line.replace('[','')\
                                                 .replace(']','')\
                                                 .split(" ", 3)
                
                parsed.append({'date': date, 'hour': hour, 'level': level, 'message': message[:-1]})

            file.close()
            with self.lock:
                self.results = analize(parsed)

            output_name = self.output_path + path.split('/')[-1].split('.')[0] + '.json'
            with open(output_name, 'w') as save_json:
                json.dump(self.results, save_json,indent=1)
        

    def load_sources(self, srcs: List[str]):
        threads = []

        for path in srcs:
            if exists(path):
                thread = th.Thread(target=self.parse, args=(path,))
                threads.append(thread)
                thread.start()
        
        for thread in threads:
            thread.join()