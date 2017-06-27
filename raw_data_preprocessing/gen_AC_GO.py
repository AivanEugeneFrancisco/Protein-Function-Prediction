import re
inf_name = "uniprot_sprot.dat"
outf_name = "AC_GO.dat"
outf2_name = "AC_BIN.dat"
inf = open(inf_name, "r")
if inf:
	print inf_name + " opened!"
outf = open(outf_name,"w")
outf2 = open(outf2_name, "w")
AC = ""
AC_flag = 0
GO = ""
count = 0
count_AC_GO = 0
for line in inf:
	if re.match(r'\/\/', line):
		if AC and GO:
			count_AC_GO += 1
			if count % 10000 == 0:
				print str(count) + " entries generated!"		
			outf.write(AC + '\t' + GO + '\n')
		AC = ""
		AC_flag = 0
		GO = ""
		count += 1
	else:
		match_ac = re.match(r'^AC\s+(\w+);', line)
		if match_ac:
			if AC_flag == 0:
				AC = match_ac.group(1)
				outf2.write(AC + '\t' + '{0:020b}'.format(count) + '\n')
				AC_flag = 1
		match_go = re.match(r'^DR\s+GO;\s+GO:(\d+);', line)
		if match_go:
			GO = GO + match_go.group(1) + ','
inf.close()
print "Total: " + str(count_AC_GO) + " out of " + str(count) + " entries gathered!"
outf.close()
print outf_name + " generated!"
print outf2_name + " generated!"
