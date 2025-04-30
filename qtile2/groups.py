from libqtile.config import Group,ScratchPad,DropDown
from libqtile import qtile
from libqtile import layout
from libqtile import widget
from libqtile.lazy import lazy

groups = [
     Group(name="1",label="●", screen_affinity=0),
     Group(name="2",label="●", screen_affinity=0),
     Group(name="3",label="●", screen_affinity=0),
     Group(name="4",label="●", screen_affinity=0),
     Group(name="5",label="●", screen_affinity=0),
     Group(name="6",label="●", screen_affinity=0),
     Group(name="7",label="●", screen_affinity=0),
     Group(name="8",label="●", screen_affinity=0),
     Group(name="9",label="●", screen_affinity=0),
     Group(name="0",label="●", screen_affinity=0),
     Group(name="q",label="●", screen_affinity=1),
     Group(name="w",label="●", screen_affinity=1),
     Group(name="e",label="●", screen_affinity=1),
     Group(name="a",label="●", screen_affinity=1),
     Group(name="s",label="●", screen_affinity=1),
     Group(name="d",label="●", screen_affinity=1),
     Group(name="f",label="●", screen_affinity=1,layouts=[layout.TreeTab()]),
]


group_images = { 
    "1":"/home/joel/.config/qtile/icons/firefox.png",
    "2":"/home/joel/.config/qtile/icons/terminal.png",
    "3":"/home/joel/.config/qtile/icons/terminal.png",
    "4":"/home/joel/.config/qtile/icons/terminal.png",
    "5":"/home/joel/.config/qtile/icons/discord.png",
    "6":"/home/joel/.config/qtile/icons/zoom.png",
    "7":"/home/joel/.config/qtile/icons/terminal.png",
    "8":"/home/joel/.config/qtile/icons/terminal.png",
    "9":"/home/joel/.config/qtile/icons/firefox.png",
    "0":"/home/joel/.config/qtile/icons/firefox.png",
    "q":"/home/joel/.config/qtile/icons/firefox.png",
    "w":"/home/joel/.config/qtile/icons/discord.png",
    "e":"/home/joel/.config/qtile/icons/spotify.png",
    "a":"/home/joel/.config/qtile/icons/open-folder.png",
    "s":"/home/joel/.config/qtile/icons/android.png",
    "d":"/home/joel/.config/qtile/icons/firefox.png",
    "f":"/home/joel/.config/qtile/icons/rubbish.png"

}

def create_group_image(group_name):
    return widget.Image(
        filename=group_images.get(group_name, "/home/joel/.config/qtile/icons/blank.png"),
        mouse_callbacks={
            "Button1": lazy.group[group_name].toscreen(),  # Cambiar al grupo al hacer clic
        },
        margin=3,
        draw_center=True,
        width=32,  # Tamaño de la imagen
        height=32,
        background="#00000000",  # Fondo negro para el widget

    )

group_widgets1 = [create_group_image(group.name) for group in groups if group.name.isdigit()]
group_widgets2 = [create_group_image(group.name) for group in groups if group.name.isdigit() == False]


def regenerate_group_widgets():
    return [create_group_image(group.name) for group in groups]




def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in '1234567890':
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
    return _inner


# Función para ir a un grupo y mover la ventana
def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return

        if name in "1234567890":
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
        else:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()

    return _inner
