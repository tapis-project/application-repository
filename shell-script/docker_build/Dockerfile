# image: tapis/basic-shell-script-app:0.1
##########################################################################
# Dockerfile for Tapis V3 basic shell script application
#
# Setup for running a bash script using the ubuntu base image.
# Could probably use a smaller base image if image size becomes a concern.
##########################################################################
FROM ubuntu:22.04

# Add the script into the container
ADD shell_script.sh /shell_script.sh

# Note: Using ENTRYPOINT makes this run immediately in non-interactive mode.
ENTRYPOINT ["/shell_script.sh"]
