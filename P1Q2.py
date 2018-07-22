# -*- coding: utf-8 -*-
## Change Code
def getKey(item):
    return item[2]

fl_input = []
with open("FloridaVoters.html", "r") as fl:
    for ln in fl:
        if ln.startswith('<td>'):
            ln = ln.rstrip()
            ln = ln.strip('<td>')
            ln = ln.strip('</td>')
            fl_input.append(ln)
fl.close() 
fl_len = len(fl_input)
print 
      
fl_cty = []
fl_rep = []
fl_dem = []

i = 0
fl_len = len(fl_input)
while i < fl_len:
    fl_cty.append(fl_input[i])
    i += 1
    fl_rep.append(int(fl_input[i].replace(",","")))
    i += 1
    fl_dem.append(int(fl_input[i].replace(",","")))
    i += 4

fl_voters = zip(fl_cty,fl_rep,fl_dem)
fl_voters = sorted(fl_voters, key=getKey, reverse=True) 

j=0
while j < (fl_len/6):
    print fl_voters[j][0], fl_voters[j][1], fl_voters[j][2]
    j += 1

