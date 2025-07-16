FROM python:3.12

RUN pip install transformers
RUN pip install 'transformers[torch]'

# copy the application into the app folder
COPY . /app
RUN chmod +x /app/analyze_sentiment.py

ENTRYPOINT ["python3", "/app/analyze_sentiment.py"]
# ENTRYPOINT ["python3", "-c", "print('hello world')"]
