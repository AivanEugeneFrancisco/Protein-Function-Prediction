import re
import os
from Bio import SeqIO
inf_name = "uniprot_sprot.fasta"
selectedf_name = "sel_AC_topGO.dat"
out_dir = "sequences"
records = SeqIO.index(inf_name, "fasta")
print str(len(records)) + " records loaded!"
selectedf = open(selectedf_name, "r")
content = ""
selected = []
count = 0
entries = 0
os.chdir(out_dir)
print "Output directory changed into " + out_dir + "!"
for line in selectedf:
	line = line.strip('\n')
	splited = line.split('\t')
	selected.append(splited[0])
print str(len(selected)) + " selected records loaded!"
sorted_records = sorted(records)
for item in sorted_records:
	matched = re.match(r'^sp\|(\w+)\|', item)
	if matched:
		entries += 1
		if matched.group(1) in selected:
			count += 1
			content = records[item].format("fasta")
			outf_name = matched.group(1) + ".fasta"
			outf = open(outf_name, "w")
			outf.write(content)
			outf.close()
print str(entries) + " records compared!"
print str(count) + " files generated!"
records.close()