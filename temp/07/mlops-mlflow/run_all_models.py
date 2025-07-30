import subprocess
import os

# Define the list of scripts to run
scripts = [
    'log_movie_model_gb.py',
    'log_movie_model_lr.py',
    'log_movie_model_nn.py',
    'log_movie_model_rf.py'
]

# Path where the scripts are located
script_path = '/workspaces/DIT637-TT07/mlops-mlflow'  # Update this to your actual path

# Change working directory to script path
os.chdir(script_path)

# Function to run a script
def run_script(script_name):
    try:
        print(f"Running {script_name}...")
        result = subprocess.run(['python', script_name], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Errors encountered in {script_name}:\n{result.stderr}")
    except Exception as e:
        print(f"Failed to run {script_name} due to: {e}")

# Run each script
for script in scripts:
    run_script(script)
