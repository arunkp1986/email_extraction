import csv
import re
import sys
#from validate_email import validate_email

"""
Usage:
$ email_extration.py data.csv 
"""

data_file = sys.argv[1]


with open(data_file,'r') as csvfile:
	data = csv.reader(csvfile,delimiter=',')
	l1 = []
	l2 = []
	for row in data:
		for i in row:
			if ('@' in i) or ('[at]' in i) or ('(at)' in i):
				o = i.replace(' (dot) ','.')
				p = o.replace('(@)','@')
				q = p.replace('(.)','.')
				r = q.replace(':',' ')
				s = r.replace('[dot]','.')
				t = s.replace('(dot)','.')
				#s = r.replace(',','')
				#t = s.replace(' ','') 
				l1.append(t)
			else:
				l2.append(i)

with open('final.csv','w') as csvfile:
	fieldnames = ['email']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	for i in l1:
		res = re.search("([^@|\s]+@[^@]+\.[^@|\s]+)",i,re.I)
		if res:
			m = res.group(1).split('\n')
			writer.writerow({'email':m[0]})
		else:
			pass

