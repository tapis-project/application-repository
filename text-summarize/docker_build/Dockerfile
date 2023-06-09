# image: tapis/text-summarize:0.1
FROM huggingface/transformers-pytorch-cpu

# Install necessary requirements
RUN pip install requests
RUN pip install lxml

# Copy the app into the container
# Need to run in /tmp to avoid permissions problem when not running as root
ADD summarize-text.py /tmp/summarize-text.py
WORKDIR /tmp

# Note: Using ENTRYPOINT makes this run immediately in non-interactive mode.
ENTRYPOINT ["python3", "/tmp/summarize-text.py"]
