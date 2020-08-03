#   __                _     _
#  / _|_   _____ __ _| | __| | ___ _ __ __ _ _ __
# | |_\ \ / / __/ _` | |/ _` |/ _ \ '__/ _` | '_ \
# |  _|\ V / (_| (_| | | (_| |  __/ | | (_| | | | |
# |_|   \_/ \___\__,_|_|\__,_|\___|_|  \__,_|_| |_|
#
# My github: https://github.com/fvcalderan/

# Original license text:
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
from typing import List

# Set of colors
bar_bg = "1E1F29"
bar_fg = "FFFFFF"

# Set of variables
mod = "mod1"
term_emu = "termite"
app_launcher = f"dmenu_run -i -p 'exec:' -nb '#{bar_bg}' -nf '#{bar_fg}' -sb '#{bar_fg}' -sf '#{bar_bg}'"
browser = "firefox"
file_browser_gui = "pcmanfm"
file_browser_term = term_emu + " -e vifmrun"
text_editor = term_emu + " -e nvim"
screenshot = "scrot_select"
python_shell = term_emu + " -e 'python3 -q'"
# used when connecting extra monitor or keyboard.
reload_screen_kbd = term_emu + " -e reload_screen_kbd"


def spawn_python():
    return lazy.spawn(term_emu + " -e python3")


keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),

    # Kill the current window
    Key([mod], "q", lazy.window.kill()),

    # Toggle floating mode for the current window
    Key([mod], "f", lazy.window.toggle_floating()),

    # Set of shortcuts
    Key([mod], "Return", lazy.spawn(term_emu)),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "r", lazy.spawn(reload_screen_kbd)),
    Key([mod, "control"], "c", lazy.shutdown()),
    Key([mod], "p", lazy.spawn(app_launcher)),
    Key([mod, "shift"], "Return", lazy.spawn(browser)),
    Key([mod], "m", lazy.spawn(file_browser_term)),
    Key([mod, "shift"], "m", lazy.spawn(file_browser_gui)),
    Key([mod], "v", lazy.spawn(text_editor)),
    Key([mod], "Print", lazy.spawn(screenshot)),
    Key([mod], "y", lazy.spawn(python_shell)),

]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.MonadTall(margin=4, border_focus=bar_fg, border_normal=bar_bg),
    layout.Max(),
]

widget_defaults = dict(
    font='mono',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screen1_config = Screen(
    top=bar.Bar(
        [
            widget.GroupBox(active=bar_fg, inactive=bar_fg, hide_unused=True, this_screen_border=bar_fg,
                            this_current_screen_border=bar_fg, borderwidth=3, highlight_method='line',
                            highlight_color=[bar_bg, bar_bg]),
            widget.WindowName(foreground=bar_bg),
            widget.Systray(),
            widget.Sep(),
            widget.Battery(format=' {char}{percent:1.0%} '),
            widget.Sep(),
            widget.Clock(format=' %m/%d %I:%M '),
        ],
        21,
        background=bar_bg,
    ),
)

screen2_config = Screen(
    top=bar.Bar(
        [
            widget.GroupBox(active=bar_fg, inactive=bar_fg, hide_unused=True, this_screen_border=bar_fg,
                            this_current_screen_border=bar_fg, borderwidth=3, highlight_method='line',
                            highlight_color=[bar_bg, bar_bg]),
            widget.WindowName(foreground=bar_bg),
            widget.Systray(),
            widget.Sep(),
            widget.Battery(format=' {char}{percent:1.0%} '),
            widget.Sep(),
            widget.Clock(format=' %m/%d %I:%M '),
        ],
        21,
        background=bar_bg,
    ),
)

screens = [
    screen1_config,
    screen2_config
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'gxmessage'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], border_focus=bar_fg, border_normal=bar_bg)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
# wmname = "qtile"
