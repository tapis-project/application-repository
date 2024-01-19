import argparse, os, requests
import pandas as pd


from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image


def use_model(flags):
    """
    :Name: use_model
    :Desctription: load_model loads the selected huggingface model to infer the visual-QA

    :param processor: Processor that processes the PIL image to tensor format
    :param model: The huggingface model that generates response to the question against the image
    :param image_question: The image and question pair 

    :return result: returns the selected answer to the question against the image
    """ 
    result = []
    image_questions = {flags.imageurl[0]: flags.question}
    model = ViltForQuestionAnswering.from_pretrained(flags.model)
    processor = ViltProcessor.from_pretrained(model)
    
    for image_url, questions in image_questions.items():
        image_pil = None
        try:
            image_pil = Image.open(requests.get(image_url, stream=True).raw)
        except:
            result.append((image_url, "No image URL or image found to answer the question."))
            continue
        
        for question in questions:
            encoding = processor(image_pil, question, return_tensors="pt")
            outputs = model(**encoding)
            logits = outputs.logits
            idx = logits.argmax(-1).item()
            result.append((image_url, question, model.config.id2label[idx]))

    if not result:
        result.append(("No image URL or image found to answer the question.",))

    return result


def store_results_display(result, display=True):
    """
    :Name: store_results_display
    :Desctription: Stores the Results in 'resullts_folder' with name 'resultfile' and conditionally displays the results

    :param result: responses to the questions
    :param display: True/False to either display results on screen or not
    :param resullts_folder: Target folder to save the results
    :param resultfile: The file to save the results

    :return: None
    """ 
    results_folder_file = os.path.join(
        os.environ.get(
            "_tapisExecSystemOutputDir",
            "results_folder"
        ),
        "results_file.csv"
    )
    results_folder = os.path.dirname(results_folder_file)
    


    results_df = pd.DataFrame(result, columns=['Image', 'Question', 'Answer'])
    results_df.to_csv(os.path.join(results_folder, "results_file.csv"), index=False)
                                  
    if display:
        for ind in results_df.index:
            print("In the image: ", results_df['Image'][ind], ", for the question: ", results_df['Question'][ind], ", the answer is: , ", results_df['Answer'][ind])      
    

def main():
    """
    :Name: entry point
    :Desctription: Takes in the command line arguments and performs Visual-QA
    """ 
    
    parser = argparse.ArgumentParser(description='Please provide an image url and a question w.r.t. the image')

    parser.add_argument("-i", "--imageurl", nargs="+", default=["http://images.cocodataset.org/val2017/000000039769.jpg"], help="Enter url to an image") 
    parser.add_argument("-q", "--question", nargs="+", default=[" What is this image?"], help="Enter a question w.r.t an image")   
    parser.add_argument("-m", "--model", default="dandelin/vilt-b32-finetuned-vqa", help="Option to use any model. Default model is dandelin/vilt-b32-finetuned-vqa")                                                   

    flags, _ = parser.parse_known_args()

    
    store_results_display(use_model(flags))

if __name__ == "__main__":
    main()