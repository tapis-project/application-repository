# img-classify

This is an app that performs image classification using Tensorflow on HPC hardware. It was demonstrated in a [tutorial](https://github.com/TACC-Cloud/gateways21-portable-computing-cloud-hpc) presented by TCC at the SCGI Gateways 2021 conference. 
<br><br>


## Details

The img-classify app is non-interactive. Once a job using this app has been submitted, the input files provided in the job submission body are automatically staged and classifcation is performed. The output can be found in the output directory specified in the app definition ("execSystemOutputDir"). 
<br><br>


## Using the img-classify app

Use the _app_definition.json_ file as a reference for creating the img-classify app. Simply download the file or copy its contents and [create the app](https://tapis.readthedocs.io/en/latest/technical/apps.html#creating-an-application).

To run the app on a specified system instead of a publicly shared one, users can add an "execSystemId" key-value pair under the "jobAttributes" field in the app definition:

```
{
    ...,

    "containerImage": "docker://tapis/img-classify:0.1",
    "jobAttributes": {
        "execSystemId": <SYSTEM_NAME_HERE>,
        "execSystemExecDir": "${JobWorkingDir}/jobs/${JobUUID}",
        
        ...
}
```
<br>

If using the job definition template, be sure to replace the "execSystemId" with a specific system (or remove it entirely) and change the "--account" to a specific allocation!
<br><br> 


## Handling input files

Underneath the "jobAttributes" field in the job definition, there is a subfield called "parameterSet". Within "parameterSet" is yet another subfield called "appArgs" where the user can pass in images to be classified using two args: an "--image_file" flag and the image file path.

```
{
    ...,

    "parameterSet": {
        "appArgs": [
            {
                "arg": "--image_file"
            },
            {
                "arg": "'<IMAGE_FILE_PATH>"
            }
        ]
    
    ...
```