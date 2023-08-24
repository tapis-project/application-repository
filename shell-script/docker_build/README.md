# Details

This folder contains all files needed to build a docker image that can be used to run a Tapis basic shell-script
application using docker or singularity.

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
docker build -f Dockerfile -t my-shell-script:0.1 .
```

## Dockerfile

Uses ubuntu as base image for running the script. Adds the script into the container. Uses ENTRYPOINT to run
the script immediately in non-interactive mode.

## shell_script.sh

The script checks:

- number of arguments are as expected
- values of arguments are as expected
- environment variables listed in shell_script.env are set
- environment variables listed in shell_script.env are set with expected values

### Running script manually

The script shell_script.sh should run successfully from this directory with the env variables
from file shell_script.env set.

To run the script shell_script.sh manually and confirm results were written to output file:
```
. ./shell_script.env
./shell_script.sh arg1 arg2
cat ./shell_script.out
```

In order to test the application using the docker image, run a command similar to the following:

```docker run -e MY_ENV1=env_1_value <NAME_OF_IMAGE> arg1 arg2```

For example:

```
docker run -e MY_ENV1=env_1_value my-shell-script:0.1 arg1 arg2
```
