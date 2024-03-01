# docker image: dhannywi/text-generation:0.1
# execute command: docker run dhannywi/text-generation:0.1

FROM huggingface/transformers-pytorch-cpu:4.18.0

COPY text-gen.py /app/text-gen.py

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "/app/text-gen.py" ]