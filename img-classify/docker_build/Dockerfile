# image: tapis/img-classify:0.4
FROM tensorflow/tensorflow:1.5.0-py3

# Install necessary requirements
RUN pip install requests

# Copy the app into the container
ADD classify_image.py /classify_image.py

# Note: Using ENTRYPOINT makes this run immediately in non-interactive mode.
ENTRYPOINT ["python", "/classify_image.py"]
