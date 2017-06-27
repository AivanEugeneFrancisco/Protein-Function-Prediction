from Bio.Blast.Applications import NcbipsiblastCommandline
import re
feature_num = 20
threads_count = 4
input_filename = "input.fasta"
output_filename= "test_features.npy"
inf_name = "../AC_BIN.dat"
inf = open(inf_name, "r")
AC_BIN_dict = {}
for line in inf:
	line = line.strip('\n')
	splited = line.split('\t')
	AC_BIN_dict[splited[0]] = splited[1]
cline = NcbipsiblastCommandline(query = input_filename, db = "swissprot", num_threads = threads_count, outfmt = 0, out = "temp.log")
stdout, stderr = cline()
blastf = open("temp.log", "r")
outf = open(output_filename,"w")
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
outf.write("\n")
outf.close()
