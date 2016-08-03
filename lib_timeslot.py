
##  Ryan Schreiber

##
##  TimeSlot class that supports a time range on a given set of days of the
##  week. Also supports a function that compares whether the two times conflict
##  with each other by overlaping.
##

class TimeSlot():

    beg,end = 0,0
    strbeg,strend = "",""
    days = []

    # Inputs:
    #   ds -> String for the days of the week (eq. "MW" or "TR")
    #   b  -> Beginning time as a string
    #   e  -> Ending time as a string
    def __init__(self,ds,b,e):
        self.days = []
        for c in ds:
            self.days.append(c)
        self.beg,self.strbeg = self.parsetime(b)
        self.end,self.strend = self.parsetime(e)

    # turns a raw string time into a number and a formated string
    def parsetime(self,stime):
        ntime = stime.split(' ')[0]
        ntime = ntime.split('a')[0]
        ntime = ntime.split('p')[0]
        arr = ntime.split(':')
        h = float(arr[0])
        m = float(arr[1])/60
        if (("p" in stime) and (h<12)):
            h += 12
        if (("a" in stime) and (h==12)):
            h = 0
        if (h>12):
            out = str(int(h-12))+":"+"{:>02d}".format(int(m*60))
        else:
            out = str(int(h))+":"+"{:>02d}".format(int(m*60))
        if (h>11):
            out += " pm"
        else:
            out += " am"
        return h+m,out

    # Returns the parameters to the object in order to make a duplicate
    def parameters(self):
        out1 = ""
        for c in self.days:
            out1 += c
        return out1,self.strbeg,self.strend

    # Simple toString method
    def __str__(self):
        a,b,c = self.parameters()
        out = ""
        out += a
        out += " from " + b
        out += " to " + c
        return out

    # Returns the length of the timeslot
    def length(self):
        return self.end-self.beg

    # Tests whether given TimeSlot is a subset of this TimeSlot
    def contains(self,other):
        for a in self.days:
            for b in other.days:
                if (a == b and self.beg <= other.beg and other.end <= self.end):
                    return True
        return False

# Overlapping function to determine if there is a conflict between to timeslots
def overlap(a,b):
    for da in a.days:
        for db in b.days:
            if (da == db):
                if (a.beg <= b.beg and b.beg <= a.end or
                    a.beg <= b.end and b.end <= a.end or
                    b.beg <= a.beg and a.beg <= b.end or
                    b.beg <= a.end and a.end <= b.end):
                    return True
    return False
                

##
## End of program
##
