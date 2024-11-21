import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="mlproject"
list_of_file = [
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/data_ingestion.py",
f"src/{project_name}/components/data_transformation.py",
f"src/{project_name}/components/model_trainer.py",
f"src/{project_name}/components/model_monintoring.py",
f"src/{project_name}/pipelines/__init__.py",
f"src/{project_name}/pipelines/training_pipeline.py",
f"src/{project_name}/pipelines/prediction_pipeline.py",
f"src/{project_name}/exception.py",
f"src/{project_name}/pipelines/logger.py",
f"src/{project_name}/pipelines/utils.py"
"app.py",
"Dockerfile",
"requirement.txt",
"setup.py"


]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir = filepath.parent
    # Create the directory if it doesn't exist
    os.makedirs(filedir, exist_ok=True)
    # Create the file if it doesn't exist
    if not filepath.exists():
        filepath.touch()
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
