import argparse

from transformers import pipeline

def analyze():
    """
    Function that analyzes the sentence that the user provided.
    """
    returnAllScores = FLAGS.return_all_scores == 'True'
    classifier = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=returnAllScores)
    print_results(classifier(FLAGS.sentence))

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
        if FLAGS.return_all_scores != 'True':
            label = results[0]['label']
            score = results[0]['score']
            print(f'{label}: {score:.2%}')
        else:
            for res in results[0]:
                label = res['label']
                score = res['score']
                print(f'{label}: {score:.2%}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sentence', type=str, default='', help='Sentence for analyzing.')
    parser.add_argument('--return_all_scores', type=str, default='True', help='Option to return all scores.')
    FLAGS, unparsed = parser.parse_known_args()
    analyze()