while (( 1 == 1 ))
do
    read -p "Enter a command: " comm
    echo $comm
    if [[ $comm == "hello" ]]
    then 
	echo "Hello $(whoami)" 
    elif [[ $comm == "quit" ]]
    then
	echo "Exiting..."
	exit 0
    elif [[ $comm == "compile" ]]
    then
	read -p "Enter filename: " file
	if [[ ! -r $file ]]
	then
	    echo "That file does not exist. Exiting!"
	    exit 0
	else
	    if gcc -Wall -Werror $file
	    then
		echo "Compilation succeded"
	    else
		echo "Compilation failed"
	    fi
	fi
    else
	echo "Error: Enrecognized input"
    fi
done
exit 0
