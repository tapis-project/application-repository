import argparse, os, requests, sys

from bs4 import BeautifulSoup

from transformers import pipeline


def url_to_file(flags):
    #Get content
    content = requests.get(flags.url).text
    prettified_content = BeautifulSoup(content, 'html.parser').prettify()
    soup = BeautifulSoup(content, 'html.parser')

    #write content to file
    with open(f"./text-generator-files/url_as_file.txt", "w", encoding="utf-8") as file:
        file.write(prettified_content)

    print(soup.title.string)
"""
def gen_text(flags):
    
    '''
    Function to generate text from input sentence, using the TextGenerationPipeline from huggingface. 
    Args:
        model_name (str): Text generation model name, please see: https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads
        sentence (str): The input sentence for text generation.
        max_num (int): Input to control the total length of the output text are generated.
        num_seq (int): Input to control how many different sequences are generated.
    Output:
        output_text (list): Based on the sentence prompt, the model will auto-complete it by generating the remaining text in the text length and number of sequences specified.
    '''
    
        
    model = flags.model
    statement = flags.statement
    sequence = flags.sequence
    max_output = flags.max_output
    file = flags.file
    
    try:
        max_len = int(max_len)
        num_seq = int(num_seq)
    except Exception as e:
        return f'Error: {e}. Please input integer for max_len and num_seq'

    try:
        generator = pipeline("text-generation", model=model_name) # tested using "distilgpt2"
    except Exception as e:
        return f'Error: {e}. Please check if model inputted is compatible.'

    try:
        output_text = generator(sentence, max_length=max_len, num_return_sequences=num_seq,)
    except Exception as e:
        return e

    return (output_text)

def write_to_file(results: str, filename: str):
    '''
    Function writes results string into a file.
    Args:
        results (str): String to be written to a file.
        filename (str): Destination file path for the results.
    Returns:
        None
    '''
        # output file destination
    directory = "text-generator"
    filename = os.path.join(directory, "output.txt")
    
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as file:
            file.write(results)
        print("Output written to", filename)
    except IOError:
        print("Error writing to file", filename)
        
    #with open(filename, 'r') as file:
    #print(file.read())

"""
def main():
    
    
    #Obtain and parse app arguments
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--model', default='distilgpt2', type=str, help='Text generation model name, please see: https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads')
    parser.add_argument('--statement', type=str, help='The sentence to be used for text generation')
    parser.add_argument('--sequence', default=2, type=int, help='Input to control how many different sequences are generated.')
    parser.add_argument('--max_output', default=10, type=int, help='Input to control the total length of the output text are generated.')
    parser.add_argument('--file', type=str, help='File to be used for text generation.')
    parser.add_argument('--url', type=str, help='URL to be used for text generation.')
    
    flags, _ = parser.parse_known_args()

    #Run the program
    url_to_file(flags)

if __name__ == "__main__":
    main()