from HTMLParser import *
import math

class CourseData():

    def __init__(self,sourcefilename,coursenumber):
        source = HTMLFile(None,sourcefilename)
        self.id = str(coursenumber)
        self.matches = source.matchall('<TD CLASS.+?dddefault.+?</TD>')
        self.info = []
        for i in self.matches:
            self.info.append(getInfoFromTD(i))
        while ('C' in self.info):
            self.info.remove('C')

    def getNumberOfSections(self):
        num = 0
        for i in self.info:
            if (self.id in i):
                num += 1
        return num

    def splitupSections(self):
        per = int(len(self.info)/self.getNumberOfSections())
        matrix = []
        n = -1
        for i in self.info:
            if (self.isCRN(i)):
                matrix.append([])
                n += 1
            matrix[n].append(i)
        return matrix

    def isCRN(self,s):
        if (len(s) == 5):
            try:
                int(s)
                return True
            except:
                pass
        return False

    def outputSectionInfo(self,section):
        out = ""
        out += "["+section[0]+"] "
        out += section[1]+section[2]+"-"+section[3]+" ("+section[5]+")"

        timeindex = []
        for i in range(len(section)):
            if ('m' in section[i]):
                timeindex.append(i)
        for i in timeindex:
            out += ","+section[i-1]+","+section[i].split("-")[0]+","+section[i].split("-")[1]
        return out

    def outputall(self,filename):
        file = open(filename,'w')
        for i in self.splitupSections():
            file.write(self.outputSectionInfo(i)+"\n")
        file.write('\b')
        file.close()
    
