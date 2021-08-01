#!/bin/sh

xmenu <<EOF | sh &
Applications
	Alacritty			alacritty
	Bitwarden			bitwarden
	Calculator			galculator
	Calendar			gnome-calendar
	Dictionary			xfce4-dict
	Evince				evince
	Meteo				meteo
	OnlyOffice			onlyoffice-desktopeditors
	Thunar				thunar
	Pinta				pinta
	Ristretto			ristretto
	Scan				simple-scan
	Virt-manager		virt-manager
	Xarchiver			xarchiver
	XTerm				xterm
Games
	GZDoom				gzdoom
Internet
	Brave				brave
	FileZilla			filezilla
	Firefox				firefox
	Mailspring			mailspring
	Skype				skypeforlinux
	Thunderbird			thunderbird
Multimedia
	Audacious			audacious
	Mediainfo			mediainfo-gui
	MKVToolNix			mkvtoolnix-gui
	Mpv					mpv
	Spotify				spotify
	VLC					vlc
Programming
	Codium				codium
	Gitg				gitg
	Sublime Text		subl
Utilities
	Bluetooth			blueberry
	Gnome Settings		gnome-control-center
	GParted				gparted
	Kvantum Manager		kvantummanager
	Pamac				pamac-manager
	Network Manager		nm-connection-editor
	Nvidia Settings		nvidia-settings
	Optimus Manager		optimus-manager-qt
	Power Manager		xfce4-power-manager-settings
	Printer Settings	system-config-printer
	Task Manager		xfce4-taskmanager

Shutdown		poweroff
Reboot			reboot
Logout			logout
EOF
