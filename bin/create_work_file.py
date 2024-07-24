import os
import re
import shutil

directory = os.path.join(os.path.dirname(__file__), '..', 'Exercises')


def create_py_file():
    pattern = re.compile(r'^ex[1-9]_[1-9]\.md$')

    for filename in os.listdir(directory):
        if pattern.match(filename):
            base_name = filename[:-3]
            new_filename = base_name + '.py'
            
            py_file_path = os.path.join(directory, new_filename)
            
            with open(py_file_path, 'w') as py_file:
                pass 
            
            print(f'Created file: {new_filename}')

def move_file():

    # Define the directory containing the .py files
    exercise_directory = os.path.join(os.path.dirname(__file__), '..', 'Exercises')

    # Define the destination folder for .py files
    solutions_directory = os.path.join(os.path.dirname(__file__), '..', 'my_solutions')

    # Create the solutions directory if it doesn't exist
    os.makedirs(solutions_directory, exist_ok=True)

    # Define the regex pattern to match .py files
    pattern = re.compile(r'^ex[1-9]_[1-9]\.py$')

    # Loop through all files in the directory
    for filename in os.listdir(exercise_directory):
        # Check if the file matches the regex pattern
        if pattern.match(filename):
            # Construct the full path for the .py file
            py_file_path = os.path.join(exercise_directory, filename)
            
            # Destination path
            new_location = os.path.join(solutions_directory, filename)
            
            # Check if file already exists in the destination
            if os.path.exists(new_location):
                print(f'File {filename} already exists in {solutions_directory}. Skipping.')
            else:
                # Move the .py file to the solutions directory
                shutil.move(py_file_path, new_location)
                print(f'Moved: {filename} to {new_location}')
                
move_file()