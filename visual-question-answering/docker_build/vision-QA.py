import argparse, os, re, requests
import random, time, json
import pandas as pd


from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image


def use_model(image_question=None):
    """
    :Name: use_model
    :Desctription: load_model loads the selected huggingface model to infer the visual-QA

    :param processor: Processor that processes the PIL image to tenser format
    :param model: The huggingface model that generates resoponse to the question againt the image
    :param image_question: The image and question pair 

    :return result: retunrs the selected answer to the question against the image
    """ 
    result =[]
    model = flags.model
    image_question = flags.image_question
    
    
    if model:
        for i_q_pair in image_question:
            image_pil=  None
            try:
                image_pil = Image.open(requests.get(i_q_pair[0], stream=True).raw)
            except:
                result.append(("NO IMAGE", "N/A", "ERROR: No image found to answer the question!"))
                return result
            for qu in i_q_pair[1]:
                encoding = processor(image_pil, qu, return_tensors="pt")
                outputs = model(**encoding)
                logits = outputs.logits
                idx = logits.argmax(-1).item()
                result.append((i_q_pair[0], qu, model.config.id2label[idx]))
    else:
        result.append(("NO MODEL", "NO MODEL", "ERROR: No model found to answer the question!"))

    return result

def store_results_display(results, display=True, resullts_folder="Answers", resultfile="answers.csv"):

    """
    :Name: store_results_display
    :Desctription: Stores the Results in 'resullts_folder' with name 'resultfile' and conditionally displays the results

    :param results: responses to the questions
    :param display: True/False to either display results on screen or not
    :param resullts_folder: Target folder to save the results
    :param resultfile: The file to save the results

    :return: None
    """ 

    results_df = pd.DataFrame(results, columns =['Image', 'Question', 'Answer'])
    results_df.to_csv(index=False)

    os.makedirs(resullts_folder, exist_ok=True)  
    op_file = os.path.join(resullts_folder, resultfile)
    results_df.to_csv(op_file)  
    if display:
        for ind in results_df.index:
            print("In the image:", results_df['Image'][ind], ", for the question: ", results_df['Question'][ind], ", the answer is:, ", results_df['Answer'][ind],)


def convert_string_2_questions(listquestions=""):
    """
    :Name: convert_string_2_questions
    :Desctription: Take s string representation of questions (strings) list and converts to a list of questions (strings)

    :param listquestions:  string representation of questions taked from the commandline arguments
    
    :return: list of questions (strings)
    """ 
    b = re.sub(r'[\[\]]', '', listquestions)
    b = re.sub(r'\',', '\'<SPLIT>', b)
    b = re.sub(r'\'', '', b)
    bl = b.split("<SPLIT>")
    questions = []
    for q in bl:
        ques = q.strip()
        questions.append(ques)
    return questions


def generate_sample_images_n_store(noOfSamples=10, display=True, samples_folder="Samples", samplefile="Samples.txt"):
    """
    :Name: generateSampleImagesAndStore
    :Desctription: Generates a sample set of IMAGE URLS (from COCO validation dataset 2017 - https://cocodataset.org/#home)

    :param noOfSamples: responses to the questions
    :param display: True/False to either display sample URLs on screen or not
    :param samples_folder: Target folder to save the samples URLs
    :param samplefile: The file to save the sample URLs

    :return sampleList: List of generated sample URLs 
    """ 

    f = open('/app/sample_images.json')
    data = json.load(f)
    f.close()
    imagelist = data["imageList"]
        
    sampleList=[]
    sampleList=random.sample(imagelist,noOfSamples)

    if display:
        print("Some sample URLS:")
        for sample in sampleList:
            print(sample)
    
    os.makedirs(samples_folder, exist_ok=True)  
    op_file = os.path.join(samples_folder, samplefile)
    f = open(op_file, "w")
    f.write("\n".join(sampleList))
    f.close()

    return sampleList


def main():
     """
    :Name: entry point
    :Desctription: Tages in the command like argimnets and performs Visual-QA
    """ 
    
    parser = argparse.ArgumentParser(description='Please provide an image url and a question w.r.t. the image')

    parser.add_argument("-o", "--output", default="Samples", help="Path to save the results:") 
    parser.add_argument("-t", "--inputtype", default="samplelist", help="Mention the type of input (pair=input and question, pairlist = image and list of questions, samplelist = to generate a random sample of image urls for reference and store in output foler as 'Samples.txt')")   
    parser.add_argument("-i", "--imageurl", default="http://images.cocodataset.org/val2017/000000039769.jpg", help="Enter url to an image") 
    parser.add_argument("-q", "--question", nargs="+", default="How many cats in image?", help="Enter a question w.r.t an image")   
    parser.add_argument("-m", "--model", default="", help="Option to use any model. Default model is")                                                   

    args = parser.parse_args()
    flags, _ = parser.parse_known_args()


    if args.inputtype == "samplelist":
        sampleList= generate_sample_images_n_store(samples_folder=args.output)
    else:
        processor, model = load_model()

        questionslist = []
        if args.inputtype == "pair":
            questionslist=[args.question]
        else:
            questionslist = convert_string_2_questions(args.questionlist)
    
    
        img_q_pair =[(args.imageurl, questionslist)]
        results = use_model(processor, model, img_q_pair)
        store_results_display(results, display=True, resullts_folder=args.output, resultfile="answers.csv")



if __name__ == "__main__":
    main()



#TODO processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
# Decide if processor is actually needed or required. 
