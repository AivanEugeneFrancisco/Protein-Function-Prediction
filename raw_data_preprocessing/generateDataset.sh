#!/bin/bash
clear
if [ -d "sequences" ]
then
	echo "Deleting and making directory \"sequences\""
	rm -r sequences
	mkdir sequences
	sleep 3
	clear
else
	echo "Making directory \"sequences\""
	mkdir sequences
	sleep 3
	clear
fi
echo "Running gen_AC_GO.py"
python gen_AC_GO.py
sleep 3
clear
echo "Running pickGO.py"
python pickGO.py
sleep 3
clear
echo "Running gen_AC_topGO.py"
python gen_AC_topGO.py
sleep 3
clear
echo "Running sel_AC_topGO.py"
python sel_AC_topGO.py
sleep 3
clear
echo "Running parse_sprot.py"
python parse_sprot.py
sleep 3
clear
echo "Running blast_sequences.py"
python blast_sequences.py
sleep 3
clear
echo "Running prepare_dataset.py"
python prepare_dataset.py
sleep 3
clear
#echo "Stopping the instance!"
#sleep 5
#ec2-stop-instances i-1a5755c1 --region us-west-2
