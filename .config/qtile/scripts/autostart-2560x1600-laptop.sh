#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#starting utility applications at boot time
feh --bg-fill /usr/share/backgrounds/nebula.jpg &
run nm-applet &
run pamac-tray &
run numlockx on &
run blueberry-tray &
run ulauncher --no-window &
run picom --experimental-backends --config $HOME/.config/picom/picom.conf &
run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
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

#starting user applications at boot time
