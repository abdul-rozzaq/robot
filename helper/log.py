import json
import os


class Logger:
    dir_name = 'logs'
    
    
    def __init__(self, name):
        self.name = name
        self.data = []
        
    
    def __enter__(self):
        return self.data

    def __exit__(self, exc_type, exc_value, trace):      
        old_data = []
        
        if os.path.exists(os.path.join(self.dir_name, self.name + '.json')):
            with open(os.path.join(self.dir_name, self.name + '.json'), 'r') as file:
                old_data = json.loads(file.read() or '[]')
        
        new_data = old_data + self.data
        
        with open(os.path.join(self.dir_name, self.name + '.json'), 'w') as file:
            file.write(json.dumps(new_data, indent=4, ensure_ascii=False))
        
        
        