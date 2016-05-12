#! /bin/bash
#
# $Author: ee364c10 $:
# $Date: 2015-01-21 11:37:39 -0500 (Wed, 21 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab01/collect_expr.bash $:
#while (( 1 == 1 ))
#do
if [[ $# < 2 ]]
then
    echo "collect_expr.bash $1"
    exit 1
fi

if [[ -e $1 ]]
then 
    echo "output file $out_file already exists!"
    exit 2
fi
i=0
out_file=$1 #get the output file
ifile=()
    shift #shift the output file
    while (( $# != 0 ))
    do
	ifile[$i]=$1
	if [[ ! -r $1 ]]
	then
	    echo "error: input file $1 is not readable!"
	exit 2
	fi
	((i=$i+1))
	#exit 2
	shift
    done
    #if we reach here that means that the above three situations are not satisfied
    #exec 4> $out_file
    
    for (( j = 0; j <= $i-1; j++ ))
    do
	now=${ifile[$j]}
        echo $now
	while read line
	do
	    name=$(echo $line | cut -d' ' -f 1)
	    data1=$(echo $line | cut -d' ' -f2)
	    data2=$(echo $line | cut -d' ' -f3)
	    data3=$(echo $line | cut -d' ' -f4)
	    data4=$(echo $line | cut -d' ' -f5)
	    data5=$(echo $line | cut -d' ' -f6)
	    let sum=$data1+$data2+$data3+$data4+$data5
	    let avg=$sum/5
	    echo "$name $data1 $data2 $data3 $data4 $data5 $sum $avg">>$out_file
	done < $now
    done
    exit 0
