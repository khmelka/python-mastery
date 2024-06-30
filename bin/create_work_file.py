import os
import re

directory = os.path.join(os.path.dirname(__file__), '..', 'Exercises')

pattern = re.compile(r'^ex[1-9]_[1-9]\.md$')

for filename in os.listdir(directory):
    if pattern.match(filename):
        base_name = filename[:-3]
        new_filename = base_name + '.py'
        
        py_file_path = os.path.join(directory, new_filename)
        
        with open(py_file_path, 'w') as py_file:
            pass 
        
        print(f'Created file: {new_filename}')