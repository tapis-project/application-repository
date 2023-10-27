from transformers import pipeline

def sentiment_analysis(*sentences):
    predictions_list = []
    for sentence in sentences:
        classifier = pipeline(task="sentiment-analysis")
        predictions = classifier(sentence)
        pretty_predictions = [{"score": round(prediction["score"], 4), "label": prediction["label"]} for prediction in predictions]
        predictions_list.extend(pretty_predictions)
    
    return predictions_list
    print(predictions_list)    