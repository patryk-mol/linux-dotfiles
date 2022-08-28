#!/bin/bash

feh --bg-fill /usr/share/backgrounds/moon.jpg &
nm-applet &
pamac-tray &
numlockx on &
ulauncher --no-window &
picom --experimental-backends --config $HOME/.config/picom/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xidlehook \
  --not-when-fullscreen \
  --not-when-audio \
  --timer 300 \
    'betterlockscreen -l' \
    '' \
  --timer 600 \
    'systemctl suspend' \
    '' &