import os

from libqtile import widget
from .theme import colors
from libqtile import qtile

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


def base(fg="text", bg="dark"):
    return {"foreground": colors[fg], "background": colors[bg]}


def separator(size=5):
    return widget.Sep(
        linewidth=0,
        foreground="#00000000",
        background="#00000000",
        padding=size,
        size_percent=40,
    )


def espacer(size=2):
    return widget.Sep(
        background=colors["dark"],
        foreground="#00000000",
        linewidth=0,
        padding=size,
        size_percent=40,
    )


def msj():
    qtile.cmd_spawn("notify-send 'Nothing assigned.'")


def icon(fg="text", bg="dark", fontsize=16, text="?", func=msj):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=4,
        mouse_callbacks={"Button1": func},
    )


def powerline(positon=0):
    if positon == 0:
        icono = "\uE0B6"
    else:
        icono = "\uE0B4"
    return widget.TextBox(
        text=icono,
        font="mononoki Nerd Font",
        foreground=colors["dark"],
        background="#00000000",
        fontsize=29,
        padding=0,
    )


def workspaces():
    return [
        powerline(),
        widget.GroupBox(
            **base(fg="light"),
            font="UbuntuMono Nerd Font",
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=6,
            padding_x=5,
            borderwidth=4,
            active=colors["active"],
            inactive=colors["inactive"],
            rounded=False,
            highlight_method="block",
            urgent_alert_method="block",
            urgent_border=colors["urgent"],
            this_current_screen_border=colors["focus"],
            this_screen_border=colors["grey"],
            other_current_screen_border=colors["dark"],
            other_screen_border=colors["dark"],
            disable_drag=True,
        ),
        powerline(1),
    ]


def open_pavu():
    qtile.cmd_spawn("pavucontrol")


def updates_cmd():
    qtile.cmd_spawn("kitty -e sudo pacman -Syu")


def open_tasks():
    qtile.cmd_spawn("kitty -e htop")


def open_power():
    qtile.cmd_spawn("open_launcher power")


def monitors():
    return [
        powerline(),
        icon(fg="color4", bg="dark", text="墳", fontsize=18, func=open_pavu),
        espacer(2),
        widget.PulseVolume(
            **base(fg="color4", bg="dark"), fontsize=18, limit_max_volume=True
        ),
        espacer(8),
        icon(fg="color3", bg="dark", text="", fontsize=18),
        espacer(2),
        widget.Battery(
            **base(fg="color3", bg="dark"), format="{percent:2.0%}", fontsize=18
        ),
        espacer(8),
        icon(fg="color6", bg="dark", text="滛", fontsize=18),
        espacer(2),
        widget.Backlight(
            **base(fg="color6", bg="dark"), backlight_name="amdgpu_bl0", fontsize=18
        ),
        powerline(1),
    ]


primary_widgets = [
    *workspaces(),
    separator(),
    powerline(),
    widget.CurrentLayoutIcon(
        **base(fg="color8", bg="dark"),
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        scale=0.65,
    ),
    widget.CurrentLayout(**base(fg="color8", bg="dark"), padding=5, fontsize=18),
    powerline(1),
    widget.Spacer(),
    powerline(),
    icon(fg="color6", bg="dark", text=" ", fontsize=18, func=open_tasks),
    espacer(0),
    widget.Memory(**base(fg="color6", bg="dark"), format="{MemUsed: .0f}{mm}"),
    powerline(1),
    separator(),
    powerline(),
    icon(fg="color5", bg="dark", text=" "),  # Icon: nf-fa-feed
    widget.Wlan(
        **base(fg="color5", bg="dark"),
        fontsize=16,
        format="{essid}",
        interface="wlp2s0",
    ),
    powerline(1),
    separator(),
    *monitors(),
    separator(),
    powerline(),
    icon(fg="color7", bg="dark", fontsize=17, text=" "),  # Icon: nf-mdi-calendar_clock
    widget.Clock(
        **base(fg="color7", bg="dark"), format="%d-%m-%Y | %H:%M", fontsize=16
    ),
    powerline(1),
    widget.Systray(background="#00000000", padding=4),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline(),
    widget.CurrentLayoutIcon(
        **base(fg="color8", bg="dark"),
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        scale=0.65,
    ),
    widget.CurrentLayout(**base(fg="color8", bg="dark"), padding=5, fontsize=18),
    powerline(1),
    widget.Spacer(),
    *monitors(),
    separator(),
    powerline(),
    icon(fg="color7", bg="dark", fontsize=17, text=" "),  # Icon: nf-mdi-calendar_clock
    widget.Clock(
        **base(fg="color7", bg="dark"), format="%d-%m-%Y | %H:%M ", fontsize=16
    ),
    powerline(1),
    separator(),
]

widget_defaults = {
    "font": "UbuntuMono Nerd Font Bold",
    "fontsize": 14,
    "padding": 1,
}
extension_defaults = widget_defaults.copy()
