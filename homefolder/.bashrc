#   __                _     _                      
#  / _|_   _____ __ _| | __| | ___ _ __ __ _ _ __  
# | |_\ \ / / __/ _` | |/ _` |/ _ \ '__/ _` | '_ \ 
# |  _|\ V / (_| (_| | | (_| |  __/ | | (_| | | | |
# |_|   \_/ \___\__,_|_|\__,_|\___|_|  \__,_|_| |_|
#
# My github: https://github.com/fvcalderan/

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Custom path
PATH="$PATH:/home/skore/dotfiles/scripts:/home/skore/.local/bin"; export PATH
EDITOR="nvim"; export EDITOR

# aliases
alias ls='ls -A --color=auto'
alias la='ls -la --color=auto'
alias ..='cd ..'
alias vi='nvim'
alias vim='nvim'
alias grep='grep --color=auto'
alias vifm='vifmrun'
alias cl='clear'
alias rm='rm -i'

# bash prompt. Default: PS1='[\u@\h \W]\$ '
PS1="\[\e[1;36m\]\u\[\e[m\]:\[\e[33m\]\W\[\e[m\]\$ "

# set vi mode
set -o vi

# run ufetch
ufetch
