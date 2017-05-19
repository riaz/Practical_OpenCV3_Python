import cv2
import pickle
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

        queryFeatures = self.get_query_feature(image)

        index = pickle.loads(open(self.indexSrc, "rb").read())

        searcher = Searcher(index)

        return searcher.search(queryFeatures)

