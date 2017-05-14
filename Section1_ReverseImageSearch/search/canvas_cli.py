import numpy as np
import pickle
import cv2
from engine import RGB3DHistogram, Searcher

"""
    This is the Canvas - Reverse Search Engine Command Line Interface
    Check: canvas_app.py for a Web based interface built using Flask and Jinja.

"""


class Canvas:
    INDEX_SRC = "index.pkl"

    def __init__(self, indexSrc=INDEX_SRC):
        self.indexSrc = indexSrc

    def get_query_feature(self, query):
        """
         This method will extract all the features from the input image to do do the actual search
        :return: feature vector of the image
        """

        image = cv2.imread(query)

        # since we have indexed the RGB histogram for the image corpus, we apply the same methods to the queryImage
        # to retrieve relevent information

        fdesc = RGB3DHistogram()
        features = fdesc.get_rgb_feature(image)

        return features

    def search(self, image):
        """
        This is the api for the search, given an image the methods returns all the relevent images
        :param image: the Image for the query
        :return:  returns the relevant indexed images
        """

        queryFeatures = c.get_query_feature(image)

        index = pickle.loads(open(self.indexSrc, "rb").read())

        searcher = Searcher(index)

        return searcher.search(queryFeatures)


if __name__ == '__main__':
    """
    This is the driver program for the canvas_cli.

    TODO:
        canvas

            Canvas Revese Image Search Command Line Tool v0.1

                     -i   <Path/to/images>   <index.kl>    Indexes the Images
                     -s   <Path/to/Scape/Config>           Scrapes Image
                     <Any valid image uri>                 Path to a image url, could be remote/local
    """

    uri = "../resources/img/0b237ed0-34b5-11e7-8b1c-c1a3f64fdbde_sean-diddy-combs-1404.jpg"

    c = Canvas()
    results = c.search(uri)

    for result in results:
        print(result)
