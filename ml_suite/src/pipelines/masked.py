from transformers import pipeline 

def mask_fill(*texts):
    predictions_list = []
    fill_mask = pipeline(task="fill-mask")
    
    for text in texts:
        predictions = fill_mask(text, top_k=1)
        pretty_predictions = [{"score": round(pred["score"], 4), "label": pred["token_str"]} for pred in predictions]
        predictions_list.extend(pretty_predictions)
        
    print(predictions_list)