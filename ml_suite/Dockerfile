FROM python:3.8
RUN mkdir src
COPY src/requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip install -r requirements.txt
COPY src /src
