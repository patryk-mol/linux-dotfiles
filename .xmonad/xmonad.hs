import XMonad
import XMonad.Actions.CopyWindow
import XMonad.Actions.WithAll
import XMonad.Actions.Promote
import XMonad.Hooks.ManageDocks
import XMonad.Util.Run
import XMonad.Util.SpawnOnce
import XMonad.Util.EZConfig
import XMonad.Layout.LayoutModifier
import XMonad.Layout.Spacing
import qualified XMonad.StackSet as W
import System.Exit

myTerminal = "alacritty"
myBorderWidth = 1
mySpacing = 4
myModMask = mod4Mask
myWorkspaces = ["1", "2", "3"]
myNormalBorderColor = "#bbbbbb"
myFocusedBorderColor = "#00ff00"

myFocusFollowsMouse :: Bool
myFocusFollowsMouse = True
myClickJustFocuses :: Bool
myClickJustFocuses = False

applySpacing :: Integer -> l a -> XMonad.Layout.LayoutModifier.ModifiedLayout Spacing l a
applySpacing i = spacingRaw False (Border i i i i) True (Border i i i i) True

myLayout = avoidStruts (tiled ||| Mirror tiled ||| Full)
  where
     tiled   = applySpacing 4 $ Tall nmaster delta ratio
     nmaster = 1
     ratio   = 1/2
     delta   = 3/100

myStartupHook = do
    spawnOnce "xrandr -s 1600x900"
    spawnOnce "nitrogen --restore &"
    spawnOnce "picom &"

myKeybindings = [
    ("M-C-r", spawn "xmonad --recompile"),
    ("M-r", spawn "xmonad --restart"),
    ("M-q", kill1),
    ("M-C-q", killAll),
    ("M-S-l", io exitSuccess),
    ("M-<Return>", spawn (myTerminal)),
    ("M-<Space>", spawn "dmenu_run -i -p \"Run: \""),
    ("M-S-m", promote),
    ("M-S-j", windows W.swapDown),
    ("M-S-k", windows W.swapUp)
    ]

main = do
   xmproc <- spawnPipe "xmobar -x 0 /home/xxx/.config/xmobar/xmobarrc"
   xmonad $ docks defaults

defaults = def {
    terminal = myTerminal,
    workspaces = myWorkspaces,
    borderWidth = myBorderWidth,
    modMask = myModMask,
    normalBorderColor = myNormalBorderColor,
    focusedBorderColor = myFocusedBorderColor,
    layoutHook = myLayout,
    startupHook = myStartupHook
} `additionalKeysP` myKeybindings
