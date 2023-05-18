# Alpaca-style Fine Tuning

The Stanford Alpaca project describes an approach to fine tuning a LLM using a relatively small (e.g., 52k) instruction-following
dataset generated using the Self-Instruct method. Please refer to the Stanford Alpaca git repository and blog post for more 
information:

  * https://github.com/tatsu-lab/stanford_alpaca
  * https://crfm.stanford.edu/2023/03/13/alpaca.html


# Overview

The Tapis application defined here provides users with the ability to run the fine-tuning step as a Tapis batch job on a suitable execution
system, such as Frontera RTX queue.

## Build the Image
First, build the docker image

```
docker build -t jstubbs/alpaca -f Dockerfile-alpaca  .
```

Convert it to an apptainer image on the login node

```
module load tacc-apptainer
apptainer pull docker://jstubbs/alpaca
```

## Execute the Image

```
apptainer run --nv alpaca_latest.sif
```
