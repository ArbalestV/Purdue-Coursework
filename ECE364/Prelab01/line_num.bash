#! /bin/bash
#
# $Author: ee364c10 $:
# $Date: 2015-01-19 21:27:27 -0500 (Mon, 19 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab01/line_num.bash $:
if [[ ! $# == 1 ]]
then
    echo "Only one filename needed. Exiting!"
    exit 0
fi
file=$1
if [[ ! -r $file ]] 
then
    echo "Cannot read $file"
else
#cat -n $file
i=0
while read file
do 
    ((i=$i+1))
    echo "$i:$file"
done < $1
fi
exit 0


