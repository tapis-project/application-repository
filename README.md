# application-repository
This repository serves to house applications that can be run on TACC hardware via Tapis v3 job submissions.

Note that in order to run an application via Tapis you will need to register a Tapis system that can execute 
applications using docker or singularity. For more information
please see the *Systems* section in the Tapis [documentation](https://tapis.readthedocs.io/en/latest/).

Another good reference for Tapis information is the live-docs which may be found [here](https://tapis-project.github.io/live-docs/).

In this repository there is a folder for each application containing the following:
* A README file that discusses how to use the application and any particular changes that may be necessary in the definition.

* A JSON file containing the application definition. Use this as a reference to create the application on a Tapis system.

* If applicable, a "docker_build" folder containing everything needed to build a Docker container from scratch, such as the Dockerfile and associated input files.
<br><br>

## Application types

There are a mix of interactive and non-interactive applications in this repository: 
* Interactive jobs run synchronously on a compute node, allowing the user to interact with the application in a web browser. The job will continue until the user shuts down the session or the job exceeds its maximum runtime.

* Non-interactive jobs do not require additional user interaction after job submission. Once the job is completed, the user can view the output in the directory as specified in the application definition ("execSystemOutputDir").
<br><br>


## Adding applications to the repository

When adding an application definition to the repository, its folder should contain the following:
* A JSON-syntax definition with all the required fields for running the application.

* A JSON-syntax job definition simulating what an actual submission would look like.

* A README detailing any specific inputs or changes that may be made to the application definition. 

* If applicable, a "docker_build" folder containing the Dockerfile used to build the image and any files that need to be copied into the container.
<br><br>

For more information on required application fields,
please see the Tapis live-docs reference [here](https://tapis-project.github.io/live-docs/?service=Apps#operation/createAppVersion).


#
Author: Swathi Vallabhajosyula
Description: This program takes inputs to perform visual question answering using a pre-trained hugging face model. 
How to run the program:
    usage: python vision-QA.py [-h] [-o OUTPUT] [-t INPUTTYPE] [-i IMAGEURL] ([-q QUESTION]|[-l QUESTIONLIST])

    Please provide an image url and a question w.r.t. the image

    options:
    -h, --help            show this help message and exit
    -o OUTPUT, --output OUTPUT
                            Path to save the results:
    -t INPUTTYPE, --inputtype INPUTTYPE
                            Mention the type of input (pair=input and question, pairlist = image and list of questions, samplelist = to generate a random sample of image urls for reference and store in output foler as 'Samples.txt'):
    -i IMAGEURL, --imageurl IMAGEURL
                            Enter url to an image:
    -q QUESTION, --question QUESTION
                            Enter a question w.r.t an image
    -l QUESTIONLIST, --questionlist QUESTIONLIST
                            Enter a question list w.r.t an image

Input: 
    OUTPUT: The path to output Dir to store the results (could be an absolute path or a relative path)
    INPUTTYPE: 
        - "pair": to provide ONE question with respect to IMAGEURL
        - "pairlist": to provide a LIST of questions with respect to IMAGEURL
        - "samplelist": to generate a random sample of image urls for reference and store in output foler as 'Samples.txt'
    IMAGEURL: A web acessible image URL.
    QUESTION: A string of text i.e. ONE question w.r.t. to IMAGEURL
    QUESTIONLIST:  A list of strings of text i.e. list of questions w.r.t. to IMAGEURL

Output:
    Either generates response to the questions w.r.t. image in IMAGEURL or generates a sample list of IMAGEURLS to try the application

examples:
* To get sample image URLS (default without any commandline inputs or -t option)
python vision-QA.py
* To get response for one answer per IMAGE URL
python vision-QA.py -t "pair" -i "http://images.cocodataset.org/val2017/000000039769.jpg" -q "How many cats in image?"
* To get resoinse for one answer per IMAGE URL
python vision-QA.py -t "pairlist" -i "http://images.cocodataset.org/val2017/000000039769.jpg" -l "['How many cats in image?', 'What animal is in the image?', 'What device is in the image?', 'How many devices?']"
* To get sample image URLS and stire them in a perticular folder
python vision-QA.py -t "samplelist" -o "Samples"


"""