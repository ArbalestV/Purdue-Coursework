#! /bin/bash
#
# $Author: ee364c10 $:
# $Date: 2015-01-24 23:35:47 -0500 (Sat, 24 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab02/yards.bash $:
    if [[ $# < 1 ]]
    then
	echo "Usage: yards.bash <filename>"
	exit 0
    fi

    if [[ ! -r $1 ]]
    then
	echo "$1 is not readable"
	exit 0
    fi

    file=$1
    #n_lines=($(#wc -l stats.txt)) #find the total number of lines-> # of conferences
    #echo $n_lines
    i=0
    conf=()
    conf_avg=()
    conf_var=()

    while read file
    do
	conf[$i]=$(echo $file | cut -d' ' -f1) #name of the ith conference
	#kil=${conf[$i]}
	#echo $kil
	j=2
	vals=()
	
	while [[ $(echo $file | cut -d' ' -f$j) != "" ]]
	do
	    tmp=$(echo $file | cut -d' ' -f$j)
	    vals[(($j-2))]=$tmp
	    ((j=$j+1))
	done
	((j=$j-2)) #total number of entries corresponding to this conference
	avg=0
	var=0
	for (( k = 0; k <= $j-1; k++)) #loop to calculate the average
	do
	    ((avg=$avg+${vals[$k]}))
	done
	((avg=$avg/$j))
	conf_avg[$i]=$avg
	#echo "average: $avg"
	for (( l = 0; l <= $j-1; l++))
	do
	    let tmp1=${vals[$l]}-$avg
	    let tmp2=($tmp1)**2
	    ((var=$var+$tmp2))
	done
	((var=$var/$j))
	conf_var[$i]=$var
	#echo "variance: $var"
	((i=$i+1))
    done < $1
    high_avg=0
    for (( m = 0; m <= $i-1; m++))
    do
	if (( ${conf_avg[$m]} >= $high_avg ))
	then
	    high_avg=${conf_avg[$m]}
	fi
	echo "${conf[$m]} schools have averaged ${conf_avg[$m]} yards receiving with a variance of ${conf_var[$m]}"
    done
    echo "The largest average yardage was $high_avg"
exit 0
	
	
	
	
	    
	
	