# shell-script

Application that runs a basic shell script on an HPC cluster.

## Details

The basic shell script application is non-interactive. It expects two command line arguments to be passed in and
one environment variable to be set. The output can be found in the output directory specified in the application
definition. If no output directory is defined in the application then the default is
*execSystemOutputDir=${JobWorkingDir}/jobs/${JobUUID}/output*.

For more information on running jobs in Tapis please see the
[documentation](https://tapis.readthedocs.io/en/latest/technical/jobs.html).

## Using the basic shell script application

Use the _app_definition.json_ file as a reference for creating the application. Simply download the file
or copy its contents and [create the application](https://tapis.readthedocs.io/en/latest/technical/apps.html#creating-an-application).

Note that an application id must be unique, so in general it is a good idea to use a naming scheme likely to result
in a unique id. For example, it is common to include a username as part of the id.

To run the application on a specific system instead of a publicly shared one, users can add the *execSystemId*
attribute under the *jobAttributes* section in the app definition:

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
