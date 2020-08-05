#   __                _     _                      
#  / _|_   _____ __ _| | __| | ___ _ __ __ _ _ __  
# | |_\ \ / / __/ _` | |/ _` |/ _ \ '__/ _` | '_ \ 
# |  _|\ V / (_| (_| | | (_| |  __/ | | (_| | | | |
# |_|   \_/ \___\__,_|_|\__,_|\___|_|  \__,_|_| |_|
#
# My github: https://github.com/fvcalderan/

#!/bin/bash

sudo mkdir -p ~/.config/qtile/
sudo ln -s -f ~/dotfiles/.config/qtile/config.py ~/.config/qtile/config.py
sudo mkdir -p ~/.config/termite/
sudo ln -s -f ~/dotfiles/.config/termite/config ~/.config/termite/config
sudo mkdir -p ~/.config/zathura/
sudo ln -s -f ~/dotfiles/.config/zathura/zathurarc ~/.config/zathura/zathurarc
sudo mkdir -p /etc/X11/xorg.conf.d/
sudo ln -s -f ~/dotfiles/etc/X11/xorg.conf.d/30-touchpad.conf /etc/X11/xorg.conf.d/30-touchpad.conf
sudo mkdir -p ~/.config/wallpapers/
sudo ln -s -f ~/dotfiles/.config/wallpapers/wallpaper ~/.config/wallpapers/wallpaper
sudo mkdir -p ~/.config/vifm
sudo ln -s -f ~/dotfiles/.config/vifm/vifmrc ~/.config/vifm/vifmrc
sudo mkdir -p ~/.config/vifm/colors/
sudo ln -s -f ~/dotfiles/.config/vifm/colors/Default.vifm ~/.config/vifm/colors/Default.vifm
sudo mkdir -p ~/.config/vifm/scripts
sudo ln -s -f ~/dotfiles/.config/vifm/scripts ~/.config/vifm/scripts

sudo ln -s -f ~/dotfiles/homefolder/.bashrc ~/.bashrc
sudo ln -s -f ~/dotfiles/homefolder/.xbindkeysrc ~/.xbindkeysrc
sudo ln -s -f ~/dotfiles/homefolder/.xinitrc ~/.xinitrc

sudo cp ~/dotfiles/scripts/scrot_select /bin/scrot_select


