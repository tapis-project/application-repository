#image jaeestee/sentiment-analysis:0.2

FROM huggingface/transformers-pytorch-cpu:4.18.0


#copy the application into the app folder
ADD analyze_sentiment.py /app/analyze_sentiment.py
ADD constants.py /app/constants.py
ADD config.json /app/config.json
WORKDIR /app


ENTRYPOINT ["python3","/app/analyze_sentiment.py"]
