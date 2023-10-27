from transformers import pipeline


def question_answering(question, context):
    question_context = f"{question} {context} "
    question_answerer = pipeline(task="question-answering")
    print(question_answerer(question_context))
    
    #prediction = question_answerer(
    #    question = "what is the name of the repository",
    #    context=  "The name of the repository is huggingface/transformers",
    #)
    #print(
    #    f"score: {round(prediction['score'], 4)}, start: {prediction['start']}, end: prediction{prediction['end']}, answer{prediction['answer']}"
    #)