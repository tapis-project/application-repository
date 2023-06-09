# Details

There are two files for building docker images. One for running the application using docker and one for running the
application using singularity.

## Prerequisites

In order to run most of the commands discussed below, you will need to be on a host that has docker installed and
configured. To test this you can run the following commands:

```
docker --version
docker images
```

In order to test the image built for singularity, you will need to be on a host that has singularity installed and
configured. To test this you can run the following commands:

```
singularity --version
singularity cache list
```

## Creating docker images

To build the image for local testing using docker, download this folder and navigate to it on the command line,
then run commands similar to the following:

```
docker build -f Dockerfile -t my-text-summarize:0.1 .
docker build -f Dockerfile_singularity -t my-text-summarize-sing:0.1 .
```

## Dockerfiles

The images are built upon TensorFlow's official _tensorflow_ image, which is itself based on Ubuntu Linux version 18.04.

## classify_img.py

The url to be processed is passed in through the command line using the _--url argument.
In order to test the application using the docker image, run a command similar to the following:

```docker run <NAME_OF_IMAGE> --url=<url>```

For example:

```
docker run --rm my-text-summarize:0.1 --url=https://text.npr.org/1180869821
```
 
Note that you should also be able to use docker to test the image created using the file Dockerfile_singularity.

In order to test the image built for singularity, you will need to be on a host that has singularity installed and
configured. To test you can run a command similar to the following:

```
singularity run docker://my-text-summarize-sing:0.1 --url=https://text.npr.org/1180869821
```
