import argparse, os, requests, sys, textwrap

from transformers import pipeline


def gen_text(flags):
    
    '''
    Function to generate text from input sentence, using the TextGenerationPipeline from huggingface. 
    Args:
        model_name (str): Text generation model name, please see: https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads
        statement (str): The input sentence for text generation.
        max_num (int): Input to control the total length of the output text are generated.
        num_seq (int): Input to control how many different sequences are generated.
    Output:
        output_text (list): Based on the sentence prompt, the model will auto-complete it by generating the remaining text in the text length and number of sequences specified.
    '''
    
        
    model = flags.model
    statement = flags.statement
    sequence = flags.sequence
    file = flags.file
    max_output = flags.max_output

    if statement == None and file == None:
        raise Exception("You must provide either a statement or a file")
    
    if file:
        if not os.path.isfile(file):
            raise Exception(f"A path provided in the --file flag is not a file | {file}")
        with open(file, mode="r") as file_obj:
            statement = file_obj.read()

    try:
        output = pipeline("text-generation",model=model)
        generated_text = output(statement, max_len=max_output, num_return_sequences=sequence)
    except Exception as e:
        print(f"Error in text generation: {e}")
        return None
    
    return generated_text[0]['generated_text']
 
    


def write_to_file(generated_text):
    '''
    Function writes results string into a file.
    Args:
        results (str): String to be written to a file.
        filename (str): Destination file path for the results.
    Returns:
        None
    '''
        # output file destination
    output_filename = os.path.join(
        os.environ.get(
            "_tapisExecSystemOutputDir",
            "text-generator-files"
        ),
        "output.txt"
    )
        
    try:
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        with open(output_filename, 'w', encoding="utf-8") as file:
            file.write(generated_text)
        print("Output written to", output_filename)
    except IOError:
        print("Error writing to file", output_filename)
    

def main():
    
    
    #Obtain and parse app arguments
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--model', default='distilgpt2', type=str, help='Text generation model name, please see: https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads')
    parser.add_argument('--statement', type=str, help='The sentence to be used for text generation')
    parser.add_argument('--sequence', default=2, type=int, help='Input to control how many different sequences are generated.')
    parser.add_argument('--max_output', default=100, type=int, help='Input to control the total length of the output text are generated.')
    parser.add_argument('--file', type=str, help='File to be used for text generation.')
    
    flags, _ = parser.parse_known_args()

    #Run the program
    print(write_to_file(gen_text(flags)))

if __name__ == "__main__":
    main()