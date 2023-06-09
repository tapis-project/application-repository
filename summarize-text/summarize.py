import sys, os
from transformers import pipeline

def func_summarize(text, minLength, maxLength, model_name):
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
    
    try:
        output = pipeline('summarization', model=model_name, min_length=minLength, max_length=maxLength)
        summary = output(text)[0]['summary_text']
    except Exception as e:
        return e
    return summary

def write_to_file(output_string, filename):
    '''
    Writes a string into a file

    Args:
        input_string:   The string to be written to a file
        filename:       The destiantion file path for the string

    Returns:
        None
    '''

    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as file:
            file.write(output_string)
        print("Output written to", filename)
    except IOError:
        print("Error writing to file", filename)

def main():
    '''
    Main function to summarize text.
    '''

    directory = "saved_outputs"
    filename = os.path.join(directory, "summary.txt")

    try:
        text = sys.argv[1]
        minLength = int(sys.argv[2])
        maxLength = int(sys.argv[3])
        if len(sys.argv) > 4:
            model_name = sys.argv[4]
        else:
            model_name = 't5-base'
    except Exception as e: 
        write_to_file("Error: " + str(e), filename)
        return
    
    summary = func_summarize(text, minLength, maxLength, model_name)
    print(summary)
    write_to_file(summary, filename)

    with open(filename, 'r') as file:
        print(file.read())  

if __name__ == "__main__":
    main()
