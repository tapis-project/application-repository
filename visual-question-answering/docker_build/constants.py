import json,os

with open("configs.json", "r") as f:
    configs = json.load(f)
    

#DIRECTORIES

DEFAULT_OUTPUT_DIR = os.environ.get("_tapisExecSystemOutputDir", "results_folder")
DEFAULT_OUTPUT_FILENAME = "results_file.csv"
DEFAULT_OUTPUT_FILE_PATH = os.path.join(
	DEFAULT_OUTPUT_DIR,
	DEFAULT_OUTPUT_FILENAME
)
