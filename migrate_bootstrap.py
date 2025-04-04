import os
import re
import shutil

SOURCE_FOLDER = "./bootstrap4-html"  # Folder with Bootstrap 4 files
OUTPUT_FOLDER = "./bootstrap5-html"  # Folder where updated files are saved

# Mapping replacements
REPLACEMENTS = [
    (r'form-group', 'mb-3'),
    (r'form-row', 'row'),
    (r'input-group-append', 'input-group'),
    (r'input-group-prepend', 'input-group'),
    (r'col-form-label-sm', 'form-label'),
    (r'col-form-label-lg', 'form-label'),
    (r'float-left', 'float-start'),
    (r'float-right', 'float-end'),
    (r'badge-pill', 'badge rounded-pill'),
    (r'ml-(\d+)', r'ms-\1'),
    (r'mr-(\d+)', r'me-\1'),
    (r'@ViewChild\(([^)]+)\)\s+([^;]+);', r'@ViewChild(\1, {{ static: false }}) \2;'), # Angular ViewChild update
    (r'@ViewChildren\(([^)]+)\)\s+([^;]+);', r'@ViewChildren(\1, {{ static: false }}) \2;') # Angular ViewChildren update
]

def aggiorna_file_html(file_path, output_path):
    """Update an HTML file by replacing Bootstrap 4 classes with Bootstrap 5 classes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        contenuto = f.read()
    
    for pattern, replacement in REPLACEMENTS:
        contenuto = re.sub(pattern, replacement, contenuto)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(contenuto)
    print(f"Updated: {file_path} -> {output_path}")

def processa_cartella():
    """Scan the folder and update all HTML and TypeScript Angular files."""
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    for root, _, files in os.walk(SOURCE_FOLDER):
        for file in files:
            if file.endswith(".html") or file.endswith(".ts"):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, SOURCE_FOLDER)
                output_path = os.path.join(OUTPUT_FOLDER, relative_path)
                
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                aggiorna_file_html(input_path, output_path)

if __name__ == "__main__":
    processa_cartella()
    print("Migration completed!")
