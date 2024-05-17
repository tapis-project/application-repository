#image jaeestee/sentiment-analysis:0.2
FROM huggingface/transformers-pytorch-cpu:4.18.0

#copy the application into the app folder
COPY analyze_sentiment.py /app/analyze_sentiment.py

ENTRYPOINT ["/app/analyze_sentiment.py"]