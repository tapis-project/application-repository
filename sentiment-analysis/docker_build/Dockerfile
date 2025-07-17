FROM python:3.12

RUN pip install transformers

RUN pip install 'transformers[torch]'

COPY . /app

RUN chmod +x /app/analyze_sentiment.py

ENTRYPOINT ["python3", "/app/analyze_sentiment.py"]
