# Details

This folder contains the Dockerfile used to build the image associated with the img-classify app, along with the files needed by the container to run.

To build the image for local testing, download this folder and navigate to it on the command line, then run the command ```docker build -f Dockerfile -t <NAME_OF_IMAGE> .```
<br><br>


## Dockerfile

The image is built upon TensorFlow's official _tensorflow_ image, which is itself based on Ubuntu Linux version 18.04.
<br><br>


## classify_img.py

Images are passed in through the command line using the _--image_file_ flag. After starting up a container, run the command ```docker run <NAME_OF_IMAGE> --image_file=<PATH_TO_IMAGE_FILE>``` to perform image classification.
<br><br>

For example, the image could be built like so:

```docker build -f Dockerfile -t tylerclemens/img-classify:latest .```
<br><br>

After the image is built, it can be run:

 ```docker run tylerclemens/img-classify:latest --image_file=https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12231410/Labrador-Retriever-On-White-01.jpg``` 
 <br><br>

 This will cause the app to perform image classification on the JPEG found in the S3 bucket at the given URL. The JPEG contains an image of a Labrador Retriever. If the app runs successfully, the following output should be produced:

 ```
Successfully downloaded inception-2015-12-05.tgz 88931400 bytes.
Labrador retriever (score = 0.97471)
golden retriever (score = 0.00324)
kuvasz (score = 0.00099)
bull mastiff (score = 0.00095)
Saint Bernard, St Bernard (score = 0.00067)
 ```
