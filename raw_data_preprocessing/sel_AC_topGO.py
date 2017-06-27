import random
import math
inf_name = "AC_topGO.dat"
outf_name = "sel_AC_topGO.dat"
#number of selected GO term
#has to be the same number is gen_AC_topGO.py
num = 1
#num = 10
inf = open(inf_name, "r")
outf = open(outf_name, "w")
#total number is the number of sequences which has GO term
#which can be obtained in gen_AC_GO.py
total_num = 521394
occur_num = 0
countf = open("topGO.dat", "r")
for line in countf:
	line = line.strip('\n')
	splited = line.split('\t')
	occur_num = splited[1]
#calculation of the probability of the occurrence of certain GO term
fractile = float(occur_num) / total_num
#pos_sel_num = 3000
#neg_sel_num = 12000
#set sample number needed here (in interger), use cell to make sure at least one instance
pos_sel_num = int(math.ceil(fractile * 10000))
neg_sel_num = 10000 - pos_sel_num
print str(pos_sel_num) + " positive entries, and " +  str(neg_sel_num) + " negative entries."
if inf:
	print inf_name + " opened!"
positive = {}
negative = {}
for line in inf:
	line = line.strip('\n')
	splited = line.split('\t')
	fmt = '{0:0' + str(num) + 'b}'
	zeros = fmt.format(0)
	#if splited[1] == "0000000000":
	if splited[1] == zeros:
		negative[splited[0]] = splited[1]
	else:
		positive[splited[0]] = splited[1]
pos_AC = positive.keys()
neg_AC = negative.keys()
sel_pos_AC = random.sample(pos_AC, pos_sel_num)
sel_neg_AC = random.sample(neg_AC, neg_sel_num)
all_AC = sel_pos_AC + sel_neg_AC
random.shuffle(all_AC)
print str(len(all_AC)) + " entries added!"
for item in all_AC:
	if (positive.has_key(item)):
		outf.write(item + '\t' + positive[item] + "\n")
	elif (negative.has_key(item)):
		outf.write(item + '\t' + negative[item] + "\n")
outf.close()
print outf_name + " generated!"
