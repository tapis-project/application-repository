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
        print(args)
        
        result = pipeline(*args)

        
    except Exception as e: 
        raise Exception(f"Error running pipeline: {e}")
    
    # Pass the arguments to the selected pipeline function
    #print(prediction)
    print("Result:", result)
        
    os.environ['SENTENCE_TRANSFORMERS_HOME'] = './.cache'

    # Print output to screen and write to file
    tapis_app_id = os.environ.get('_tapisAppId')
    if tapis_app_id is None:
        # Not running under Tapis, write to /tmp
        print('Not running under Tapis. Writing output to /tmp\n')
        outputPath = '/tmp/output.txt'
    else:
        # Running under Tapis.
        print('Running under Tapis: _tapisAppId=%s\n' % tapis_app_id)
        # If Docker, write to /TapisOutput,
        # else write to $_tapisExecSystemOutputDir
        tapis_sing_name = os.environ.get('SINGULARITY_NAME')
        if tapis_sing_name is None:
            print('Running via Tapis using Docker\n')
            outputPath = '/TapisOutput/output.txt'
        else:
            print('Running via Tapis using Singularity\n')
            outputDir = os.environ.get('_tapisExecSystemOutputDir')
            if outputDir is None:
                print('WARNING: _tapisExecSystemOutputDir not set. Using /tmp for output.')
                outputPath = '/tmp/output.txt'
            else:
                outputPath = os.path.join(outputDir, "output.txt")
    print('Using output path: %s\n' % outputPath)
    with open(outputPath, "a") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
