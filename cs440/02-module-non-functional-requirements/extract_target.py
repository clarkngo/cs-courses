import nbformat
import os

NOTEBOOK_FILE = "hos02.ipynb"
TARGET_SCRIPT = "production_service.py"

if not os.path.exists(NOTEBOOK_FILE):
    print(f"[-] Error: {NOTEBOOK_FILE} not found.")
    exit(1)

with open(NOTEBOOK_FILE, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Filter explicitly for code cells under the student exercises section
exercise_code = []
capture = False

for cell in nb.cells:
    if cell.cell_type == "markdown" and "Try It Yourself: Student Exercises" in cell['source']:
        capture = True
    if capture and cell.cell_type == "code":
        exercise_code.append(cell['source'])

# Combine the flawed code payloads into a clean standalone module script layout
standalone_source = (
    "# Production Service Layer - Project Horizon Module 02\n\n" +
    "\n\n".join(exercise_code) +
    "\n\nif __name__ == '__main__':\n"
    "    print('[+] System operational diagnostics loaded.')\n"
)

with open(TARGET_SCRIPT, "w", encoding="utf-8") as f:
    f.write(standalone_source)

print(f"[+] Successfully extracted student exercises into '{TARGET_SCRIPT}'.")