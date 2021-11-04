# application-repository
This repository serves to house applications that can be run on TACC hardware via Tapis v3 job submissions.

There is a folder for each app containing the following:
* A README file that discusses how to use the app and any particular changes that may be necessary in the app's definition.

* A JSON file containing the app definition. Use this as a reference to create the app on a Tapis system.

* If applicable, a "docker_build" folder containing everything needed to build the app's Docker container from scratch, such as the Dockerfile and associated input files.
<br><br>

## App types

There are a mix of interactive and non-interactive apps in this repository: 
* Interactive app jobs run continuously on a compute node, allowing the user to interact with the app in a web browser. The job will continue until the user shuts down the session or the job exceeds its maximum runtime.

* Non-interactive apps do not require additional user interaction after job submission. Once the job is completed, the user can view the output in the directory as specified in the app definition ("execSystemOutputDir").
<br><br>


## Adding apps to the repository

When adding an app to the repository, its folder should contain the following:
* A JSON-syntax app definition with all the required fields for running the app.

* A JSON-syntax job definition simulating what an actual submission would look like.

* A README detailing any specific inputs or changes that may be made to the app definition. 

* If applicable, a "docker_build" folder containing the Dockerfile used to build the image and any files that need to be copied into the container.
<br><br>

For more information on required app fields, view [the Tapis documentation](https://tapis-project.github.io/live-docs/?service=Apps#operation/createAppVersion).