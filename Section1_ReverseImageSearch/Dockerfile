# This is the docker file to setup: OpenCV3 + Python3  environment
FROM ubuntu
MAINTAINER Riaz Munshi # riaz.2012@gmail.com

# Upgrading and Updating to the latest version of ubuntu
RUN apt-get update
RUN apt-get upgrade

# Installing the pre-requisites
RUN apt-get install build-essential
RUN apt-get install cmake git pkg-config
RUN apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
RUN apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libgtk2.0-dev
RUN apt-get install libatlas-base-dev gfortran

# Setting up python 3 and virtualenv
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip3 install virtualenv virtualenvwrapper

# Setting up vitual env settings
RUN export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
RUN export WORKON_HOME=$HOME/.virtualenvs
RUN source /usr/local/bin/virtualenvwrapper.sh

# Creating a python3 virtual environment named cv
RUN mkvirtualenv cv
RUN apt-get install python3.4

# Installing pip
RUN pip install numpy

# Additional step needed to avoid the permission denied error
RUN rm -rf ~/.cache/pip/
RUN pip install numpy


# Building and Installing OpenCV3 with Python 3
# Make sure that version of opencv and opencv_contrib are the same
# Eg: 3.0.0 in our case

# Downloading OpenCV3
CMD ["cd", "~"]
RUN git clone https://github.com/Itseez/opencv.git
CMD ["cd", "opencv"]
RUN git checkout 3.0.0

# Downloading OpenCV3_contrib
CMD ["cd" ,"~"]
RUN git clone https://github.com/Itseez/opencv_contrib.git
CMD ["cd" ,"opencv_contrib"]
RUN git checkout 3.0.0

#Installing OpenCV3
CMD ["cd", "~/opencv"]
CMD ["mkdir", "build"]
CMD ["cd", "build"]
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..

RUN make -j4
RUN make install
RUN ldconfig

CMD ["cd", "~/.virtualenvs/cv/lib/python3.4/site-packages/"]
RUN ln -s /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.so


#Installing Flask
RUN pip install Flask


# Working on virtualenv "cv"
workon cv


