from transformers import pipeline


def language_model_casual(prompt):
    generator = pipeline(task="text-generation")
    print(generator(prompt)[0]["generated_text"])
