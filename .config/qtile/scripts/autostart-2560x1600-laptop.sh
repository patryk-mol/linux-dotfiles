#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#Some ways to set your wallpaper besides variety or nitrogen
feh --bg-fill /usr/share/backgrounds/space.jpg &

#starting utility applications at boot time
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
run deadd-notification-center &

numlockx on &
blueberry-tray &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

#starting user applications at boot time
run cbatticon -u 1 -i notificationq &