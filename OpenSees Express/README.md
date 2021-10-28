# OpenSees Express

OpenSees Express is a sequential version of the OpenSees application, rather than a parallelized one. See the [OpenSees documentation](https://opensees.berkeley.edu/wiki/index.php/OpenSees_User) for more information. <br></br>


## Details

OpenSees Express is non-interactive. Once a job using this app has been submitted, the input files provided in the app definition (TCL, raw data, etc.) are staged and the main TCL file is executed. The resulting output can be found in the app definition output directory. <br></br>


## Using the OpenSees Express app

Use the _app_definition.json_ file as a reference for creating the OpenSees Express app. Simply download the file or copy its contents and [create the app](https://tapis.readthedocs.io/en/latest/technical/apps.html#creating-an-application).

If the user wants to use a specific system to run the app rather than a shared system, they can add an "execSystemId" key-value pair under the "jobAttributes" object. For example:

```
{
    ...
    "containerImage": "stevemock/docker-opensees:latest",
    "jobAttributes": {
        "execSystemId": <SYSTEM_NAME_HERE>
        "execSystemExecDir": "${JobWorkingDir}/jobs/${JobUUID}",
        ...
}
```
<br>


## Handling input files

Underneath "jobAttributes" in the app definition, there are two important fields: "parameterSet" and "fileInputs".

OpenSees Express requires that at least one TCL file be used as input. In the reference app definition, a TCL file is provided by the user and passed to the job as "input.tcl" (note that the tapis://<SYSTEM_NAME>/ prefix indicates the file exists on a Tapis system). 

If the user has multiple files to pass in, this can be done in the job submission request, as seen below. There are a few points regarding file inputs passed in through the job submission request:
* The main input file *must* follow the same syntax as that provided in the app definition.
* If a job submission request contains a main file different from that provided in the app definition, it will override the app definition file.
* Any additional files added in the job submission request do not have to exist in the app definition already.
<br></br>

```
{
    ...,

    "fileInputs": [
        {
            "sourceUrl": "tapis://<SYSTEM_NAME>/main_tcl_file.tcl",
            "targetPath": "input.tcl",
            "inPlace": false,
            "meta": {
                "name": "TCL_input",
                "required": true
            }
        },
        {
            "sourceUrl": "tapis://<SYSTEM_NAME>/extra_file_1.tcl",
            "targetPath": "extra_file_1.tcl"
        },
        {
            "sourceUrl": "tapis://<SYSTEM_NAME>/extra_file_2.tcl",
            "targetPath": "extra_file_2.tcl"
        },

        ...
    ]
}
```

Read the [Tapis jobs documentation](https://tapis.readthedocs.io/en/latest/technical/jobs.html#fileinputs) for more information on file inputs.