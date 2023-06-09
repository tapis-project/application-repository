import json
from transformers import pipeline

def gen_text(sentence: str, max_len: int, num_seq: int) -> list:
    '''
    Function to generate text from input sentence, using the TextGenerationPipeline from huggingface. 
    
    Args:
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

    generator = pipeline("text-generation", model="distilgpt2")

    try:
        output_text = generator(sentence, max_length=max_len, num_return_sequences=num_seq,)
    except Exception as e:
        return e

    return (output_text)

def main():
    sentence = input('Sentence prompt: ')
    max_len = input('Maximum output length (int): ')
    num_seq = input('Desired number of sequences to generate (int): ')

    model_output = gen_text(sentence, max_len, num_seq)
    results = {'text_output': model_output}

    # write results into a json file
    with open('text_output.json', 'w') as out:
        json.dump(results, out, indent=2)

if __name__ == "__main__":
    main()