# text-summarize

This is an application that performs text summarization using hugging face transformer using bart-large-cnn model.
More information can be found [here](https://huggingface.co/facebook/bart-large-cnn)

## Details

The text-summarize application is non-interactive. Once a job using this app has been submitted, the input files provided
in the job submission body are automatically staged and transformation is performed.
The output can be found in the output directory specified in the application definition (*execSystemOutputDir*).

## Using the text-summarize application

Use the _app_definition.json_ file as a reference for creating the text-summarize application. Simply download the file
or copy its contents and [create the app](https://tapis.readthedocs.io/en/latest/technical/apps.html#creating-an-application).

Note that an application id must be unique, so in general it is a good idea to use a naming scheme likely to result
in a unique id. For example, it is common to include a username as part of the id.

To run the application on a specific system instead of a publicly shared one, users can add the *execSystemId*
attribute under the *jobAttributes* section in the app definition:

```
{
    ...,

    "containerImage": "docker://tapis/text-summarize:0.1",
    "jobAttributes": {
        "execSystemId": <SYSTEM_NAME_HERE>,
        "execSystemExecDir": "${JobWorkingDir}/jobs/${JobUUID}",
        
        ...
}
```

If using the job definition template, be sure to replace the *execSystemId* with a specific system
(or remove it entirely), update *appId* with the Id of the application you created and change the "--account" in
*appArgs* to your specific account allocation.


## Handling input files

Underneath the *jobAttributes* field in the job definition, there is a subfield called *parameterSet*.
Within *parameterSet* is yet another subfield called *appArgs* where the user can pass in url to be classifed
using two args: an "--url" flag and the url for text news.

```
{
    ...,

    "parameterSet": {
        "appArgs": [
            {
                "arg": "--url"
            },
            {
                "arg": "'<TEXT_NEWS_URL from https://text.npr.org>"
            }
        ]
    
    ...
```
