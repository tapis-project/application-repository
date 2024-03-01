
FROM huggingface/transformers-pytorch-cpu:4.18.0

COPY summarize.py /app/summarize.py

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "/app/summarize.py" ]