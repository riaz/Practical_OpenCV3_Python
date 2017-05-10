import engine

"""
    This is a client program that is used to index the images that the scraper extracts to the directory that you set in setup_cfg.json
"""

if __name__ == '__main__':

    image_src = "../resources/img"
    index_dst = "index.pkl"

    #generate Index
    engine.Indexer(image_src, index_dst)
