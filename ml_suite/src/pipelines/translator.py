from transformers import pipeline


def translator(from_language, to_language, text):
    sentence_structure = f"translate {from_language} to {to_language}: {text}"
    translator = pipeline(task="translation", model="t5-small")
    print(translator(sentence_structure)[0]["translation_text"])
