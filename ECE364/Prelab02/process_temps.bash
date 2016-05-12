#! /bin/bash
#
# $Author: ee364c10 $:
# $Date: 2015-01-25 15:25:29 -0500 (Sun, 25 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab02/process_temps.bash $:
if [[ ! $# = 1 ]]
then
    echo "Usage: process_temps.bash <input file>"
    exit 1
fi
if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file."
    exit 2
fi
file=$1
i=0
while read file
do
    #echo $i
    if (( i == 0 ))
    then
	((i=$i+1))
	continue
    else
	time=$(echo $file | cut -d' ' -f1)
	#echo $time
	j=2
	vals=()
	avg=0
	while [[ $(echo $file | cut -d' ' -f$j) != "" ]]
	do
	    tmp=$(echo $file | cut -d' ' -f$j)
	    #echo $tmp
	    let k=$j-2
	    #echo $k
	    let vals[$k]=$tmp
	    #echo "${vals[$k]}"
	    let avg=$avg+vals[$k]
	    let j=$j+1
	   # echo $j
	done
	let j=$j-2
	#echo $j
	#echo $avg
	let avg=$avg/$j
	#echo $avg
	   
    echo "Average temperature for time $time was $avg C."
    let i=$i+1
    fi
done < $1
exit 0