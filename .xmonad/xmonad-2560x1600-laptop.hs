import XMonad
import XMonad.Actions.CopyWindow
import XMonad.Actions.WithAll
import XMonad.Actions.Promote
import XMonad.Actions.CycleWS
import XMonad.Actions.MouseResize
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.ManageDocks
import XMonad.Hooks.ManageHelpers
import XMonad.Hooks.EwmhDesktops
import XMonad.Util.Run
import XMonad.Util.SpawnOnce
import XMonad.Util.EZConfig
import XMonad.Util.NamedScratchpad
import XMonad.Layout.LayoutModifier
import XMonad.Layout.LimitWindows
import XMonad.Layout.MultiToggle
import XMonad.Layout.MultiToggle.Instances
import XMonad.Layout.NoBorders
import XMonad.Layout.PerWorkspace
import XMonad.Layout.Renamed
import XMonad.Layout.ResizableTile
import XMonad.Layout.SimplestFloat
import XMonad.Layout.Spacing
import XMonad.Layout.ThreeColumns
import XMonad.Layout.WindowArranger
import XMonad.Layout.WindowNavigation
import qualified Data.Map as M
import qualified XMonad.StackSet as W
import qualified XMonad.Layout.MultiToggle as MT
import qualified XMonad.Layout.ToggleLayouts as T
import System.Exit

myTerminal = "alacritty"
myFileManager = "thunar"
myBrowser = "firefox"
myEmailClient = "mailspring"
myCalendar = "gnome-calendar"
myPasswordManager = "bitwarden"
myVisualEditor = "subl"
myGitClient = "gitg"
myCalculator = "galculator"
myBorderWidth = 1
myModMask = mod4Mask
myWorkspaces = ["1", "2", "3", "4", "5"]
myNormalBorderColor = "#000000"
myFocusedBorderColor = "#00ff00"

rect = W.RationalRect l t w h
               where
                 h = 0.25
                 w = 0.25
                 t = (1.0 -h) /2
                 l = (1.0 -w) /2 


myFocusFollowsMouse = True
myClickJustFocuses = False

windowCount = gets $ Just . show . length . W.integrate' . W.stack . W.workspace . W.current . windowset

applySpacing i = spacingRaw True (Border i i i i) True (Border i i i i) True

tall     = renamed [Replace "tall"] $ avoidStruts $ smartBorders $ windowNavigation $ limitWindows 5 $ applySpacing 4 $ ResizableTall 1 (3/100) (1/2) []
threeCol = renamed [Replace "threeCol"] $ avoidStruts $ smartBorders $ windowNavigation $ limitWindows 7 $ ThreeCol 1 (3/100) (1/2)
monocle  = renamed [Replace "monocle"] $ avoidStruts $ smartBorders $ windowNavigation $ limitWindows 20 Full
floats   = renamed [Replace "floats"] $ avoidStruts $ smartBorders $ limitWindows 20 simplestFloat
full     = renamed [Replace "full"] $ smartBorders $ windowNavigation $ limitWindows 1 Full

myLayoutHook = mouseResize $ windowArrange $ T.toggleLayouts floats
               $ onWorkspaces ["1"] full $ mkToggle (NBFULL ?? NOBORDERS ?? EOT) myDefaultLayout
             where
               myDefaultLayout = withBorder myBorderWidth tall
                                 ||| noBorders monocle
                                 ||| floats
                                 ||| threeCol
                                 ||| noBorders full

myManageHook = composeAll
     [ className =? "confirm"         --> doFloat
     , className =? "file_progress"   --> doFloat
     , className =? "dialog"          --> doFloat
     , className =? "download"        --> doFloat
     , className =? "error"           --> doFloat
     , className =? "Gimp"            --> doFloat
     , className =? "notification"    --> doFloat
     , className =? "pinentry-gtk-2"  --> doFloat
     , className =? "splash"          --> doFloat
     , className =? "toolbar"         --> doFloat
     , className =? "Bitwarden"       --> doFloat
     , className =? "Galculator"      --> doRectFloat rect
     , (className =? "firefox" <&&> resource =? "Dialog") --> doFloat
     , isFullscreen -->  doFullFloat
     ]

myStartupHook = do
    spawnOnce "lxsession &"
    spawnOnce "~/.fehbg &"
    spawnOnce "picom &"
    spawnOnce "volumeicon &"
    spawnOnce "nm-applet &"
    spawnOnce "cbatticon -i notification &"
    spawnOnce "dunst &"
    spawnOnce "xfce4-power-manager --daemon"
    spawnOnce "trayer --edge top --align right --widthtype request --padding 6 --SetDockType true --SetPartialStrut true --expand true --monitor 0 --transparent true --alpha 0 --tint 0x282c34  --height 22 &"

myKeybindings = [
-- general keybinds
    ("M-C-r", spawn "xmonad --recompile"),
    ("M-r", spawn "xmonad --restart"),
    ("M-q", kill1),
    ("M-C-q", killAll),
    ("M-S-l", io exitSuccess),
-- app hotkeys
    ("M-<Return>", spawn (myTerminal)),
    ("M-<Space>", spawn "dmenu_run -i -p \"Run:\""),
    ("M-M1-<Space>", spawn "~/.xmenu.sh"),
    ("M-t", spawn (myFileManager)),
    ("M-a", spawn (myCalculator)),
    ("M-s", spawn (myVisualEditor)),
    ("M-e", spawn (myEmailClient)),
    ("M-c", spawn (myCalendar)),
    ("M-g", spawn (myGitClient)),
    ("M-w", spawn (myPasswordManager)),
    ("M-b", spawn (myBrowser)),
    ("M-S-b", spawn (myBrowser ++ " -private-window")),
    ("M-`", spawn "dunstctl history-pop"),
    ("M-v", spawn "notify-send \"$(date +%H:%M:%S)\""),
-- window manipulation (move/resize/shift)
    ("M-S-m", promote),
    ("M-S-j", windows W.swapDown),
    ("M-S-k", windows W.swapUp),
    ("M-C-h", sendMessage Shrink),
    ("M-C-j", sendMessage MirrorShrink),
    ("M-C-k", sendMessage MirrorExpand),
    ("M-C-l", sendMessage Expand),
    ("M-S-.", shiftToNext >> nextWS),
    ("M-S-,", shiftToPrev >> prevWS),
-- change focused screen
    ("M-.", nextScreen),
    ("M-,", prevScreen),
-- change layout
    ("M-<Tab>", sendMessage NextLayout),
-- toggle fullscreen
    ("M-f", sendMessage (MT.Toggle NBFULL) >> sendMessage ToggleStruts),
-- float/tile windows
    ("M-S-f", withFocused toggleFloat),
    ("M-S-t", sinkAll)
    ] where
            toggleFloat w = windows (\s -> if M.member w (W.floating s)
                            then W.sink w s
                            else (W.float w rect s))

main = do
    xmproc <- spawnPipe "xmobar -x 0 /home/patryk/.config/xmobar/1920x1080rc"
    xmonad $ docks $ ewmh def {
        manageHook = myManageHook <+> manageDocks,
        terminal = myTerminal,
        workspaces = myWorkspaces,
        borderWidth = myBorderWidth,
        modMask = myModMask,
        normalBorderColor = myNormalBorderColor,
        focusedBorderColor = myFocusedBorderColor,
        layoutHook = myLayoutHook,
        startupHook = myStartupHook,
        logHook = dynamicLogWithPP $ namedScratchpadFilterOutWorkspacePP $ xmobarPP
            { ppOutput = \x -> hPutStrLn xmproc x
            , ppCurrent = xmobarColor "#00ff00" ""                -- Current workspace
            , ppVisible = xmobarColor "#e5951d" ""                -- Visible but not current workspace
            , ppHidden = xmobarColor "#82aaff" ""                 -- Hidden workspaces
            , ppHiddenNoWindows = xmobarColor "#c792ea" ""        -- Hidden workspaces (no windows)
            , ppTitle = xmobarColor "#b3afc2" "" . shorten 80     -- Title of active window
            , ppSep =  "<fc=#666666> <fn=1>|</fn> </fc>"          -- Separator character
            , ppUrgent = xmobarColor "#c45500" "" . wrap "!" "!"  -- Urgent workspace
            , ppExtras  = [windowCount]                           -- # of windows current workspace
            , ppOrder  = \(ws:l:t:ex) -> [ws,l]++ex++[t]          -- order of things in xmobar
            }
} `additionalKeysP` myKeybindings
