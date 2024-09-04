# Details

This folder contains all files needed to build a tar archive that can be used to run a basic shell-script
application using ZIP runtime in Tapis.

## Creating the ZIP archive

To create the tgz app archive file run the following command from this directory.

```
tar -czvf /tmp/shell_script.tgz app/shell_script.sh tapisjob.manifest
```

## Deploying the ZIP archive

Once the ZIP archive has been created it must be placed where the Tapis Jobs service can find it.

The simplest approach is to copy the archive file to the execution host where jobs will be run. Then the Tapis
application definition can point to the file using an absolute path.

The Jobs service can also transfer the archive from another system as part of the staging process.
For more information, please see the Tapis documentation covering
[ZIP runtime support](https://tapis.readthedocs.io/en/latest/technical/jobs.html#zip).

## shell_script.sh

The script checks:

- number of arguments are as expected
- values of arguments are as expected
- environment variables listed in shell_script.env are set
- environment variables listed in shell_script.env are set with expected values
