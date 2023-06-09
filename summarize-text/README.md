# Summarize-Text
## Text Summarization using HuggingFace Models
A description of the text summarization model can be found [here](https://huggingface.co/docs/transformers/tasks/summarization).

This is an application that performs the text summarization model in the HPC system.

For example, for the following arguments:
```
{
    "name": "summarize-text",
    "appId": "summarize-text-by-prit",
    "appVersion": "0.1.1",
    "execSystemId": "<system name>",
    "parameterSet": {
        "appArgs": [
            {
                "arg": "'The Tapis framework is an application programming interface (API) hosted in the cloud. Using Tapis, computational researchers can manage data and execute software on a variety of different systems, including bare metal servers, virtual machines (VMs) and high-performance computing (HPC) clusters. This website contains a collection of self-paced tutorials for learning how to incorporate Tapis into computational research workflows.'"
            },
            {
                "arg": "5"
            },
            {
                "arg": "25"
            }
        ]
    }
}
```

The output is
```
Output written to saved_outputs/summary.txt
this website contains a collection of self-paced tutorials for learning how to incorporate Tapis into computational research workflows
```
