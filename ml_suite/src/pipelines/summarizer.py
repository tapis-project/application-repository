from transformers import pipeline


def summarizer(text):
    summarize=pipeline(task="summarization")
    print(summarize(text)[0]["summary_text"])