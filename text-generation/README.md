# Text-Generation
Application for the text-generation NLP model using TextGenerationPipeline from huggingface. A detailed description can be found in the [documentation](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.TextGenerationPipeline). The model is designed to run on an HPC system at TACC and is created as part of SGX3 program.

## Details
The text-generation model is a language model designed to generate new text. Based on the sentence prompt, the model will auto-complete it by generating the remaining text in the text length and number of sequences specified.

This directory contains the `app.json` file to define the application using the `dhannywi/text-generation:0.2` docker image.

The `job.json` defines the jobs definition to be submitted to the HPC cluster through a client.

The `job.json` file takes in four arguments; the model name, the sentence input, the total length of text and the number of sequences to generate.


## Usage
For example, using the following arguments:
```
{
    "name": "text-generation-job",
    "appId": "text-generation-dwi67",
    "appVersion": "0.2.0",
    "execSystemId": "<system name>",
    "parameterSet": {
        "appArgs": [
            {
                "arg": "distilgpt2" 
            },
            {
                "arg": "'Once upon a time'"
            },
            {
                "arg": "30"
            },
            {
                "arg": "2"
            }
        ]
    }
}
```


Return the following output in `text-generator/output.txt`:
```
{'generated_text': 'Once upon a time of opportunity, it is impossible to explain the difference between this belief and a belief that is held up by other individuals. And of'}
{'generated_text': "Once upon a time when America's middle classes have been under such intense pressure, their government doesn't want it. They want it. They want it"}
Output written to text-generator/output.txt
Once upon a time of opportunity, it is impossible to explain the difference between this belief and a belief that is held up by other individuals. And of
Once upon a time when America's middle classes have been under such intense pressure, their government doesn't want it. They want it. They want it
```

## Note:
```
As of right now, TACC uses pretrained, default models from huggingface. The text generated from these models is not reflecting of TACC. Please be aware that the generation of text may be unpredictable and may have language that some may find insensitive or inappropriate. User discretion is advised.  
```