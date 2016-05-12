#! /bin/bash
#
# $Author: ee364c10 $: 
# $Date: 2015-01-19 20:48:32 -0500 (Mon, 19 Jan 2015) $: 
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab01/exist.bash $:
while [[ ! $# == 0 ]]
do
    file=$1
    #echo $file
    if [[ -r $file ]]
    then
	#echo $file
	echo "File $1 is readable"
    else
	if [[ ! -e $file ]]
	then
	    touch $file
	fi
    fi
    shift
done
exit 0     
