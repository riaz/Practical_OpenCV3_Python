import numpy as np
import cv2
import pickle
from os import listdir
from os import sep

"""
    This module contains all the important classes for the Search Engine eg:
        1. RGB3DHistogram  - Generates the feature vector per image
        2. Indexer         - Associates the feature vector with every image and we call this indexing, useful for search
        3. Searcher        - Given a query Image, the Searcher extracts the feature vectors from the query Image,
                             and tries to compute the chi-squared distance between every indexed image to rank them
                             accordingly.
"""


# Here we try to create a 3D RGB histogram with 8 bins each
class RGB3DHistogram:
    """
        Generates the feature vector per image, which is a flattened RGBHistogram of the image
    """

    def __init__(self, bins=[8, 8, 8]):
        # total bins per channel
        self.bins = bins

    def get_rgb_feature(self, image):
        """
        This method generates a 3D histogram  of the image in RGB space
        and then we normalize the histogram to make the image search scale
        invariant

        """

        hist = cv2.calcHist([image], [0, 1, 2],
                            None, self.bins, [0, 256, 0, 256, 0, 256])

        norm = hist.copy()
        cv2.normalize(hist, norm)

        # to make the comparison easy we flatten the histogram
        return norm.flatten()


class Indexer:
    """
    Associates the feature vector with every image and we call this indexing, useful for search
    """

    def __init__(self, src, dst):
        """
        :param src:  Image Data set Source
        :param dst:  Destination of Image index

        """

        self.src = src
        self.dst = dst

        # The index in this case will be a dictionary
        lookup = dict()

        # We create a RGB3DHistorgram object and run get_rgb_feature() on each image,
        # to extract their RGB feature vector for similarity ranking

        fdesc = RGB3DHistogram()

        for img in listdir(src):
            # get the image file name
            fname = img[img.rfind(sep) + 1:]

            print(fname)
            # load the image
            image = cv2.imread(src + sep + img)

            if image == None:
                # Ignores bad image
                continue

            features = fdesc.get_rgb_feature(image)
            lookup[fname] = features

        # now that the lookup is indexed , we pickle it  into dst

        f = open(self.dst, 'wb')
        f.write(pickle.dumps(lookup))
        f.close()


class Searcher:
    """
        Given a query Image, the Searcher extracts the feature vectors from the query Image,
        and tries to compute the chi-squared distance between every indexed image to rank them
        accordingly
    """

    def __init__(self, index):
        """
        Initializes Index
        :param index:  loading the pickled index
        """

        self.index = index

    def chi2_distance(self, histA, histB, eps=1e-10):
        """

        :param histA:  RGB3DHistogram of Image A
        :param histB:  RGB3DHistogram of Image B
        :param eps:
        :return: similarity scores
        """

        dist = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
                             for (a, b) in zip(histA, histB)])

        return dist

    def search(self, query):
        """
        This is the actual search functionality, given the feature vector of a queryImage
        this function returns a list of images in the order of relevancy.

        :param query: The feature vector of the query image
        :return: list of matched images from the index along with their the relevancy scores
        """

        results = dict()

        for (fname, feature) in self.index.items():
            # we try to compute the chi-squared distance between
            # the query and the image feature and store them in results

            dist = self.chi2_distance(feature, query)

            results[fname] = dist

        # ranking the matches based on the distances
        # the lesser the distance the more similar the results are

        results = sorted([(v, k) for (k, v) in results.items()])

        return results[:20]
