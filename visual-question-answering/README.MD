# Project Title

A huggingface model for Visual Question answering

## Description

This project provied a sample application that loads a docker image which runs a simple higgingface interfcae for visual question answering using TAPIS API Calls. 

## Getting Started

### Dependencies

* HiggingFace, Docker, Pytorch
* Access to TAPIS Account

### Installing

* After making any change to the Vision-QA.py, 'build' the docker image from withon the 'docker_build' folder, test it with the 'run' command and 'push' it to an accessible drive.
```
$ docker build -f <DockerFileName> -t <name-space>/<image-name>:<version> .
$ docker run <name-space>/<image-name>:<version>
$ docker push <name-space>/<image-name>:<version>

```
An example: 
```
$ docker build  -f Dockerfile_GPU -t swathimanikya/vision-qa:0.0.1 .
$ docker run swathimanikya/vision-qa:0.0.1
$ docker push swathimanikya/vision-qa:0.0.1
```

* To run on a GPU system:
    - Build docker image using file Dockerfile_GPU (https://hub.docker.com/r/huggingface/transformers-tensorflow-gpu)
    - (or simply) use docker Image swathimanikya/vision-qa:0.0.1

* To run on a CPU system:
    - Build docker image using file Dockerfile_CPU (https://hub.docker.com/r/huggingface/transformers-tensorflow-cpu)
    - (or simply) use docker Image swathimanikya/vision-qa:0.0.2

### Executing program

* Follow example.ipynb to  establish a TAPIS connection and run the application on TACC systems.
* Enter your "<Enter TACC Username>" at the following places:
    - system definition "effectiveUserId":"<Enter TACC Username>"
    - client.systems.createUserCredential(systemId=system_id_hpc,userName='<Enter TACC Username>',privateKey=privateKey, publicKey=publicKey)

## Help

N/A

## Authors

Manikya Swathi Vallabhajosyula

## Version History

* 0.0.1
   
    * Initial Release

## License
