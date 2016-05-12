# EE364 student .bashrc file  
#
if [[ -r ~ee364/config/default.bashrc ]]  
then
    . ~ee364/config/default.bashrc
fi

if [[ -f ${HOME}/.bash_ansi_prompt ]] 
then
  . ${HOME}/.bash_ansi_prompt	
fi

#if [[ -f ${HOME}/.bash_ansi_edit ]] 
#then
#  . ${HOME}/.bash_ansi_edit	
#fi

#
# Do NOT edit above this line!!!!!!!!!!!
#
