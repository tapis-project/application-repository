import argparse, os, sys

from transformers import pipeline


def summarize(flags) -> str:
    '''
    Summarize the text.

    Args:
        text: The text to be summarized.
        minLength: The minimum length of the summary.
        maxLength: The maximum length of the summary.
        model_name: The name of the model to be used for summarization.
    Returns:
        summary: The summarized text.
        '''
    
    text = flags.text
    min_len = flags.min
    max_len = flags.max
    model = flags.model
    file = flags.file
    
    if not text and not file:
        raise Exception("Must provide at least 1 statement with --text flag or at least 1 file with the --file.")
    
    
    if file and not os.path.isfile(file):
        raise Exception(f"A path provided in the --file flag is not a file | {file}")

    with open(file, mode="r") as file_obj:
        text = file_obj.read()
    
    output = pipeline('summarization', model=model)
    summary_result = output(text, min_length=min_len, max_length=max_len)

    if not summary_result:
        raise Exception("No summary result")

    return summary_result[0]['summary_text']

    
def write_to_file(summary_result):
    """
    Writes a string into a file

    Args:
        input_string:   The string to be written to a file
        filename:       The destiantion file path for the string

    Returns:
        None
    """
    output_filename = os.path.join(
        os.environ.get(
            "_tapisExecSystemOutputDir",
            "saved_outputs"
        ),
        "summary.txt"
    )
        
    try:
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        with open(output_filename, 'w') as file:
            file.write(summary_result)
        print("Output written to", output_filename)
    except IOError:
        print("Error writing to file", output_filename)

def main():
    '''
    Main function to summarize text.
    '''

    #using argparse to rewrite the main function
    # adding args, flagging the statement to be summarized as mandatory
    # minLength and maxLength will have default values
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--text', type=str, help='This is the text that needs to be summarized.')
    parser.add_argument('--min', default=3, type=int, help='this is the minimum characters to be used in the summary.')
    parser.add_argument('--max', default=5, type=int, help='this is the maximum characters to be used in the summary.')
    parser.add_argument('--model', default='t5-base', type=str, help='select your model type. Default is t5-base.')
    parser.add_argument('--file', type=str, help='files to be added intead of statement')
    
    flags, _ = parser.parse_known_args()
    
    #print(summary)
    write_to_file(summarize(flags))


if __name__ == "__main__":
    main()
    
#TODO 1) add the STDerr for file failure. Needs to return the reason for failure so that we can catch the exception. Write to STDerr and then exit program. 
# sys.exit() or just exit(). Provide an exit code. Remember that it must be an integer. Don't use 0 because typically non0 return codes indicate error. 