import utils
import sys
import logging
import json


class Scraper():
    def __init__(self,filename):
        if not utils.is_python3():
            print("Please run using Python 3")
            sys.exit(0)
        else:
            try:
                import urllib
                import requests
                from bs4 import BeautifulSoup

            except ImportError as e:
                print(e.msg)
                sys.exit(0)

        self.uniqUrls = set()
        self.loadConfig(filename)

        logging.debug("Scraper Successfully Initialized")

    def prepareSeedUrl(self,engs,kwds):

        res = list()

        # Please make sure that the urlMap is consistent with the engines in config, 1-1 mapping
        urlMap = {
            "yahoo.com"  : "https://images.search.yahoo.com/search/images?p=",
            "google.com" : "https://www.google.com/search?tbm=isch&q=",
            "bing.com"   : "http://www.bing.com/images/search?q="
        }

        try:
            for i in engs:
                for j in kwds:
                    url = urlMap[i] + str(kwds)
                    if not url in self.uniqUrls:
                        self.uniqUrls.add(url)
                        res.append(url)

        except Exception:
            logging.debug("Failed populating for a entry.")
            #continue

        if res.empty():
            res.append("http://yahoo.com") # We try to extract images from yahoo.com homepage, if its empty

        return res


    def loadConfig(self,filename):
        try:
            with open(filename) as json_data:
                conf = json.load(json_data)
                self.id   = conf["id"] if "id" in conf else "101"
                self.kwds = conf["keywords"] if "keywords" in conf else ["snakes"]
                self.engs = conf["engines"] if "engines" in conf else ["yahoo.com"]

                self.urlList = self.prepareSeedUrl(self.engs,
                                                   self.kwds)

        except Exception as e:
            print(e.msg)
            print("Error! Loading Configuration. Scraper will exit.")
            sys.exit(0)



    def run(self):
        try:
            for url in self.urlList:
                req = requests.get(url)
                soup = BeautifulSoup(req.txt)

                for link in soup.find_all('a'): #hyperlinks
                    new_url  = link.get('href')

                    if not new_url in self.uniqUrls:
                        self.uniqUrls.add(new_url)
                        self.urlList.append(new_url)

                #removing url from self.urlList
                self.urlList.remove(url)
        except KeyboardInterrupt:
            print("User Stopped Scraping")
            sys.exit(0)

if __name__ == '__main__':
    cfile = "setup_cfg.json"

    scraper = Scraper(cfile)
    scraper.run()
