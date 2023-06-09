import argparse

from transformers import pipeline

FLAGS = None

def analyze():
    """
    Function that analyzes the sentence that the user provided.

    Returns:
        results (List): sentiment analysis results.
    """
    returnAllScores = FLAGS.return_all_scores != 'False'
    analyzer = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=returnAllScores)
    results = analyzer(FLAGS.sentence)

    return results

def print_results(results):
    """
    Function that prints the results.

    Args:
        results (List): The results of the analysis.
    """
    if FLAGS.sentence == '':
        print("There was no sentence to analyze.")
    else:
        print("The sentence: " + FLAGS.sentence)
        if FLAGS.return_all_scores == 'False':
            label = results[0]['label']
            score = results[0]['score']
            print(f'{label}: {score:.2%}')
        else:
            for res in results[0]:
                label = res['label']
                score = res['score']
                print(f'{label}: {score:.2%}')

def main():
    results = analyze()
    print_results(results)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sentence', type=str, default='', help='Sentence for analyzing.')
    parser.add_argument('--return_all_scores', type=str, default='True', help='Option to return all scores.')
    FLAGS, unparsed = parser.parse_known_args()
    main()