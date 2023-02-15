#Greedy matchimg
#The repeat character(* and +) push outward in both directions (greedy) to match the largest string

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

#research() returns true/false depending on whether the string matches the regular expression
#If we actually want the matching strings to be extracted, we use  re.findall()

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

#Non-Greedy matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

#Fine-Tuning string extraction
import re
h = 'From bbaah006@st.ug.edu.gh sun feb 12 06:08:12 2023'
m = re.findall('\S+@\S+', h)
print(m)

data = 'From bbaah006@st.ug.edu.gh sun feb 12 06:08:12 2023'
atpos = data.find('@')
print(atpos)

fgl = data.find(' ', atpos)
print(fgl)
host = data[atpos+1 : fgl]
print(host)
#Double split pattern
line = 'From bbaah006@st.ug.edu.gh sun feb 12 06:08:12 2023'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

#regular expression
import re
h = 'From bbaah006@st.ug.edu.gh sun feb 12 06:08:12 2023'
l = re.findall('@.+? ', h)
print(l)

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confindence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximunm:', max(numlist))
