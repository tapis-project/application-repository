# sentiment-analysis
This application utilizes the sentiment analysis pipeline from Hugging Face.
It is categorized under the Natural Language Processing: Text Classification.
For more information click [here](https://huggingface.co/tasks/text-classification).

This application is reliant on a job, therefore not interactive. 

***app_definition.json***
- App definition written in Json format defining the specific image and other parameters to be used in Tapis.

```
{
    "id": "<id>-sentiment-analysis",
    "version": "0.2",
    "description": "Application utilizing the sentiment analysis model from Hugging Face.",
    "jobType": "BATCH",
    "runtime": "SINGULARITY",
    "runtimeOptions": ["SINGULARITY_RUN"],
    "containerImage": "docker://jaeestee/sentiment-analysis:0.2",
    "jobAttributes": {
        "parameterSet": {
            "archiveFilter": { 
                "includeLaunchFiles": false 
            }
        },
        "memoryMB": 1,
        "nodeCount": 1,
        "coresPerNode": 1,
        "maxMinutes": 10
    }
}
```
> Replace <id> to make the application id unique as that is a requirement in the Tapis environment.

***job_definition.json***
- Job definition written in Json format defining parameters and arugments to be used.

```
{
    "name": "sentiment-analysis-job",
    "appId": "<id>-sentiment-analysis",
    "appVersion": "0.2",
    "execSystemId": "<system name>",
    "parameterSet": {
        "appArgs": [
            {"arg": "--sentence"},
            {"arg": "'<sentence>'"},
            {"arg": "--return_all_scores"},
            {"arg": "<True/False>"},
            {"arg": "--model"},
            {"arg": "<Model>"}
        ]
    }
}
```
> Replace <id> with the same id used above. Replace <sentence>, <True/False>, and/or <Model> with proper values explained in the `README.md` in the `docker_build` directory. [Click here to get there faster.](https://github.com/jaeestee/application-repository/tree/main/sentiment-analysis/docker_build#running-the-image)
> If certain arguments are not wanted, make the argument value empty. aka, leave it as `""`.
