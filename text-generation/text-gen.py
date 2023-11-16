import argparse, os, requests, sys

from bs4 import BeautifulSoup
from transformers import pipeline


def url_to_file(flags):
    #Get content
    content = requests.get(flags.url).text
    soup = BeautifulSoup(content, 'html.parser')

    
    #remove footer
    content_footer = soup.find('footer')
    if content_footer:
        content_footer.decompose()
    
    content = soup.get_text()
    content.replace("\n", "")
    
    #write content to file
    with open(f"./text-generator-files/url_as_file.txt", "w", encoding="utf-8") as file:
        file.write(str(content))

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
    max_output = flags.max_output
    file = flags.file
    url = flags.url
    url_file_used = "./text-generator-files/url_as_file.txt"

    if statement == None and file == None and url == None:
        raise Exception("You must provide either a statement, a file, or a URL")
    
    if file and not os.path.isfile(file):
        raise Exception(f"A path provided in the --file flag is not a file | {file}")


    if file == None:
        with open(url_file_used, mode="r", encoding="utf-8") as file_obj:
            statement = file_obj.read()
    else:
        with open(file, mode="r", encoding="utf-8") as file_obj:
            statement = file_obj.read()

    try:
        output = pipeline("text-generation")
        generated_text = output(statement, model=model, max_length=max_output, num_return_sequences=sequence)
    except Exception as e:
        return e

    return(str(generated_text[0]['generated_text'].replace("'\n'", "").encode("utf-8")))


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
        with open(output_filename, 'w') as file:
            file.write(generated_text)
        print("Output written to", output_filename)
    except IOError:
        print("Error writing to file", output_filename)
        
    #with open(filename, 'r') as file:
    #print(file.read())
    

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
    print(write_to_file(gen_text(flags)))

if __name__ == "__main__":
    main()