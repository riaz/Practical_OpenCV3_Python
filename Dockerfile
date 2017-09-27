# This is the docker file to setup: OpenCV3 + Python3  environment
FROM ubuntu:latest
MAINTAINER Riaz Munshi # riaz.2012@gmail.com

RUN apt-get update && apt-get upgrade

#==========OpenCV pre-requisites=========
RUN apt-get -y install cmake git pkg-config
RUN apt-get -y install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
RUN apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libgtk-3-dev libxvidcore-dev libx264-dev
RUN apt-get -y install libatlas-base-dev gfortran

#=========================================


#=============Installing Python=================
RUN apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

#================================================

#========== Installing Python dev================
RUN apt-get -y install python2.7-dev python3.5-dev 
#================================================


#========== Installing Dlib Prerequisite==========
RUN apt-get -y install libboost-all-dev
#=================================================

# Additional step needed to avoid the permission denied error
RUN rm -rf ~/.cache/pip/
RUN pip install numpy


# Building and Installing OpenCV3 with Python 3
# Make sure that version of opencv and opencv_contrib are the same
# Eg: 3.1.0 in our case

# Downloading OpenCV3
CMD ["cd", "~"]
RUN git clone https://github.com/Itseez/opencv.git && cd opencv && git checkout 3.1.0

# Downloading OpenCV3_contrib
CMD ["cd" ,"~"]
RUN git clone https://github.com/Itseez/opencv_contrib.git && cd opencv_contrib && git checkout 3.1.0 

#Installing OpenCV3
CMD ["cd", "~"]
##CMD ["mkdir", "build"]
##CMD ["cd", "build"]
RUN cd opencv && mkdir build && cd build && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
#	-D INSTALL_C_EXAMPLES=ON \
#	-D INSTALL_PYTHON_EXAMPLES=ON \
#       -D BUILD_PYTHON_SUPPORT=ON \
	-D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON .. && make -j4 && make install && ldconfig

#RUN ln -s /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.so

# Installing Flask
RUN pip install Flask

# Installing Tensorflow
RUN pip3 install tensorflow 

# Installing Ipython
RUN apt-get -y install python-dev ipython ipython-notebook

# Installing Jupyter
RUN pip3 install jupyter 

RUN python -m pip install ipykernel

RUN python -m ipykernel install --user


# Installing Dlib
RUN pip3 install scipy
RUN pip3 install scikit-image
RUN pip3 install dlib

COPY jupyter_notebook_config.py /root/.jupyter/

# setting my tmux - terminal multiplexer
RUN apt-get -y install tmux

# Setting up the work directory
RUN mkdir /src

WORKDIR "/src"
