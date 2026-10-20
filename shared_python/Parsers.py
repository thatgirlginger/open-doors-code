from bs4 import BeautifulSoup as bs 

from shared_python.Requests import RequestHandler

class LinkParser:
    def __init__(self, filetext):
        self.filetext = filetext
    def extract_links(self):
        soup = bs(self.filetext, 'html.parser')
        hrefs = 'soup.find_all('a')' #list comp here
