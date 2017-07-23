# Practical_OpenCV3_Python
Projects for Video Series titled "Practical OpenCV3 Image Processing with Python"


[![Download](https://img.shields.io/badge/Build-Passing-brightgreen.svg) ](https://www.github.com/riaz)
[![Download](https://img.shields.io/badge/Python-3.6.1-brightgreen.svg) ](https://www.python.org/downloads)
[![Download](https://img.shields.io/badge/OpenCV-3.2.0_dev-brightgreen.svg) ](https://www.opencv.org/)
[![Download](https://img.shields.io/badge/Numpy-1.12.1-brightgreen.svg) ](https://www.numpy.org)
[![Download](https://img.shields.io/badge/Browser-Chrome-brightgreen.svg) ](www.google.com/chrome)



[1]  DESCRIPTION
------------------------------------------------------------------------------------------
In this volume we will start with applying image processing techniques to various sources and try to built an
intuition for how image processing is an essential step in every large scale computer vision pipeline. We will learn
about what good features are in this Volume and methods to extract them. We will be focus on learning algorithms
that can train over these features in the Volume 2 with applications being applying various filters, performing edge
detection, thresholding, image processing and transformation techniques, working with blobs/contours and image
segmentation techniques. The next volume will deal with application that combine Computer Vision techniques
with machine learning to build more intelligent application like real-time face tracking, head pose estimation ,
gesture tracking using 2D cameras etc.

Understanding Volume 1 is crucial to get started with the Volume 2 , so it is expected to complete the entire
Volume 1 along with the applications based on it.

[2]  CONTENTS
-----------------------------------------------------------------------------------------
Lets now see the contents of each section

## SECTION 1:

In this section, we learn about the various image transformation techniques like Hough Transformation , which are
all based on scoring probabilities of existence of points of interests and converging on the output. We will learn
techniques to stretch, shrink, rotate and warp and image and in later sections we will see how such
transformations don’t effect when trying to do Object Recognition using homography. We next learn about how
Image Histograms are built and how we can use techniques like Histogram Equalization to De-noise a image
effectively and we will further delve into properties of a histogram and how it can be used to build a image search
search of some point of accuracy.

Query Image

![alt text](https://github.com/riaz/Practical_OpenCV3_Python/blob/master/images/query.jpg)


Result

![alt text](https://github.com/riaz/Practical_OpenCV3_Python/blob/master/images/canvas_app.png)




## SECTION 2:

In this section, we learn about the Image Segmentation methods and methods to extract region of interests (ROIs)
or contours on which we can apply any type of image processing pipeline to work with the contours. We also learn
a technique called as template matching which can be used to detect a pattern a an image in a linear way. We also
learn about Background Subtraction, which can be useful to segment away foreground from background and
manipulate them individually. We also learn techniques. We will also learn about how Computer Vision is used in
the field of Medical Imaging and we conclude this section by learning how to train a application to be able to detect
predefined targets and also to be able to detect number plates, even though we would dive into the details of how
the SVM implementation works to detect number plates.
Number Plate Segmentation

![alt text](https://github.com/riaz/Practical_OpenCV3_Python/blob/master/images/number_app_1.png)


Number Plate Extraction

![alt text](https://github.com/riaz/Practical_OpenCV3_Python/blob/master/images/number_app_2.png)


Detection and Prediction

![alt text](https://github.com/riaz/Practical_OpenCV3_Python/blob/master/images/number_app_3.png)



## SECTION 3:

In this section, we learn about what features means in terms of OpenCV and what are the elements of good features
in an image which may include edges, corners etc. We later explore on the most common corner detection
algorithm which is Harris Corner Detection Algorithm. We also learn about SIFT,SURF et al, which are scale and
rotation invariant corner detections and have application in object tracking. We then learn about optical flow
which is the pattern of apparent motion of image objects between two consecutive frames caused by the
movement of object or camera.We will also diving into the application of Deep-Learning for Feature Extraction on a
greater scale of accuracy.

This Section has a very challenging project where we try to write deep-learning algorithms to understand scene’s and label objects and classify them
accordingly. We could further extend this concept by paraphrasing the objects and their actions and coming up
with a beautiful prose that summarises these elements in a image and is converse to a Text-to- Imagery Storytelling
which is very popular nowadays especially in VR world.

![alt text](https://github.com/riaz/Practical_OpenCV3_Python/blob/master/images/scene_app_1.png)


[3] CONTACT US
-------------------------------
Riaz Munshi - riaz.2012@gmail.com   [ Author ]
Sai Ganesh  - saiganeshb@gmail.com  [ Reviewer ]
