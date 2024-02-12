import argparse, os
import constants

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
    
    statement = flags.statement    
    file = flags.file
    model = constants.DEFAULT_MODEL
    sequence = constants.SEQUENCE
    max_output = constants.MAX_OUTPUT

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
        
    try:
        os.makedirs(os.path.dirname(constants.DEFAULT_OUTPUT_FILE_PATH), exist_ok=True)
        with open(constants.DEFAULT_OUTPUT_FILE_PATH, 'w', encoding="utf-8") as file:
            file.write(generated_text)
        print("Output written to", constants.DEFAULT_OUTPUT_FILE_PATH)
    except IOError:
        print("Error writing to file", constants.DEFAULT_OUTPUT_FILE_PATH)
    

def main():
    
    
    #Obtain and parse app arguments
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--statement', type=str, help='The sentence to be used for text generation')
    parser.add_argument('--file', type=str, help='File to be used for text generation.')
    
    flags, _ = parser.parse_known_args()

    #Run the program
    print(write_to_file(gen_text(flags)))

if __name__ == "__main__":
    main()