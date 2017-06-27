inf_1_name = "AC_GO.dat"
inf_2_name = "topGO.dat"
outf_name = "AC_topGO.dat"
#number of selected GO term
#has to be the same number in sel_AC_topGO.py
#num = 10
num = 1
inf_1 = open(inf_1_name, "r")
inf_2 = open(inf_2_name, "r")
outf = open(outf_name, "w")
if inf_1 and inf_2:
	print inf_1_name + " and " + inf_2_name + " opened!"
GO_list = []
for line in inf_2:
	line = line.strip('\n')
	splited = line.split('\t')
	GO_list.append(splited[0])
GO_dict = {}
for i in range(len(GO_list)):
	GO_dict[GO_list[i]] = 1 << ((num - 1) - i)
for line in inf_1:
	line = line.strip('\n')
	splited = line.split('\t')
	AC = splited[0]
	GO = splited[1].split(',')
	GO_BIN = 0
	for item in GO:
		if item:
			if GO_dict.has_key(item):
				GO_BIN = GO_BIN | GO_dict[item]
	#outf.write(AC + '\t' + '{0:010b}'.format(GO_BIN) + '\n')
	fmt = '{0:0' + str(num) + 'b}'
	outf.write(AC + '\t' + fmt.format(GO_BIN) + '\n')
inf_1.close()
inf_2.close()
outf.close()
print outf_name + " was generated!"
