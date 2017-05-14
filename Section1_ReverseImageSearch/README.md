# Canvas - A Reverse Image Search Engine

[ ![Download](https://img.shields.io/badge/Python3-OK-brightgreen.svg) ](https://python.org)




[1]  DESCRIPTION
------------------------------------------------------------------------------------------
A Reverse Image Search Engine is used to search for similar images with the query being an image.
Today, Reverse Image Search Engine is supported by most of the prominent search engines and 
with the rapid advancements in the fields of Computer Vision, Deep Learning and Cheap Computational Power (Moore's Law) 
we are able to incrementally design new and more modern Reverse Image Search.

Canvas is a very minimalistic Reverse Image Search, but covers all teh essential components on which
a modern search engine is based on. While we plan to improve on the methods on which
we rank images and index images, we are always open to suggestions and please write to us, if you find any bugs or suggestions 
will have a positive effect on our work.

[2]  SETUP
-----------------------------------------------------------------------------------------
This project is written in Python3 and uses the OpenCV3 Libary.

Dependencies:
        1. Python 3
        2. OpenCV 3
        3. OpenCV3 contrib Library 
        4. Numpy

Softwares:
        1. Docker (optional)
        

> Method 1 : Using Local System

Please use build.sh for ( Mac / Linux ) and build.bat for Windows.
Note: This method creates a python virtualenv, to create a independent 
environment that runs all the projects, no additional setup needed.

> Method 2 : Using Docker

Please install docker and find the "Dockerfile" in the main repository for setting up the 
development environment. 
 
If you are new to docker please refer https://docs.docker.com/


[3]  TEST
--------------------------------------------------------------------------------------------

Once the environment is set successfully.

Clone the Project:

>git clone http://github.com/riaz/Section1_ReverseImageSearch

Go to "search" directory

1. setup_cfg.json - You can configure scraping here
2. scraper.py     - Run this to do the scraping
3. index.py       - Run this after scraper.py, to index images
4. canvas_cli.py  - Run this to play with the search engine
5. canvas_app.py  - Web based search engine, upload an image and 
                    find the relevant images ranked accordingly.[ under development ]
                    
Run Instructions:

1. python scraper.py
   
   Press Ctrl + C to Stop Scraping when done.
       
2. python indexer.py
  
   ![alt text](https://github.com/riaz/Practical_OpenCV3_Python/blob/master/Section1_ReverseImageSearch/resources/readme/index.png)

3. python canvas_cli.py

   ![alt text](https://github.com/riaz/Practical_OpenCV3_Python/blob/master/Section1_ReverseImageSearch/resources/readme/canvas_cli.png)



[4] CONTACT US
-------------------------------
<author_email>
<reviewer_email>
