import json, os

with open("config.json", "r") as f:
    configs = json.load(f)

# DIRECTORY 
        
DEFAULT_OUTPUT_DIR = "/TapisOutput"
DEFAULT_OUTPUT_FILENAME = configs["outputFilename"]
DEFAULT_OUTPUT_FILE_PATH = os.path.join(
	DEFAULT_OUTPUT_DIR,
	DEFAULT_OUTPUT_FILENAME
)
