#! /bin/bash
#
# $Author: ee364c10 $: 
# $Date: 2015-01-19 20:00:56 -0500 (Mon, 19 Jan 2015) $: 
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab01/sum.bash $:
sum=0
while [[ ! $# == 0 ]]
do
    ((sum=$sum+$1))
    shift
done
echo $sum
exit 0 
