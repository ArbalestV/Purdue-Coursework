#! /bin/bash
#
# $Author: ee364c10 $:
# $Date: 2015-01-20 00:58:53 -0500 (Tue, 20 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab01/sensor_sum.sh $:
if [[ ! $# == 1 ]]
then
    echo "One filename needed. Exiting!"
    exit 0
fi
file=$1
while read file
do
    #echo $file
    now=$file
    #tmp=$(echo $file)
    #echo $tmp
    #tmp=$("$now" | cut -d' ' -f1)
    tmp=$(echo "$now" | cut -d' ' -f1 | cut -c1,2)
    #echo $tmp
    tmp2=$(echo "$now" | cut -d' ' -f3)
    #echo $tmp2
    tmp3=$(echo "$now" | cut -d' ' -f5)
    #echo $tmp3
    tmp4=$(echo "$now" | cut -d' ' -f7)
    #echo $tmp4
    let tmp5=$tmp2+$tmp3+$tmp4
    #echo $tmp5
    echo $tmp" "$tmp5
    #sun=$(cut -d ' ' -f 1 | cut -c 1-2)
    #echo $tmp
   # echo $tmp1
    #echo "$(file | cut -c1,2)"
    #sen=$(file | cut -c1,2)
    #sen=cut 
   # echo $sen
    #val1="$(echo file | cut -f1)"
    #val2="$(echo file | cut -f2)"
    #val3="$(echo file | cut -f3)"
    #let tot=val1+val2+val3
    #echo "$sen $tot"
done < $1
exit 0
