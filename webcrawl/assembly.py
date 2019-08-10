from bs4 import BeautifulSoup
import urllib.request as url

class AssemblyCrawler:
    def __init__(self, param):
        self.param = param

    def scrap(self):

        soup =BeautifulSoup(urlopen(self.url), 'html.parser')