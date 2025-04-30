from libqtile import bar,widget,qtile,hook 
from groups import group_widgets1,group_widgets2,regenerate_group_widgets
from libqtile.lazy import lazy


displays = 1
f = open("/home/joel/.config/qtile/systeminfo/displays.txt","r")
displays = str(f.read())
if displays.isdigit():
    displays = int(displays)

if displays == 1:
    group_widgets2  = regenerate_group_widgets()



bars = []

bars.append(
    top=bar.Bar(
        [
            
        ],
        30,
        border_color = "#282738",
        border_width= [0,0,0,0],
        margin = [15,15,6,15],
        background="#00000000"
    )
)
