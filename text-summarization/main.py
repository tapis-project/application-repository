import argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

def execute_pipeline(text, minLength, maxLength):
    # Your pipeline code here
    model_path = 'models/'
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path, local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    print('Summarizer model loaded successfully')

    out = summarizer(text,
                         max_length= maxLength,
                         min_length= minLength)


    # Save output to a file
    with open("output.txt", "w") as f:
        f.write(out[0]['summary_text'])
    with open("output.txt", "r") as f:
        print(f.read())

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, 
                            default='Always set the memory reservation value below the hard limit, otherwise the hard limit takes precedence. A reservation of 0 is the same as setting no reservation. By default (without reservation set), memory reservation is the same as the hard memory limit.')
    parser.add_argument('--minLength', type=int, default=5)
    parser.add_argument('--maxLength', type=int, default=20)
    args = parser.parse_args()

    # Execute pipeline with provided inputs
    execute_pipeline(args.text,
                     args.minLength,
                     args.maxLength)
