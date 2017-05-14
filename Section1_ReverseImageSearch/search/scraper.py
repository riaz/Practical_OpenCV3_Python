import sys
import utils
import logging
import json
import requests
from os import sep
from bs4 import BeautifulSoup

"""
 This is a driver function as well as the Scraper module for Canvas Image Search Engine.
"""


class Scraper:
    """
    1. This is the Image Scraper and used to source Images from the Web.
    2. The Scraper is initialized from the setup_cfg.json file, you can edit the properties in this file to customize
    the scraping.
    3. To get started with the scraper , setup image sources eg: yahoo.com/google.com and topics of interest in
    setup_cfg.json.
    4. Once done, just run the scraper.py to do the scraping and all the images get stored into the "dst" location that you set in the config.
    5. The scraper is designed to run incrementally and can e stopped by Keyboard Interrupt.

    Note: Design and Implementation of the Scraper is not in the scope of the Course. You can index images
    from your local file system without having to run the Scraper.

    Hints: You can make a multi-threaded Scraper to be able to scrape for faster, sharing a single urlList (resource)
    using a semaphore.
    """

    DEFAULT_ENGINE = "yahoo.com"
    DEFAULT_TOPIC = "nature"
    DEFAULT_DST = ".." + sep + "resources" + sep + "img"  # default destination for images
    IMAGE_HOME = ".." + sep + "resources"

    def __init__(self, filename):
        """
        Initializes the Scraper

        :param filename: The path to setup_cfg.json file to initialize the scraper
        """
        # Checking for python3 interpreter
        if not utils.is_python3():
            print("Please run using Python 3")
            sys.exit(0)

        # a set of unique urls from where we scrape images
        self.uniqUrls = set()

        # initializing scraper from config file
        self.kwds, self.engs, self.dst, self.urlList = self.load_config(filename)

        logging.debug("Scraper Successfully Initialized")

    def prepare_seed_url(self, engs, kwds):
        """
        Prepares the Seed Url from the list of engines and keywords

        :param engs: list of search engines
        :param kwds: list of topics of interests
        :return:  prepared list of seed urls based on engs and kwds
        """
        res = list()

        # Please make sure that the urlMap is consistent with the engines in config, 1-1 mapping
        urlMap = {
            "yahoo.com": "https://images.search.yahoo.com/search/images?p=",
            "google.com": "https://www.google.com/search?tbm=isch&q=",
            "bing.com": "http://www.bing.com/images/search?q="
        }

        try:
            for i in engs:
                for j in kwds:
                    url = urlMap[i] + str(j)
                    if not url in self.uniqUrls:
                        self.uniqUrls.add(url)
                        res.append(url)

        except Exception:
            logging.debug("Failed populating for a entry.")

        if len(res) == 0:
            # We try to extract images from yahoo.com homepage, if its empty
            res.append(self.DEFAULT_ENGINE)

        return res

    def load_config(self, filename):
        """
        Loads properties from the setup_cfg.json file, any new key added to this file must be handled appropriately.
        :param filename:
        :return:
        """
        try:
            with open(filename) as json_data:
                conf = json.load(json_data)
                kwds = conf["keywords"] if "keywords" in conf else self.DEFAULT_TOPIC
                engs = conf["engines"] if "engines" in conf else self.DEFAULT_ENGINE
                dst = self.IMAGE_HOME + conf["dst"] if "dst" in conf else self.DEFAULT_DST

                urlList = self.prepare_seed_url(engs,
                                                kwds)
            return kwds, engs, dst, urlList

        except Exception as e:
            print(e.msg)
            print("Error! Loading Configuration. Scraper will exit.")
            sys.exit(0)

    def run(self):
        """
        This will trigger the actual scrapping process after all the pro-processing is done.
        This will run almost indefinitely, press "Ctrl + C" or KeyboardInterrupt to halt the Scraping process.

        :return: None
        """
        try:
            for url in self.urlList:
                try:
                    req = requests.get(url)
                except Exception as e:
                    # possible 404 , ignore url and continue
                    continue

                soup = BeautifulSoup(req.content, "html.parser")

                for link in soup.find_all('a'):
                    # checking for hyperlinks
                    new_url = link.get('href')

                    if new_url not in self.uniqUrls:
                        self.uniqUrls.add(new_url)
                        self.urlList.append(new_url)

                for tag in soup.findAll('img'):

                    link = tag.get('src')  # get the link

                    # Check if the tag is in expect format
                    del tag['src']

                    if link is not None:
                        elem = '.'
                        idx = link.rindex(elem) if elem in link else -1

                        if idx is -1: break

                        ext = link[link.rindex('.') + 1:]

                        if ext == 'jpg' or ext == 'png' or ext == 'gif':
                            # extracting the filename
                            filename = link.strip(sep).rsplit(sep, 1)[-1]

                            try:
                                # use requests to get the content of the images
                                image = requests.get(link).content
                            except:
                                # possible 404 , ignore url and continue
                                continue

                            with open(self.dst + filename, 'wb') as f:
                                # write the image into a file
                                f.write(image)

                # removing url from self.urlList
                self.urlList.remove(url)

        except KeyboardInterrupt:
            # When user presses Ctrl + C, to voluntarily stop the scraping process.
            print("User Stopped Scraping")
            sys.exit(0)


if __name__ == '__main__':
    """
    Canvas Image Scraper Driver Program
    """

    CON_MSG = "Scraping Images.......This process may take some time."

    conf = "setup_cfg.json"

    print(CON_MSG)
    scraper = Scraper(conf)
    scraper.run()
