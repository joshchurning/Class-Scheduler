

from lib_course import *

class Schedule():

    def __init__(self,_id):
        self.sections = []
        self._id = _id

    def __str__(self):
        out = "Schedule #"+str(self._id)+"\n"
        for i in self.sections:
            out += i.__str__()+"\n"
        return out

    def add(self,s):
        self.sections.append(s)

    def valid(self):
        for a in self.sections:
            for b in self.sections:
                if (a != b and conflict(a,b)):
                    return False
        return True
