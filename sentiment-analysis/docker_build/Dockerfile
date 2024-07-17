#image tapis/sentiment-analysis:0.1

FROM huggingface/transformers-pytorch-cpu:4.18.0

COPY analyze_sentiment.py constants.py config.json /app/
WORKDIR /app

ENTRYPOINT ["python3","/app/analyze_sentiment.py"]
