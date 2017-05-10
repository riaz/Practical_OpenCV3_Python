import sys
import utils
import logging
import json
import importlib
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, filename):
        if not utils.is_python3():  # Utils.is_python3():
            print("Please run using Python 3")
            sys.exit(0)
        else:
            try:
                importlib.import_module("requests")
                from bs4 import BeautifulSoup

            except ImportError as e:
                print(e.msg)
                sys.exit(0)

        self.uniqUrls = set()
        self.load_config(filename)

        logging.debug("Scraper Successfully Initialized")

    def prepare_seed_url(self, engs, kwds):

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
            res.append("http://yahoo.com")  # We try to extract images from yahoo.com homepage, if its empty

        return res

    def load_config(self, filename):
        try:
            with open(filename) as json_data:
                conf = json.load(json_data)
                self.id = conf["id"] if "id" in conf else "101"
                self.kwds = conf["keywords"] if "keywords" in conf else ["snakes"]
                self.engs = conf["engines"] if "engines" in conf else ["yahoo.com"]
                self.dst = "../resources/" + conf["dst"] if "dst" in conf else "img"
                self.urlList = self.prepare_seed_url(self.engs,
                                                   self.kwds)

        except Exception as e:
            print(e.msg)
            print("Error! Loading Configuration. Scraper will exit.")
            sys.exit(0)

    def run(self):
        try:
            for url in self.urlList:
                # print(url)

                try:
                    req = requests.get(url)
                except Exception as e:

                    continue

                soup = BeautifulSoup(req.content, "html.parser")

                for link in soup.find_all('a'):  # hyperlinks
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
                            filename = link.strip('/').rsplit('/', 1)[-1]  # to get the correct file name

                            try:
                                image = requests.get(link).content  # use requests to get the content of the images
                            except:
                                continue

                            with open(self.dst + filename, 'wb') as f:
                                f.write(image)  # write the image into a file

                # removing url from self.urlList
                self.urlList.remove(url)

        except KeyboardInterrupt:
            print("User Stopped Scraping")
            sys.exit(0)


if __name__ == '__main__':
    cfile = "setup_cfg.json"

    scraper = Scraper(cfile)
    scraper.run()
