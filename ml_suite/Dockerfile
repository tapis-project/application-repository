FROM python:3.8

# Create directories
RUN mkdir src  \
    && mkdir /inputs 

# Copy requirements and install dependencies
COPY src/requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip install -r requirements.txt

# Copy src directory into container
COPY src /src
