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
    def __init__(self, data):
       self.dict = json.loads(data)


import json
import requests
from pprint import pprint
#main method
if __name__ == '__main__':

    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=d46c2a4c9f2842c5bcf9b1948f61afbe')
    response = requests.get(url)

    data = response.json()
    art = Article(json.loads(data))
    print(art.a)


    #pprint(data)
