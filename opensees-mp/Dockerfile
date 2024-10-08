######################################################
#
# OpenSees image
# Tag: tapis/opensees-mp:3.4.0
#
# Attribution: This image was originally created by Ian Wang; see his original repository
# here: https://github.com/wangyinz/opensees-container
#
# This is a vanilla installation of OpenSeesMP 3.4.0 on Ubuntu 20.04 compiled with Intel MPI
# You can run the app demo by running the container with no
# arguments.
#
# docker run -it --rm tapis/opensees-mp:3.4.0
#
# To run your own input, mount your data to the /data volume and
# specify the traditional invocation command
#
# mpirun docker run -it --rm -v `pwd`:/data tapis/opensees-mp:3.4.0 /bin/sh -c 'OpenSeesMP < /data/myinput.tcl'
#
# The data will appear in your current directory at the end of the run.
#
# Note that you should ether use mvapich2 or unset FI_PROVIDER and FI_PROVIDER_PATH in impi
# (though in some basic testing, mvapich2 performed as well or better)
# 
######################################################

# decend from base MPI image developed for the SCOPED project
FROM ghcr.io/seisscoped/container-base:ubuntu20.04_mpi
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN echo deb https://apt.repos.intel.com/mkl all main > /etc/apt/sources.list.d/intel-mkl.list && \
    apt-get -y update && \
    apt-get -y install intel-mkl-64bit-2020.1-102 && \
    apt-get -y install git vim-tiny make cmake tcl8.6 tcl8.6-dev gcc g++ gfortran python3-dev && \
    docker-clean && \
    sed -i '3 i . /opt/intel/compilers_and_libraries/linux/mkl/bin/mklvars.sh intel64 mod' /entry.sh && \
    useradd --create-home ubuntu 
RUN cd /home/ubuntu && \
    mkdir bin lib && \
    wget http://graal.ens-lyon.fr/MUMPS/MUMPS_5.2.1.tar.gz && \
    tar -xf MUMPS_5.2.1.tar.gz && rm MUMPS_5.2.1.tar.gz && \
    cd MUMPS_5.2.1 && \
    cp Make.inc/Makefile.INTEL.PAR Makefile.inc && \
    sed -i 's/mpiicc/mpicc/g' Makefile.inc && \
    sed -i 's/mpiifort/mpif90/g' Makefile.inc && \
    sed -i 's/OPTF    =.*/OPTF    = -O3 -fopenmp/g' Makefile.inc && \
    sed -i 's/OPTL    =.*/OPTL    = -O3 -fopenmp/g' Makefile.inc && \
    sed -i 's/OPTC    =.*/OPTC    = -O3 -fopenmp/g' Makefile.inc && \
    make -j mumps_lib && mkdir ../mumps && mv lib ../mumps/lib && mv include ../mumps/include && \
    cd .. && rm -rf MUMPS_5.2.1
ADD makes/Makefile.def /home/ubuntu/Makefile.def
RUN cd /home/ubuntu && source /entry.sh && git clone https://github.com/OpenSees/OpenSees.git && \
    cd OpenSees && \
    git checkout v3.4.0 && cp ../Makefile.def ./ && \
    PROGRAMMING_MODE=PARALLEL_INTERPRETERS make -j 28 && \
    mv EXAMPLES/SmallMP ../SmallMP && cd .. && rm -rf OpenSees Makefile.def
COPY inputs /data
RUN mv /home/ubuntu/SmallMP /data/SmallMP && rmdir /home/scoped
RUN chown -R ubuntu:ubuntu /home/ubuntu /data
ENV HOME=/home/ubuntu \
    NB_USER=
USER ubuntu
WORKDIR /data
ENV PATH $PATH:/home/ubuntu/bin
VOLUME ["/data"]
CMD [ "/bin/sh", "-c", "OpenSeesMP" ]