
from lib_timeslot import *

class Section():

    def __init__(self,instring):
        data = instring.split(",")
        self.title = data[0]
        self.timeslots = []
        if (len(data)>3):
            self.timeslots.append(TimeSlot(data[1],data[2],data[3]))
        if (len(data)>6):
            self.timeslots.append(TimeSlot(data[4],data[5],data[6]))
        if (len(data)>9):
            self.timeslots.append(TimeSlot(data[7],data[8],data[9]))

    def __str__(self):
        out = self.title+"\n"
        for i in self.timeslots:
            out += i.__str__() + "\n"
        return out

def conflict(a,b):
    for i in a.timeslots:
        for j in b.timeslots:
            if overlap(i,j):
                return True
    return False
        

