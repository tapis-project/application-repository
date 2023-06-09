import sys, os
from transformers import pipeline

def gen_text(model_name: str, sentence: str, max_len: int, num_seq: int) -> list:
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
    try:
        max_num = int(max_len)
        num_seq = int(num_seq)
    except Exception as e:
        return f'Error: {e}. Please input integer for max_num and num_seq'

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
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as file:
            file.write(results)
        print("Output written to", filename)
    except IOError:
        print("Error writing to file", filename)

def main():
    # output file destination
    directory = "text-generator"
    filename = os.path.join(directory, "output.txt")

    # get input
    try:
        model_name = sys.argv[0]
        sentence = sys.argv[1]
        max_len = sys.argv[2]
        num_seq = sys.argv[3]
    except Exception as e:
        write_to_file(f'{e}\nNeed proper CLI inputs: <model_name>, <sentence>, <max_len> and <num_seq>\n', filename)
        return e
    
    # run model and get results
    model_output = gen_text(model_name, sentence, max_len, num_seq)
    if type(model_output) == list:
        results = ""
        for i in model_output:
            print(i["generated_text"])
            results += str(i["generated_text"]) + '\n'
    else:
        results = str(model_output) + '\n'

    write_to_file(results, filename)

    with open(filename, 'r') as file:
            print(file.read())

if __name__ == "__main__":
    main()