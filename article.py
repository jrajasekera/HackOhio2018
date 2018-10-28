
import requests
class Article:

    class Source:
        #the constructor for the Source class
        def __init__(self, id, name):
            self.id = null
            self.name = ""

        #method that sets the value of ID
        def setid(self,id):
            self.id = id

        #method that sets the value of name
        def setname(self,name):
            self.name = name

        #method that gets the value of ID
        def getid(self):
            return self.id

        #method that gets the value of Name
        def getname(self):
            return self.name




    #the constructor for the Article class initializes all of attributes
    #source represents the source object
    #author represents
    def __init__(self):
        self.author = ""
        self.content = ""
        self.description = ""
        self.publishedAt = ""
        self.source = ""
        self.title = ""
        self.url = ""
        self.urlToImage = ""

    def getauthor(self):
        return self.author

    def getcontent(self):
        return self.content

    def getdescription(self):
        return self.description

    def getpublishedat(self):
        return self.publishedAt

    def getsource(self):
        return self.source
    def gettitle(self):
        return self.title
    def geturl(self):
        return self.url
    def geturltoimage(self):
        return self.urlToImage

    def setauthor(self, a):
        self.author = a
    def setcontent(self, c):
        self.content = c
    def setdescription(self,d):
        self.description = d
    def setpublishedat(self, p):
        self.publishedAt = p
    def setsource(self, s):
        self.source = s
    def settitle(self, t):
        self.title = t
    def seturl(self, u):
        self.url = u
    def seturltoimage(self, ui):
        self.urlToImage = ui

import json
import requests
from pprint import pprint
#main method
if __name__ == '__main__':

    #get JSON object using News API
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=d46c2a4c9f2842c5bcf9b1948f61afbe')
    response = requests.get(url)
    #convert Response object into a dictionary
    json_data = json.loads(response.text)
    #list that will hold the articles in order
    articlesList = []

    #using a for each loop to get the attributes of each article
    #keep the order of the articles
    for key,articles in json_data.items():
        #if the key is "Articles", create another for each loop
        # that iterates through the each article
        # within the loop, get each attribute and create an Article
        # object by sending them in as parameters
        # store each article object in a sequence
        if key == 'articles':
          for individualarticle in articles:
              resultArticle = Article()
              resultArticle.setauthor(individualarticle['author'])
              print(resultArticle.author())
              resultArticle.setcontent(individualarticle['content'])
              resultArticle.setdescription(individualarticle['description'])
              resultArticle.setpublishedat(individualarticle['publishedAt'])
              resultArticle.setsource(individualarticle['source'])
              resultArticle.settitle(individualarticle['title'])
              resultArticle.seturl(individualarticle['url'])
              resultArticle.setdescription(individualarticle['urlToImage'])
              articlesList.append(resultArticle)


