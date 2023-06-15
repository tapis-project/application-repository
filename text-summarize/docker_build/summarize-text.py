"""Simple text summarization of news article.
Model and pipline from https://huggingface.co/
This program summarizes news article.
Change the --url argument to a specific url in https://text.npr.org
"""
from __future__ import print_function
import argparse
import sys

from lxml import html
from transformers import pipeline
import requests

def run_summarize(url, model_name):
  summarizer = pipeline("summarization", model=model_name)
  page = requests.get(url)
  tree = html.fromstring(page.content)

  plain_text = ','.join(tree.xpath(".//div[@class='paragraphs-container']//text()"))
  plain_text = str(plain_text.encode('ascii', 'ignore'))
  print(plain_text)
  print(summarizer(plain_text, max_length=130, min_length=30, do_sample=False))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--url',
      type=str,
      default='https://text.npr.org/1180869821',
      help='A url from the list in https://text.npr.org/'
  )
  parser.add_argument(
      '--model_name',
      type=str,
      default='facebook/bart-large-cnn',
      help='Name of the hugging face model from https://huggingface.co/'
  )  
  args = parser.parse_args()
  run_summarize(args.url, args.model_name)