#!/bin/bash

feh --bg-fill /usr/share/backgrounds/nebula.jpg &
nm-applet &
pamac-tray &
numlockx on &
blueberry-tray &
ulauncher --no-window &
picom --experimental-backends --config $HOME/.config/picom/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xidlehook \
  --not-when-fullscreen \
  --not-when-audio \
  --timer 60 \
    'xbacklight -set 10 -time 0 -steps 1' \
    'xbacklight -set 60 -time 0 -steps 1' \
  --timer 240 \
    'xbacklight -set 10 -time 0 -steps 1; betterlockscreen -l' \
    'xbacklight -set 60 -time 0 -steps 1' \
  --timer 300 \
    'systemctl suspend' \
    'xbacklight -set 60 -time 0 -steps 1' &
