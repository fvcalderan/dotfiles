#   __                _     _                      
#  / _|_   _____ __ _| | __| | ___ _ __ __ _ _ __  
# | |_\ \ / / __/ _` | |/ _` |/ _ \ '__/ _` | '_ \ 
# |  _|\ V / (_| (_| | | (_| |  __/ | | (_| | | | |
# |_|   \_/ \___\__,_|_|\__,_|\___|_|  \__,_|_| |_|
#
# My github: https://github.com/fvcalderan/

# set resolution
# xrandr --output eDP1 --mode 1366x768 --left-of HDMI1
mons -e right

# set keyboard layout and swap Esc/Caps
setxkbmap br
setxkbmap -option caps:swapescape

# set keyboard special keys (volume and brightness)
xbindkeys

# change keyboard letter repetition to a faster speed
xset r rate 300 50

# start compositor
picom &

# set wallpaper
feh --bg-scale ~/.config/wallpapers/wallpaper

# start windowmanager
exec qtile
