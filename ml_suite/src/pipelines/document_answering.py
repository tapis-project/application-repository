import requests

from transformers import pipeline

from PIL import image


url = "https://datasets-server.huggingface.co/assets/hf-internal-testing/example-documents/--/hf-internal-testing--example-documents/test/2/image/image.jpg"
image = Image.open(requests.get(url, stream=True).raw)

doc_question_answerer = pipeline("document-question-answering", model="magorshunov/layoutlm-invoices")
preds = doc_question_answerer(
    question="What is the total amount?",
    image=image,
)
print(preds)