import os
import ast
import subprocess
import sys

def extract_imports(file_path):
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

def generate_requirements(directory='.'):
    python_files = [f for f in os.listdir(directory) if f.endswith('.py')]

    all_imports = set()

    for file in python_files:
        file_path = os.path.join(directory, file)
        file_imports = extract_imports(file_path)
        all_imports.update(file_imports)

    with open('requirements.txt', 'w', encoding='utf-8') as req_file:
        for package in sorted(all_imports):
            req_file.write(package + '\n')

def install_requirements():
    if sys.platform.startswith('win'):
        python_cmd = 'python'
    else:
        python_cmd = 'python3'

    try:
        subprocess.run([python_cmd, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    except subprocess.CalledProcessError:
        print("Error installing requirements. Please make sure you have Python and pip installed.")

if __name__ == "__main__":
    generate_requirements()
    install_requirements()
