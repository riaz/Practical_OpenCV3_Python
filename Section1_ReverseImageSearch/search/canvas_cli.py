import numpy as np
import pickle
import cv2
import engine


class Canvas:
    def __init__(self, indexSrc="index.pkl"):
        self.indexSrc = indexSrc

    def get_query_feature(self, query):
        """
         This method will extract all the features from the input image to do do the actual search
        :return:
        """

        image = cv2.imread(query)

        # since we have indexed the RGB histogram for the image corpus, we apply the same methods to the queryImage
        # to retrieve relevent information

        fdesc = engine.RGB3DHistogram()
        features = fdesc.get_rgb_feature(image)

        return features

    def search(self, image):
        """
            This is the api for the search, given an image the methods returns all the relevent images
        :param image: the Image for the query
        :return:  returns the relevent indexed images
        """

        queryFeatures = c.get_query_feature(image)

        index = pickle.loads(open(self.indexSrc,"rb").read())

        searcher = engine.Searcher(index)

        return searcher.search(queryFeatures)


if __name__ == '__main__':

    uri = "../resources/img/0b237ed0-34b5-11e7-8b1c-c1a3f64fdbde_sean-diddy-combs-1404.jpg"

    c = Canvas()
    results = c.search(uri)

    for result in results:
        print(result)


    # next we need to push the results to the front-end
