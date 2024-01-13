import os
import ast
import subprocess
import sys

def extract_imports(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read(), filename=file_path)

        imports = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module)

        return imports
    except Exception as e:
        error_message = f"Error extracting imports from {file_path}: {e}"
        print(error_message)
        with open('errors.txt', 'a', encoding='utf-8') as error_file:
            error_file.write(error_message + '\n')
        return set()

def generate_requirements(directory='.'):
    try:
        python_files = [f for f in os.listdir(directory) if f.endswith('.py')]

        all_imports = set()

        for file in python_files:
            file_path = os.path.join(directory, file)
            file_imports = extract_imports(file_path)
            all_imports.update(file_imports)

        with open('requirements.txt', 'w', encoding='utf-8') as req_file:
            for package in sorted(all_imports):
                req_file.write(package + '\n')
    except Exception as e:
        error_message = f"Error generating requirements: {e}"
        print(error_message)
        with open('errors.txt', 'a', encoding='utf-8') as error_file:
            error_file.write(error_message + '\n')

def install_requirements():
    try:
        if sys.platform.startswith('win'):
            python_cmd = 'python'
        else:
            python_cmd = 'python3'

        subprocess.run([python_cmd, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    except subprocess.CalledProcessError as e:
        error_message = f"Error installing requirements: {e}"
        print(error_message)
        print("Please make sure you have Python and pip installed.")
        with open('errors.txt', 'a', encoding='utf-8') as error_file:
            error_file.write(error_message + '\n')

if __name__ == "__main__":
    generate_requirements()
    install_requirements()
