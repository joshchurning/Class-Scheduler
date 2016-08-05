
## Automatically gets course info for tamu class sections

from HTMLParser import *

class CourseInfo():

    def __init__(self, inlist):
        self.department = inlist[0]
        self.number = inlist[1]
        self.crn = inlist[2]
        self.title = ""
        self.prof = ""
        self.section = "000"
        self.capacity = 0
        self.actual = 0
        self.remaining = 0
        
        self.url1 = ""
        self.url1 += "https://compass-ssb.tamu.edu/pls/PROD/bwykschd.p_disp_listcrse?term_in=201631&subj_in="+str(self.department)
        self.url1 += "&crse_in="+str(self.number)
        self.url1 += "&crn_in="+str(self.crn)
        self.url1 += "&deviceType=C"

        self.url2 = ""
        self.url2 += "https://compass-ssb.tamu.edu/pls/PROD/bwykschd.p_disp_detail_sched?term_in=201631&crn_in="+str(self.crn)

    def run(self):
        out = []
        out.append(self.crn)
        out.append(self.department)
        out.append(self.number)

        parser1 = HTMLFile(self.url1)
        results1 = parser1.matchall("<TD CLASS.+?</TD>")
        self.times = []
        for i in range(int(len(results1)/7)):
            self.times.append([])
            self.times[i].append(striptags(results1[i*7+0]))
            self.times[i].append(striptags(results1[i*7+2]))
            self.times[i].append(striptags(results1[i*7+1]))
        self.prof = striptags(results1[6])[:-2]

        parser2 = HTMLFile(self.url2)
        results2 = striptags(parser2.matchall("<TH.+?<BR><BR>")[0]).split(" - ")
        self.title = results2[0]
        self.section = results2[3]
        results3 = parser2.matchall("<TD CLASS.+?</TD>")
        self.capacity = striptags(results3[1])
        self.actual = striptags(results3[2])
        self.remaining = striptags(results3[3])
        
    def __str__(self):
        out = self.title +"\n"
        out += str(self.department)+" "+str(self.number)+" "+str(self.section)+" "+str(self.crn)+"\n"
        for t in self.times:
            for i in t:
                out += str(i) + " "
            out += "\n"
        out += self.prof + "\n"
        out += str(self.capacity)+" "+str(self.actual)+" "+str(self.remaining)+"\n"
        return out       

def striptags(s):
    s = s.split(">")[1]
    s = s.split("<")[0]
    return s




###
### TESTING SECTION
###

### FORMAT [department,number,crn]


tests = [["HIST","280","19180"],
         ["CSCE","411","22892"],
         ["CSCE","315","13020"],
         ["SCMT","400","21545"]]

for i in range(len(tests)):
    print ("\nTEST #"+str(i+1)+"\n")
    test = CourseInfo(tests[i])
    test.run()
    print (test)

