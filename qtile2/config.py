from groups  import groups,go_to_group,go_to_group_and_move_window
from layouts import layouts,floating_layout
from screens import screens
from hooks import autostart,floating
from keys import keys,mouse
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"




