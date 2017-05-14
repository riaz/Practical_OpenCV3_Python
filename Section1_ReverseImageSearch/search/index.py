from engine import Indexer
from os import sep

"""
    This is a client program that is used to index the images that the scraper extracts to the directory that you set in setup_cfg.json
"""

IMAGE_SRC = ".." + sep + "resources"

if __name__ == '__main__':
    """
        Canvas RGB3D Histogram Based Feature Indexer Driver.
        The indexer needs two parameters
            1.The directory of the images to index
            2.The name of the file where the index will be stored, defaults to index.pkl
    """

    CON_MSG = "Indexing Images.......This process may take some time."
    image_src = IMAGE_SRC + sep + "img"
    index_dst = "index.pkl"

    print(CON_MSG)
    # generate Index
    Indexer(image_src, index_dst)
