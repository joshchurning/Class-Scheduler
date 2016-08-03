

from lib_section import *

class Course():

    def __init__(self,name,filename):
        self.name = name
        file = open(filename)
        data = file.read()
        file.close()
        data = data.split('\n')[:-1]
        self.sections = []
        for i in data:
            self.sections.append(Section(i))

    def __str__(self):
        out = self.name + "\n\n"
        for i in self.sections:
            out += i.__str__() + "\n"
        return out
