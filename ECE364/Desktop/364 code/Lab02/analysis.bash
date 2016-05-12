#! /bin/bash
#
# $Author: ee364c10 $:
# $Date: 2015-01-28 10:21:46 -0500 (Wed, 28 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Lab02/analysis.bash $:
 if [[ $# < 1 ]]
 then
     echo "Usage: analysis.bash <input file>"
     exit 1
 fi
if [[ ! -r $1 ]]
then
    echo "$1 is not readable"
    exit 2
fi
file=$1
i=0
proc=()
proc_avg=()
avg_p_w=()
while read file
do
   proc[$i]=$(echo $file | cut -d' ' -f1,2) 
   #echo "${proc[$i]}"
   j=3
   vals=()
   while [[ $(echo $file | cut -d' ' -f$j) != "" ]]
   do
       tmp=$(echo $file | cut -d' ' -f$j)
       vals[(($j-3))]=$tmp
       #echo "$tmp"
       ((j=$j+1))
       #echo $j
   done
   let p=$j-4
   #echo $p
   #echo ${vals[$p]}
   let pow=${vals[$p]}
   ((j=$j-2)) #total number of entries corresponding to this processor
   avg=0
   
   for (( k = 0; k <= $p-1; k++)) #loop to calculate the average
   do
       ((avg=$avg+${vals[$k]}))
   done
   ((avg=$avg/$k))
   #echo $avg
   proc_avg[$i]=$avg
   #let const=9/10
   let avg2=9*$avg/10
   #echo $avg2
   for (( l = 0; l <= $p-1; l++))
   do
       if (( ${vals[$l]} < $avg2 ))
       then
	   tmp=${vals[l]}
	   echo "Run 1 for ${proc[$i]} with score $tmp was 90% less than average"
       fi
   done
   echo "${proc[$i]} scored an average of $avg"
   let avg_p_w[$i]=$avg/$pow
   ((i=$i+1))
done < $1
high_avg=0
proc_n=""
for (( m = 0; m <= $i-1; m++))
do
    if (( ${avg_p_w[$m]} >= $high_avg ))
    then
	high_avg=${avg_p_w[$m]}
	proc_n=${proc[$m]}
    fi
done
echo "The best performance per watt was received by $proc_n at $high_avg"
exit 0

   