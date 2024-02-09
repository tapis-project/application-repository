import json, os, requests


# READ JSON CONFIGS

with open('config.json', 'r') as f:
        configs = json.load(f)

# DIRECTORY 
        
DEFAULT_OUTPUT_DIR = os.environ.get("_tapisExecSystemOutputDir", "saved_outputs")
DEFAULT_OUTPUT_FILENAME = "summary.txt"
DEFAULT_OUTPUT_FILE_PATH = os.path.join(
	DEFAULT_OUTPUT_DIR,
	DEFAULT_OUTPUT_FILENAME
)

# SUMMARY CHARACTERS 

MIN_VALUE = configs["summaryCharacters"]["min"]
MAX_VALUE = configs["summaryCharacters"]["max"]

# MODELS

DEFAULT_MODEL = configs["model"]["defaultModelt5Base"]
CHECKPOINT_MODEL = configs["model"]["checkpointModel"]

