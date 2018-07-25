#(a)
Q = open("quotes.txt","r")

lines = Q.readlines()
#print lines

def put_in_list(lines):
    i = 0
    store_list = []
    while i < len(lines)-1:
        line =str(lines[i]+ " - " +lines[i+1])
        line = line.replace('\r\n','')
        line=line.replace('\n','')
        store_list.append(line)
        i += 2
    return store_list

a = put_in_list(lines)
print a[0:5]


#(b)
test = ['How we spend our days is, of course, how we spend our lives. - Annie Dillard']
def substract_name(lines):
    for line in lines:
        line = line.split(" - ")
        line = line[:-1]
        line = str(line)[2:-2]
    return line #this is a string

print substract_name(test)

import re

def split_words(line):
    words = []
    line=substract_name(lines) #use the substract_name() to substract the name
    line=line.lower()
    splitted =re.split('\W',line)
    for word in splitted:
        if word!='-' and word !='':
            words.append(word)
    return words #this is a list
b = split_words(substract_name(test)) #b is a list
print b


"""
#(c)
def histogram(s): #putting
    h = dict()
    for c in s:
        h[c] = h.get(c,0) + 1
    return h
c = histogram(b)#this is a dictionary
print c 

#(d)
reverse_dic = {}
for i in lines:
    if key in c[i]:
        reverse_dic[key] = {}
        reverse_dic[key][i]=str(c[i][key])  

reverse_dic['course']
#reverse_dic(line)
"""


