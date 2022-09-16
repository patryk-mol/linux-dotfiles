import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy
from libqtile.widget import Spacer

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def next_screen_number():
    current_screen = qtile.screens.index(qtile.current_screen)
    if current_screen is 0:
        return 2
    if current_screen is 1:
        return 0
    if current_screen is 2:
        return 2
    return current_screen

@lazy.function
def move_screen_focus_left(qtile):
    qtile.cmd_to_screen(next_screen_number())

def prev_screen_number():
    current_screen = qtile.screens.index(qtile.current_screen)
    if current_screen is 0:
        return 1
    if current_screen is 1:
        return 1
    if current_screen is 2:
        return 0
    return current_screen

@lazy.function
def move_screen_focus_right(qtile):
    qtile.cmd_to_screen(prev_screen_number())

keys = [

# Most of our keybindings are in sxhkd file - except these

# SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),

# SUPER + SHIFT KEYS
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod, "mod1"], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# MOVE ACTIVE SCREEN
    Key([mod, "mod1"], "h", move_screen_focus_left()),
    Key([mod, "mod1"], "l", move_screen_focus_right()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

# VOLUME KEYBINDS
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 2%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 2%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toogle")),

# BRIGHTNESS KEYBINDS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10 -time 100")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10 -time 100")),

# SCREENSHOT KEYBINDS
    Key([], "Print", lazy.spawn("xfce4-screenshooter -r -s Pictures/")),
    Key(["shift"], "Print", lazy.spawn("xfce4-screenshooter -w -s Pictures/")),
    Key([mod], "Print", lazy.spawn("xfce4-screenshooter -f -s Pictures/")),

# MY KEYBINDS
    #Key([mod], "space", lazy.spawn("ulauncher-toggle"), desc='Run Launcher'),
    Key([mod], "b", lazy.spawn("brave"), desc='Run Brave'),
    Key([mod], "v", lazy.spawn("bitwarden-desktop"), desc='Run Bitwarden'),
    Key([mod, "shift"], "x", lazy.spawn("archlinux-logout"), desc="Open logout window"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc='Run Alacritty'),
    Key([mod], "t", lazy.spawn("thunar"), desc='Run Thunar'),
    Key([mod, "mod1"], "space", lazy.spawn("xfce4-appfinder"), desc="Open AppFinder"),
]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Work", "Code", "Files", "VM", "Video", "Gaming", "Mail", "Chat", "Music",]

group_layouts = ["max", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

def init_layout_theme():
    return {"margin":2,
            "border_width":2,
            "border_focus": "#aaaaac",
            "border_normal": "#464648"
            }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(margin=6, border_width=2, border_focus="#FFFFFF", border_normal="#414143"),
    layout.MonadThreeCol(margin=6, border_width=2, border_focus="#FFFFFF", border_normal="#414143"),
    layout.MonadWide(margin=6, border_width=2, border_focus="#FFFFFF", border_normal="#414143"),
    layout.Max(**layout_theme)
]

# COLORS FOR THE BAR
def init_colors():
    return [["#7f8c8d", "#7f8c8d"], # color 0 - active workspace color
            ["#1E1E20", "#1E1E20"], # color 1 - background
            ["#AAAAAC", "#AAAAAC"], # color 2 - font color
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5 - font color on bar
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#232324", "#232324"], # color 7
            ["#464648", "#464648"], # color 8 - inactive workspaces color
            ["#a9a9a9", "#a9a9a9"]] # color 9

colors = init_colors()

# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def open_notification_center():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/show-notification-center.sh'])

def init_widgets_list_display1():
    home = os.path.expanduser('~')
    widgets_list = [
        widget.GroupBox(
            font="FontAwesome",
            fontsize = 16,
            margin_y = 3,
            margin_x = 0,
            padding_y = 6,
            padding_x = 5,
            borderwidth = 0,
            disable_drag = True,
            active = colors[0],
            inactive = colors[8],
            rounded = False,
            highlight_method = "block",
            block_highlight_text_color = colors[7],
            this_current_screen_border = colors[5],
            this_screen_border = colors[5],
            foreground = colors[2],
            background = colors[1]
        ),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.WindowCount(font = "Noto Sans Bold", foreground = colors[2], background = colors[1], show_zero = True),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.CurrentLayout(font = "Noto Sans Bold", foreground = colors[2], background = colors[1]),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.CurrentScreen(font = "Noto Sans Bold", active_color = colors[2], inactive_color = colors[8], active_text = "active", inactive_text = "active"),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.Spacer(),
        widget.WindowName(font="Noto Sans", fontsize = 14, foreground = colors[5], background = colors[1], width=bar.CALCULATED),
        widget.Spacer(),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.Net(font="Noto Sans", fontsize = 12, foreground = colors[2], background = colors[1], format = '{down}', padding = 0),
        widget.TextBox(font = "FontAwesome", text = "    ", foreground = colors[5], background = colors[1], fontsize = 16),
        widget.Net(font="Noto Sans", fontsize = 12, foreground = colors[2], background = colors[1], format = '{up} ', padding = 0),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.TextBox(font = "FontAwesome", text = "  ", foreground = colors[5], background = colors[1], fontsize = 16),
        widget.ThermalSensor(
            foreground = colors[2],
            foreground_alert = colors[6],
            background = colors[1],
            metric = True,
            padding = 3,
            threshold = 80,
            update_interval = 1,
            tag_sensor = "CPU",
        ),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.TextBox(font = "FontAwesome", text = "  ", foreground = colors[5], background = colors[1], padding = 0, fontsize = 16),
        widget.CPU(font = "Noto Sans", format = '{freq_current}GHz {load_percent}%', foreground = colors[2], background = colors[1], padding = 0, fontsize = 12),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.TextBox(font = "FontAwesome", text = "  ", foreground = colors[5], background = colors[1], padding = 0, fontsize = 16),
        widget.Memory(
            font="Noto Sans",
            format = '{MemUsed:.0f}M/{MemTotal:.0f}M',
            update_interval = 1,
            fontsize = 12,
            foreground = colors[2],
            background = colors[1],
        ),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.TextBox(font = "FontAwesome", text = "  ", foreground = colors[5], background = colors[1], padding = 0, fontsize = 16),
        widget.Clock(font = "Noto Sans", foreground = colors[2], background = colors[1], fontsize = 12, format = "%Y-%m-%d %H:%M"),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.GenPollText(
            font = "FontAwesome",
            fontsize = 16,
            foreground = colors[5],
            background = colors[1],
            update_interval=1,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(home + '/.config/qtile/scripts/change-audio-output.sh')},
            func=lambda: subprocess.check_output(home + '/.config/qtile/scripts/current-audio-output.sh').decode("utf-8")),
        widget.Volume(foreground = colors[2], background = colors[1]),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.Systray(foreground = colors[2], background = colors[1], icon_size = 20, padding = 4),
        widget.TextBox(
            font = "FontAwesome",
            text = "      ",
            foreground = colors[2],
            background = colors[1],
            mouse_callbacks = {"Button1": open_notification_center},
            padding = 0,
        ),
    ]
    return widgets_list

def init_widgets_list_display2():
    widgets_list = [
        widget.GroupBox(
            font="FontAwesome",
            fontsize = 16,
            margin_y = 3,
            margin_x = 0,
            padding_y = 6,
            padding_x = 5,
            borderwidth = 0,
            disable_drag = True,
            active = colors[0],
            inactive = colors[8],
            rounded = False,
            highlight_method = "block",
            block_highlight_text_color = colors[7],
            this_current_screen_border = colors[5],
            this_screen_border = colors[5],
            foreground = colors[2],
            background = colors[1]
        ),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.WindowCount(font = "Noto Sans Bold", foreground = colors[2], background = colors[1], show_zero = True),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.CurrentLayout(font = "Noto Sans Bold", foreground = colors[2], background = colors[1]),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.CurrentScreen(font = "Noto Sans Bold", active_color = colors[2], inactive_color = colors[8], active_text = "active", inactive_text = "active"),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.Spacer(),
        widget.WindowName(font = "Noto Sans", fontsize = 14, foreground = colors[5], background = colors[1], width=bar.CALCULATED),
        widget.Spacer(),
        widget.Clock(font="Noto Sans", foreground = colors[2], background = colors[1], fontsize = 12, format="%Y-%m-%d %H:%M"),
    ]
    return widgets_list

def init_widgets_list_display3():
    widgets_list = [
        widget.GroupBox(
            font="FontAwesome",
            fontsize = 16,
            margin_y = 3,
            margin_x = 0,
            padding_y = 6,
            padding_x = 5,
            borderwidth = 0,
            disable_drag = True,
            active = colors[0],
            inactive = colors[8],
            rounded = False,
            highlight_method = "block",
            block_highlight_text_color = colors[7],
            this_current_screen_border = colors[5],
            this_screen_border = colors[5],
            foreground = colors[2],
            background = colors[1]
        ),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.WindowCount(font = "Noto Sans Bold", foreground = colors[2], background = colors[1], show_zero = True),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.CurrentLayout(font = "Noto Sans Bold", foreground = colors[2], background = colors[1]),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.CurrentScreen(font = "Noto Sans Bold", active_color = colors[2], inactive_color = colors[8], active_text = "active", inactive_text = "active"),
        widget.Sep(linewidth = 1, padding = 10, foreground = colors[2], background = colors[1]),
        widget.Spacer(),
        widget.WindowName(font = "Noto Sans", fontsize = 14, foreground = colors[5], background = colors[1], width=bar.CALCULATED),
        widget.Spacer(),
        widget.Clock(font="Noto Sans", foreground = colors[2], background = colors[1], fontsize = 12, format="%Y-%m-%d %H:%M"),
    ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list_display1()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list_display2()
    return widgets_screen2

def init_widgets_screen3():
    widgets_screen3 = init_widgets_list_display3()
    return widgets_screen3

def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26, opacity=1.0)), # Center screen
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26, opacity=1.0)), # Left screen
        Screen(top=bar.Bar(widgets=init_widgets_screen3(), size=26, opacity=1.0)), # Right screen
    ]

screens = init_screens()

# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

########################################################
############### assgin apps to groups ##################
########################################################
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    #####################################################################################
    ### Use xprop fo find  the value of WM_CLASS(STRING) -> First field is sufficient ###
    #####################################################################################
    d[group_names[0]] = ["Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
                        "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser",]
    d[group_names[2]] = ["Subl", "VSCodium", "Meld", "org.gnome.Meld", "Gitg", "Gittyup",
                        "subl", "vscodium", "meld", "org.gnome.meld", "gitg"]
    d[group_names[3]] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
                        "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt",]
    d[group_names[4]] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer", "Virt-manager",
                        "virtualbox manager", "virtualbox machine", "vmplayer", "virt-manager",]
    d[group_names[5]] = ["Vlc","vlc", "Mpv", "mpv" ]
    d[group_names[6]] = ["Steam",]
    d[group_names[7]] = ["Geary", "Mail", "Thunderbird", "Mailspring",
                        "geary", "mail", "thunderbird", "mailspring",]
    d[group_names[8]] = ["Skype", "skype"]
    d[group_names[9]] = ["Spotify",  "Clementine", "Audacious", "Sonixd",
                        "spotify", "clementine", "audacious", "sonixd",]
    ######################################################################################

    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            # client.group.cmd_toscreen(toggle=False)

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME

# @hook.subscribe.client_new
# def client_new(client):
#     if client.window.get_wm_class()[0] == 'brave-browser':
#         client.togroup("1")

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules, 
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='ArchLinux Logout'),
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Archlinux-tweak-tool.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='ulauncher'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='Archlinux-logout.py'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='xfce4-terminal'),
    Match(wm_class='Bitwarden'),
    Match(wm_class='xfce4-appfinder'),
],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
