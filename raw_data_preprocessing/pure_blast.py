# this script is intended to compare with my method
import re
import os
import time
import pprint as pp
start_time = time.time()
sequences_dir = "sequences"
selectedf_name = "sel_AC_topGO.dat"
topf_name = "topGO.dat"
fullf_name = "AC_GO.dat"
threads_count = 4
hit_count = 0
fullf = open(fullf_name, 'r')
full_dict = {}
selected_dict = {}
for line in fullf:
	line = line.strip('\n')
	splited = line.split('\t')
	tmp = splited[0]
	splited = splited[1].split(',')
	splited.pop()
	full_dict[tmp] = splited
selectedf = open(selectedf_name, 'r')
topf = open(topf_name, 'r')
for line in topf:
	line = line.strip('\n')
	splited = line.split('\t')
	topGO = splited[0]
for line in selectedf:
	line = line.strip('\n')
	splited = line.split('\t')
	selected_dict[splited[0]] = int(splited[1])
#pp.pprint(selected_dict)
#pp.pprint(full_dict)
os.chdir(sequences_dir)
# in case there is no alignment for a sequence
for key, value in selected_dict.items():
	blastf = open(key + ".log", "r")
	for line in blastf:
		line = line.strip('\n')
		matched = re.match(r'^sp\|(\w+)\.\w+\|\w+?\s+RecName:\s+.+?\s+[0-9]+(\.[0-9])?\s+([0-9]+.[0-9]+|[0-9]+e-[0-9]+)\s*$', line)
		if matched:
			AC = matched.group(1)
			if AC == key:
				continue
			else:
				try:
					full_dict[AC]
				except KeyError:
					continue
				if topGO in full_dict[AC]:
					if selected_dict[key] == 1:
						hit_count = hit_count + 1/float(len(full_dict[AC]))
				else:
					if selected_dict[key] == 0:
						hit_count = hit_count + 1/float(len(full_dict[AC]))
				break
print "The accuracy of pure Psi-Blast is", float(hit_count)/len(selected_dict)
