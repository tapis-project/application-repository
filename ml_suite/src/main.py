import argparse
import os
import sys


# Import your pipeline functions here
from pipelines import (
    sentiment_analysis, 
    language_model_casual,
    translator,
    question_answering,
    summarizer,
    mask_fill
)

def main():
    args = sys.argv[1:]
    pipelines = {
        "sentiment_analysis": sentiment_analysis,
        "language_model_casual": language_model_casual,
        "translator": translator,
        "question_answering": question_answering,
        "summarizer": summarizer,
        "mask_fill": mask_fill
    }
    pipeline_names = list(pipelines.keys())
    
    if len(args) < 1:
        raise Exception(f"Missing pipeline argument. The first provided argument must be a pipeline type. The available types are {pipeline_names}")
    
    pipeline_name = args[0]
    if pipeline_name not in pipeline_names:
        raise Exception(f"Invalid argument for pipeline, must be one of {pipeline_names}")
    
    pipeline = pipelines[pipeline_name]

    try:
        if len(args[1:]) > 0:
            pipeline(*args[1:])
            return 
        
        # Search for input data in the "inputs" folder
        try:
            tree = list(os.walk("inputs"))[0] 
        except IndexError:
            try:
                tree = list(os.walk("/src/inputs"))[0]
            except IndexError:
                # Handle the case where both searches fail
                raise Exception("Error: Both 'inputs' and '/src/inputs' directories not found.")

        filenames = [os.path.join(tree[0], name) for name in tree[2] if name != ".gitkeep"]

        if len(filenames) == 0:
            raise Exception("No input files found in the 'inputs' directory.")

        args = []
        for filename in filenames:
            with open(filename, "r") as file:
                args.append(file.read())
        
        result = pipeline(*args)
    except Exception as e: 
        raise Exception(f"Error running pipeline: {e}")

    # Resolve the output file path based on environment
    outputDir = os.environ.get('_tapisExecSystemOutputDir') or "/TapisOutput"
    os.makedirs(outputDir, exist_ok=True)

    with open(os.path.join(outputDir, 'output.txt'), "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()

