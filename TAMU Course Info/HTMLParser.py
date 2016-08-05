
import re
from urllib.request import *


class HTMLFile():

    url = ""
    htmlfile = ""
    html = ""

    components = []
    
    def __init__(self,url=None,filename=None):
        if (url != None):
            self.url = url
            self.htmlfile = urlopen(url)
            self.html = self.htmlfile.read().decode()
        else:
            self.url = None
            self.htmlfile = open(filename)
            self.html = self.htmlfile.read()

    def matchall(self,pattern):
        regex = re.compile(pattern)
        matches = re.findall(regex,self.html)
        return matches

    def outputSource(self,filename):
        file = open(filename,'w')
        file.write(self.html)
        file.close()

def getInfoFromTD(resection):
    out = []
    for i in resection.split("<"):
        for j in i.split(">"):
            out.append(j)
    return out[int(len(out)/2)]
