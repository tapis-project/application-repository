# docker_build
This folder can be used to build docker images in order to run `sentiment_analysis.py`.

***analyze_sentiment.py***
- This python script contains all the necessary components to analyze any sentence that a user provides.

# Docker Image Handling
- This is assuming that docker is already installed on the system
## Pulling the image, `jaeestee/sentiment-analysis:02`, from Docker Hub:
To pull the existing image, run this command:
```bash
$ docker pull jaeestee/sentiment-analysis:0.2
```
If done properly, ``jaeestee/sentiment-analysis`` should show up with the tag ``latest`` when running this command:
```bash
$ docker images
```
> The output should look similar to this:
> ```
> REPOSITORY                    TAG    IMAGE ID       CREATED         SIZE
> jaeestee/sentiment-analysis   0.2    d8276d24fa21   2 hours ago     897MB
> ```

## Building the image:
To build the image, run this command:
```bash
$ docker build -t <DockerHub Username>/sentiment-analysis:<tag> .
```
- replace all the <> with custom 
If done properly, there should be a success message like this:
```
Successfully built d8276d24fa21
Successfully tagged jaeestee/sentiment-analysis:latest
```
## Running the image:
To run the image, run this command:
```bash
$ docker run jaeestee/sentiment-analysis:0.2 <arguments>
```
There are multiple arguments built into this application. Here are your options:
|Arguments|Explanation|Options|Example|
|---|---|---|---|
|sentence|The sentence to analyze. (Technically optional, but that's no fun)|Anything|--sentence='I love potatoes'|
|model|Model to use. (Optional)|[Link](https://huggingface.co/models?pipeline_tag=text-classification&sort=downloads)|--model='j-hartmann/emotion-english-distilroberta-base'|
|return all scores|Choose to either return all or only one score. Anything other than f or false is considered as true. Capitalization does not matter. (Optional as default is "True")|f, false, true|--return_all_scores='f'| 
