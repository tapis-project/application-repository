#image tapis/sentiment-analysis:1.0.1

FROM huggingface/transformers-pytorch-cpu:4.18.0

COPY analyze_sentiment.py constants.py config.json /app/
RUN mkdir /.cache
RUN chmod 777 /.cache
WORKDIR /app

ENTRYPOINT ["python3","/app/analyze_sentiment.py"]
