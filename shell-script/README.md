# shell-script

Application examples that run a basic shell script on an HPC cluster using an application *jobType* of **BATCH** or
on a single host using a *jobType* of **FORK**. This directory contains examples and instructions for five
different combinations of application *jobType* and *runtime*. Each example is in a separate subdirectory.
The combinations are:

- Subdirectory fork_docker: FORK jobType and DOCKER runtime
- Subdirectory fork_singularity: FORK jobType and SINGULARITY runtime
- Subdirectory fork_zip: FORK jobType and ZIP runtime
- Subdirectory batch_singularity: BATCH jobType and SINGULARITY runtime
- Subdirectory batch_zip: BATCH jobType and ZIP runtime.

Each subdirectory contains files that can be used as starting templates for an application and a job
submission request. Note that an application id must be unique. When not creating an application
for general use, it is a good idea to use a naming scheme likely to result in a unique id. For example, as indicated in
the provided application json files, a username may be included as part of the id.

The subdirectory **docker_build** contains instructions for building the docker image used in the examples.
The subdirectory **zip_build** contains instructions for building the zip archive used in the examples.

The file **sys_exec.json** shows a Tapis system definition that can be used as a starting template for creating
an execution system in Tapis. Note that this template is based on a test VM used by the TACC Tapis development
team. It is set up to support running both FORK and BATCH type jobs using a runtime of DOCKER, SINGULARITY or ZIP.
In particular, note that the queues (aka partitions) defined for the system must match the HPC queues on the
HPC cluster. Remember to register credentials for the Tapis system after you create it.

## Details

The basic shell script application is non-interactive. It expects two command line arguments to be passed in and
one environment variable to be set. The output can be found in the output directory specified in the application
definition. If no output directory is defined in the application then the default is
*execSystemOutputDir=${JobWorkingDir}/jobs/${JobUUID}/output*.



For more information on running jobs in Tapis please see the
[documentation](https://tapis.readthedocs.io/en/latest/technical/jobs.html).

## Using the basic shell script application

Use the desired _app_definition.json_ file from one of the subdirectories as a reference for creating the application.
Simply download the file or copy its contents and [create the application](https://tapis.readthedocs.io/en/latest/technical/apps.html#creating-an-application).

Note that an application id must be unique, so in general it is a good idea to use a naming scheme likely to result
in a unique id. For example, it is common to include a username as part of the id.

To run the application on a specific system instead of a publicly shared one, users can add the *execSystemId*
attribute under the *jobAttributes* section in the app definition. For example:

```
{
    ...,

    "containerImage": "docker://tapis/basic-shell-script:0.1",
    "jobAttributes": {
        "execSystemId": <SYSTEM_NAME_HERE>,
        "execSystemExecDir": "${JobWorkingDir}/jobs/${JobUUID}",
        
        ...
}
```

If using the job definition template, be sure to replace the *execSystemId* with a specific system
(or remove it entirely), update *appId* with the Id of the application you created and change the "-A" in
*schedulerOptions* to your specific account allocation.


## Application input arguments and environment variables

Underneath the *jobAttributes* field in the job definition, there is a subfield called *parameterSet*.
Within *parameterSet* is yet another subfield called *appArgs* where the user must pass in the arguments expected
by the shell script. Under *parameterSet* there is also the subfield called *envVariables* where the environment
variable expected by the shell script must be set.

```
{
    ...,

    "parameterSet": {
      "appArgs": [
      {
        "arg": "arg1",
        "name": "appArg1Name",
        "inputMode": "FIXED"
      },
      {
        "arg": "arg2",
        "name": "appArg2Name",
        "inputMode": "FIXED"
      }
      ],
      "envVariables": [
      {
        "key": "MY_ENV1",
        "value": "env_1_value"
      }
      ]
    },
    
    ...
```
