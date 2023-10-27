import argparse, csv, os

from typing import List, Tuple
from typing_extensions import TypedDict

from transformers import pipeline


class Analysis(TypedDict):
    label: str
    score: float

AnalysisResult = List[Tuple[str, Analysis]]

def analyze(flags) -> AnalysisResult:
    """
    Function that analyzes the sentence that the user provided.

    Args:
        flags.sentence (str): The sentence to be analyzed.  
        flags.return_all_scores (str): Option to return all scores or just the highest.
        flags.model (str): A custom model from the Hugging Face hub.
            - optional model: j-hartmann/emotion-english-distilroberta-base

    Returns:
        results (List): sentiment analysis results.
    """
    # if the model is empty, it uses a basic model, else uses provided model
    model = flags.model if flags.model else None
    try:
        analyzer = pipeline("sentiment-analysis", model=model, return_all_scores=True)
    except Exception as e:
        raise Exception(f"Pipeline instantiation error: {e}")
    
    sentences = flags.sentences if flags.sentences != None else []
    
    files = flags.files if flags.files != None else []
    
    if len(files) == 0 and len(sentences) == 0:
        raise Exception("Must provide at least 1 sentence with --sentences flag or at least 1 file with the --files.")
    
    for path in files:
        if not os.path.isfile(path):
            raise Exception(f"A path provided in the --files flag is not a file | {path}")
        
        with open(path, mode="r") as file:
            sentences.append(file.read())
            
    analyses = analyzer(sentences)

    results = []
    for i, analysis in enumerate(analyses):
        results.append((sentences[i], analysis))
    print(results)
    return results

def store_results(results: AnalysisResult) -> None:
    """
    Function that stores the results into a csv file.

    Args:
        results (List): The results of the analysis.
    """
    
    #if there was no sentence provided, prints this message, else prints the results
    with open(
        os.path.join(os.environ.get("_tapisExecSystemOutputDir", ""), 'results.csv'),
        mode='a',
        newline=''
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["SENTENCE","POSITIVE", "NEGATIVE"])
        for sentence, analysis in results:
            writer.writerow([
                sentence, 
                next(filter(lambda analysis: analysis["label"] == "POSITIVE", analysis)),
                next(filter(lambda analysis: analysis["label"] == "NEGATIVE", analysis)),
            ])
    
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--sentences', type=str, nargs="+", help='Sentence for analyzing.')
    parser.add_argument('--model', type=str, default='', help='Optional model name')
    parser.add_argument('--files', type=str, nargs="+", help='File(s) upon which to run sentiment analysis')

    # args = parser.parse_args()
    
    flags, _ = parser.parse_known_args()
    store_results(analyze(flags))

if __name__ == '__main__':
    main()
