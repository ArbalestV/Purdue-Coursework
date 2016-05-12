#! /bin/bash
#
# $Author: ee364c10 $:
# $Date: 2015-01-19 22:45:03 -0500 (Mon, 19 Jan 2015) $:
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364c10/Prelab01/check_file.bash $:
if [[ ! $# == 1 ]]
then 
    echo "At most one file name required. Exiting!"
    exit 0
fi
file=$1
if [[ ! -e $file ]] 
then
    echo "$file does not exist"
else
    echo "$file exists"
fi
if [[ ! -d $file ]] 
then
    echo "$file is not a directory"
else
    echo "$file is a directory"
fi
if [[ ! -f $file ]] 
then
    echo "$file is not an ordinary file"
else
    echo "$file is an ordinary file"
fi
if [[ ! -r $file ]] 
then
    echo "$file is not readable"
else
    echo "$file is readable"
fi
if [[ ! -w $file ]] 
then
    echo "$file is not writable"
else
    echo "$file is writable"
fi
if [[ ! -x $file ]] 
then
    echo "$file is not executable"
else
    echo "$file is executable"
fi
exit 0
