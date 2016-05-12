#! /bin/bash
#
# $Author: ee364c10 $:
# $Date: 2015-01-25 19:34:50 -0500 (Sun, 25 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab02/run.bash $:
command gcc $1 -o quick_sim
if [[ $? = 1 ]] 
then
    echo "error: quick_sim could not be compiled!"
    exit 1
fi
file=$2
while [[ -e $file ]]
do
    read -p "$file exists. Would you like to delete it? " response
    echo $response
    if [[ $response != "y" &&  $response != "yes" ]]
    then
	read -p "Enter a new filename: " file
    else
	command rm $file
	break
    fi
done
command touch $file
cache="1 2 4 8 16 32"
set $cache
issue="1 2 4 8 16"
set $issue
#for i in ${cache[*]}
#do
#    echo $i
#done
#for j in ${issue[*]}
#do
#    echo $j
#done
proc_name=()
cache_size=()
issue_size=()
cpi=()
exec_time=()
manufacturer="a i"
set $manufacturer
count=0
for i in ${cache[*]}
do
    for j in ${issue[*]}
    do
	for k in ${manufacturer[*]}
	do
	    #echo $i ":" $j : $k
	    if [[ $k == "a" ]]
	    then
		proc_name[$count]="AMD Opteron"
		#echo "${proc_name[$count]}"
	    else
		proc_name[$count]="Intel Core i7"
		#echo "${proc_name[$count]}"
	    fi
	    #command quick_sim $i $j $k
	    cache_size[$count]=$(command quick_sim $i $j $k | cut -d':' -f4)
	    #echo "cache size: ${cache_size[$count]}"
	    issue_size[$count]=$(command quick_sim $i $j $k | cut -d':' -f6)
	    #echo "issue size: ${issue_size[$count]}"
	    cpi[$count]=$(command quick_sim $i $j $k | cut -d':' -f8)
	    #echo "CPI: ${cpi[$count]}"
	    exec_time[$count]=$(command quick_sim $i $j $k | cut -d':' -f10)
	    #echo "Execution Time: ${exec_time[$count]}"
	    echo "${proc_name[$count]}:${cache_size[$count]}:${issue_size[$count]}:${cpi[$count]}:${exec_time[$count]}">>$file
	    ((count=$count+1))
	done
    done
done
#echo $count
high_exec_time=0
index=0
for (( l = 0; l <= $count-1; l++ ))
do
    if (( ${exec_time[$l]} >= $high_exec_time ))
    then
	high_exec_time=${exec_time[$l]}
	index=$l
    fi
done
#echo $file
echo "Fastest run time achieved by ${proc_name[$index]} with cache size ${cache_size[$index]} and issue width ${issue_size[$index]} was ${exec_time[$index]}"
exit 0

	