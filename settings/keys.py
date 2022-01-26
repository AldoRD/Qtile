from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"

keys = [
    Key(key[0], key[1], *key[2:])
    for key in [
        # Window Configs
        # Switch between windows in current stack panel
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),

        # Toggle floating
        ([mod, "shift"], "f", lazy.window.toggle_floating()),

        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        ([mod, "shift"], "h", lazy.layout.shuffle_left()),
        ([mod, "shift"], "l", lazy.layout.shuffle_right()),
        ([mod, "shift"], "j", lazy.layout.shuffle_down()),
        ([mod, "shift"], "k", lazy.layout.shuffle_up()),
        ([mod], "space", lazy.layout.next()),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        # ([mod, "control"], "h", lazy.layout.grow_left()),
        # ([mod, "control"], "l", lazy.layout.grow_right()),
        # ([mod, "control"], "j", lazy.layout.grow_down()),
        # ([mod, "control"], "k", lazy.layout.grow_up()),
        
        # Change window sizes (MonadTall)
        ([mod, "control"], "l", lazy.layout.grow()),
        ([mod, "control"], "h", lazy.layout.shrink()),
       
        # Toggle between different layouts as defined below
        ([mod], "Tab", lazy.next_layout()),
        ([mod, "shift"], "Tab", lazy.prev_layout()),
        
        # Kill window
        ([mod], "w", lazy.window.kill()),
        
        # Switch focus of monitors
        ([mod], "period", lazy.next_screen()),
        ([mod], "comma", lazy.prev_screen()),
        
        # Restart Qtile
        ([mod, "control"], "r", lazy.restart()),
        ([mod, "control"], "q", lazy.shutdown()),
        ([mod], "r", lazy.spawncmd()),
        
        # ------App Configs----------
        # Menu
        ([mod], "m", lazy.spawn("open_launcher menu")),
        
        # Window Nav
        ([mod, "shift"], "m", lazy.spawn("rofi -m -1 -show")),
        
        # Browser
        ([mod], "b", lazy.spawn("firefox")),
        
        # File Explorer
        ([mod], "e", lazy.spawn("kitty -e ranger")),
        
        # Terminal
        ([mod], "Return", lazy.spawn("kitty")),
        
        # Screenshot
        ([mod], "s", lazy.spawn("screenshot")),
        ([mod, "shift"], "s", lazy.spawn("screenshot window")),
        ([mod, "control", "shift"], "s", lazy.spawn("screenshot select")),

        # Extra menus
        ([mod, "mod1"], "l", lazy.spawn("open_launcher power")),
        ([mod ,"mod1"], "m", lazy.spawn("open_launcher music")), 
        
        # ------------ Hardware Configs ------------
        # Volume
        # ([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
        # ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
        # ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
        ([], "XF86AudioLowerVolume", lazy.spawn("changevolume down")),
        ([], "XF86AudioRaiseVolume", lazy.spawn("changevolume up")),
        ([], "XF86AudioMute", lazy.spawn("changevolume mute")),
        
        # Brightness
        ([], "XF86MonBrightnessUp", lazy.spawn("changebright up")),
        ([], "XF86MonBrightnessDown", lazy.spawn("changebright down")),
    ]
]
