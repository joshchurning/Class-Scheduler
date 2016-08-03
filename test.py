

from lib_schedule import *
from copy import deepcopy

c1 = Course("ECEN 314","sectiondata/ecen314.txt")
c2 = Course("CSCE 314","sectiondata/csce314.txt")
c3 = Course("CSCE 110","sectiondata/csce110.txt")

s = []

def addCourse(c,schedules):
    if schedules == []:
        for i in range(len(c.sections)):
            schedules.append(Schedule(0))
            schedules[i].add(c.sections[i])
        for i in range(len(schedules)):
            schedules[i]._id = i
        return schedules
    else:
        out = []
        for i in range(len(c.sections)):
            for s in schedules:
                a = deepcopy(s)
                a.add(c.sections[i])
                out.append(a)
        for i in range(len(out)):
            out[i]._id = i
        return out
    return []

s = addCourse(c1,s)
s = addCourse(c2,s)
s = addCourse(c3,s)

for i in s:
    if (i.valid()):
        print (i)
