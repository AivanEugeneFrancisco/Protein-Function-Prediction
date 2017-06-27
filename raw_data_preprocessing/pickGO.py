num = 1;
inf_name = "AC_GO.dat"
outf_name = "topGO.dat"
inf = open(inf_name,"r")
if inf:
	print inf_name + " opened!"
outf = open(outf_name,"w")
dict = {}
for line in inf:
	line = line.strip('\n')
	splitedLine = line.split('\t')
	second = splitedLine[1]
	go = second.split(',')
	for item in go:
		if dict.has_key(item):
			dict[item] += 1
		else:
			dict[item] = 1
sort = sorted(dict.items(), key = lambda x: x[1], reverse = True)
selected = sort[1:num + 1]
for i in selected:
	outf.write(i[0] + '\t' + str(i[1]) + '\n')
inf.close()
outf.close()
print outf_name + " generated!"
