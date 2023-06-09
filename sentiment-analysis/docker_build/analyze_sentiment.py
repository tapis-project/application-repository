import argparse, csv
from transformers import pipeline

FLAGS = None

def analyze() -> list:
    """
    Function that analyzes the sentence that the user provided.

    Args:
        FLAGS.sentence (str): The sentence to be analyzed.  
        FLAGS.return_all_scores (str): Option to return all scores or just the highest.
        FLAGS.model (str): A custom model from the Hugging Face hub.
            - optional model: j-hartmann/emotion-english-distilroberta-base

    Returns:
        results (List): sentiment analysis results.
    """
    #the returnAllScores will always default to True, unless False is given
    returnAllScores = FLAGS.return_all_scores.lower() not in ('false', 'f')

    #if the model is empty, it uses a basic model, else uses provided model
    if not FLAGS.model:
        analyzer = pipeline("sentiment-analysis", return_all_scores=returnAllScores)
    else:
        #try-except block to make sure that the model name given exists
        try:
            analyzer = pipeline("sentiment-analysis", model=FLAGS.model, return_all_scores=returnAllScores)
        except Exception as e:
            return "Error: Model does not exist." 

    results = analyzer(FLAGS.sentence)

    return results

def print_results(results: list):
    """
    Function that prints the results.

    Args:
        results (List): The results of the analysis.
    """
    #if there was no sentence provided, prints this message, else prints the results
    with open('results.csv', 'w') as file:
        writer = csv.writer(file)

        if FLAGS.sentence == '':
            writer.writerow(["There was no sentence to analyze."])
        else:
            writer.writerow(["The sentence", FLAGS.sentence])
            if FLAGS.return_all_scores.lower() in ('false', 'f'):
                label = results[0]['label']
                score = results[0]['score']
                writer.writerow([label, '{:.2%}'.format(score)])
            else:
                for res in results[0]:
                    label = res['label']
                    score = res['score']
                    writer.writerow([label, '{:.2%}'.format(score)])
        file.close()

def main():
    results = analyze()
    if "Error" in results:
        with open('results.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow([results])
            file.close()
    else:
        print_results(results)

    with open('results.csv', 'r') as file:
        print(file.read())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--sentence', type=str, default='', help='Sentence for analyzing.')
    parser.add_argument('--return_all_scores', type=str, default='True', help='Option to return all scores.')
    parser.add_argument('--model', type=str, default='', help='Optional model name')

    FLAGS, unparsed = parser.parse_known_args()

    main()