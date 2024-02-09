import argparse, os

import constants

from bs4 import BeautifulSoup
from transformers import pipeline


def url_to_file(flags) -> str:
    '''
    Write the URL contents to a file 
    '''
    
    if flags.url == None:
        pass
    
    #Get content
    content = constants.GET_CONTENT(flags.url)
    soup = BeautifulSoup(content, 'html.parser')

    #Remove footer
    content_footer = soup.find('footer')
    if content_footer:
        content_footer.decompose()
    
    #Extract text and handle encoding
    content = soup.get_text()
    content.replace("\n", "").encode("utf-8", errors="replace").decode("utf-8")
    
    #Write content to file
    with open(f"./file_inputs/url_as_file.txt", "w", encoding="utf-8") as file:
        file.write(content)
    
def summarize(flags) -> str:
    '''
    Summarize the text.

    Args:
        text: The text to be summarized.
        minLength: The minimum length of the summary.
        maxLength: The maximum length of the summary.
        model_name: The name of the model to be used for summarization.
        url: URL to be summarized. 
    Returns:
        summary: The summarized text.
        '''
    
    text = flags.text
    model = constants.DEFAULT_MODEL #If you want to use the checkpoint model, change DEFAULT_MODEL to CHECKPOINT_MODEL
    file = flags.file
    url = flags.url
    url_file_used = './file_inputs/url_as_file.txt'
    
    if text == None and file == None and url == None:
        raise Exception("Must provide at least 1 statement with --text flag, 1 file with the --file, or 1 url with the --url.")
    
    if file and not os.path.isfile(file):
        raise Exception(f"A path provided in the --file flag is not a file | {file}")

    if text:
        pass
    elif file:
        with open(file, mode="r", encoding="utf-8") as file_obj:
            text = file_obj.read()
    else:       
       with open(url_file_used, mode="r", encoding="utf-8") as file_obj:
            text = file_obj.read()
    
    min_len = len(text) //20
    max_len = len(text) //10 
            
    output = pipeline('summarization', model=model)
    summary_result = output(text, min_length=min_len, max_length=max_len)

    if not summary_result:
        raise Exception("No summary result")

    return str(summary_result[0]['summary_text'].
               replace("\n", "").
               encode("ascii", errors="ignore").
               decode("utf-8"))


def write_to_file(summary_result):
    """
    Args:
        input_string:   The string to be written to a file
        filename:       The destiantion file path for the string

    Returns:
        None
    """
        
    try:
        os.makedirs(os.path.dirname(constants.DEFAULT_OUTPUT_FILE_PATH), exist_ok=True)
        with open(constants.DEFAULT_OUTPUT_FILE_PATH, 'w') as file:
            file.write(summary_result)
        print("Output written to", constants.DEFAULT_OUTPUT_FILE_PATH)
    except IOError:
        print("Error writing to file", constants.DEFAULT_OUTPUT_FILE_PATH)
        

def main():
    '''
    Main function to summarize text.

    #using argparse to rewrite the main function
    # adding args, flagging the statement to be summarized as mandatory
    # minLength and maxLength will have default values
    '''
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--text', type=str, help='This is the text that needs to be summarized.')
    parser.add_argument('--url', type=str, help='URL that can be summarized. ** NOTE this feature is limited to only lite sites with text only.')
    parser.add_argument('--file', type=str, help='files to be added intead of statement')

    flags, _ = parser.parse_known_args()

    #print(summary)
    try:
        url_to_file(flags)
    except:
        pass
    write_to_file(summarize(flags))


if __name__ == "__main__":
    main()
