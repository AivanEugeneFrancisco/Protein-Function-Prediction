from Bio.Blast.Applications import NcbipsiblastCommandline
import re
import os
import time
start_time = time.time()
feature_num = 20
threads_count = 4
sequences_dir = "sequences"
selectedf_name = "sel_AC_topGO.dat"
inf_name = "AC_BIN.dat"
outf_name = "sel_AC_Blast.dat"
selectedf = open(selectedf_name, "r")
inf = open(inf_name, "r")
print selectedf_name + " and " + inf_name + " opened!"
selected = []
for line in selectedf:
	line = line.strip('\n')
	splited = line.split('\t')
	selected.append(splited[0])
AC_BIN_dict = {}
for line in inf:
	line = line.strip('\n')
	splited = line.split('\t')
	AC_BIN_dict[splited[0]] = splited[1]
outf = open(outf_name, "w")
os.chdir(sequences_dir)
print "Current directory changed into " + sequences_dir + "!"
percent_count = 0
for item in selected:
	outf.write(item + "\t")
#	cline = NcbipsiblastCommandline(query = item + ".fasta", db = "swissprot", max_hsps_per_subject = 1, num_threads = threads_count, outfmt = 0, out = "tmp.log")
	cline = NcbipsiblastCommandline(query = item + ".fasta", db = "swissprot", num_threads = threads_count, outfmt = 0, out = item + ".log")
	if percent_count % (len(selected) / 100) == 0:
		print str(percent_count / (len(selected) / 100)) + "% finished!"
		if percent_count == 0:
			print "Time elasped: Unknown"
			print "Time remaining: Unknown"
		else:
			m, s = divmod(time.time() - start_time, 60)
			h, m = divmod(m, 60)
			print "Time elasped: %d:%02d:%02d" % (h, m, s)
			del h,m,s
			m, s = divmod((float(len(selected)) / percent_count) * (time.time() - start_time) - (time.time() - start_time), 60)
			h, m = divmod(m, 60)
			print "Time remaining: %d:%02d:%02d" % (h, m, s)
			del h,m,s
	#print item + ".fasta is under processing!"
	stdout, stderr = cline()
	tmpf_name = item + ".log"
	blastf = open(tmpf_name, "r")
	AC = ""
	expect = ""
	count = 0
	for line in blastf:
		line = line.strip("\n")
		matched = re.match(r'^sp\|(\w+)\.\w+\|\w+?\s+RecName:\s+.+?\s+[0-9]+(\.[0-9])?\s+([0-9]+.[0-9]+|[0-9]+e-[0-9]+)\s*$', line)
		if matched:
			if count < feature_num:
				AC = matched.group(1)
				#get rid of the same ac number
				if AC == item:
					continue
				expect = matched.group(3)
				if AC in AC_BIN_dict:
					#0:010 can show from 0 to 1024 int
					if '.' in expect:
						outf.write(AC_BIN_dict[AC] + '1' * 10)
					else:
						matched = re.match(r'^[0-9]+e-([0-9]+$)', expect)
						outf.write(AC_BIN_dict[AC] + '{0:010b}'.format(int(matched.group(1))))
				else:
					continue
				AC = ""
				expect = ""		
				count += 1
			else:
				break
	#if there is not enough alignments
	while count < feature_num:
		outf.write("0" * 20 + "0" * 10)
		count += 1
	blastf.close()
#	os.remove(tmpf_name)
	outf.write("\n")
	percent_count += 1
os.chdir("..")
outf.close()
print outf_name + " generated!"
total_time = time.time() - start_time
m, s = divmod(time.time() - start_time, 60)
h, m = divmod(m, 60)
print "Total blast time is: %d:%02d:%02d" % (h, m, s)
