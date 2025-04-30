from libqtile.config import Screen
from libqtile import bar, widget, qtile, hook
from groups import group_widgets2
from libqtile.log_utils import logger
from libqtile.lazy import lazy
from widgets import get_text_box,get_groupbox,get_volume,get_battery,get_window_name,get_spacer,get_clock,get_image,get_calendar



def set_groupbox(group_widgets2):
    displays = 1
    f = open("/home/joel/.config/qtile/systeminfo/displays.txt","r")
    displays = str(f.read())
    if displays.isdigit():
        displays = int(displays)
    
    if displays == 1:
        arr = ["1","2","3","4","5","6","7","8","9","0","q","w","e","a","s","d","f"]
        group_widgets2 = [get_groupbox(10,arr,"text","#d28f7f","text","#ffffff","#f9c3c2","#000000","#9dced3",True)]

    return group_widgets2


gb_main_arr = ["1","2","3","4","5","6","7","8","9","0"]



color1 = "#282738"
color2 = "#9dced3"
color3 = "#ca7697"

screens = [
    Screen(
        top=bar.Bar(
            [
                get_spacer(10),
                widget.Prompt(),
                get_window_name(False),
                get_spacer(bar.STRETCH),
                *set_groupbox(group_widgets2),
                get_spacer(bar.STRETCH),
                get_spacer(100),
                get_text_box("",45,-6.5,"#9dced3","#00000000"),
                get_volume("#282738","#9dced3","Martian Mono Nerd Font Bold","     ","    {volume}%"),
                get_text_box("",45,-6.5,"#ca7697","#9dced3"), 
                get_image('/home/joel/.config/qtile/icons/bateria-llena.png',background="#ca7697"),
                get_battery("13","  {percent:2.0%}  ","#ff0000","#282738","Martian Mono Nerd Font Bold","#ca7697",-5),
                get_text_box("",45,-6.5,"#282738","#ca7697"),
                get_text_box(" ",foreground="#9dced3",background="#282738",font="Martian Mono Nerd Font Bold"),
                get_clock(format="%H:%M",foreground="9dced3",background="#282738",font="Martian Mono Nerd Font Bold"),
                get_spacer(18,background="#282738")
            ],
            30,
            border_color = "#282738",
            border_width = [0,0,0,0],
            margin = [15,15,0,15],
            background="#00000000"
        ),
    ),
    Screen(
        top=bar.Bar( #pantalla principal
           [   
                get_spacer(10),
                widget.Prompt(),
                get_window_name(True),
                get_spacer(bar.STRETCH),
                get_groupbox(10,gb_main_arr,"text","#d28f7f","text","#ffffff","#f9c3c2","#000000","#9dced3",True),
                get_spacer(bar.STRETCH),
                get_spacer(100),
                get_text_box("",45,-6.5,color2,"#00000000"),
                get_volume(color1,color2,"0xProtoNerdFont Regular"," ","   {volume}%"),
                get_text_box("",45,-6.5,color3,color2), 
                get_image('/home/joel/.config/qtile/icons/bateria-llena.png',background=color3),
                get_battery("13"," {percent:2.0%} ","#ff0000","#282738","Martian Mono Nerd Font Bold","#ca7697",-5),
                get_text_box("",45,-6.5,color1,color3),
                get_text_box(" ",foreground=color2,background=color1,font="Martian Mono Nerd Font Bold"),
                get_clock(format="%I:%M %p",foreground=color2,background=color1,font="Martian Mono Nerd Font Bold"),
                get_spacer(18,background="#282738")
            ],
            30,
            border_color='#282738',
            border_width = [0,0,0,0],
            margin=[15,15,0,15],
            background="#00000000"
        ),
    )
]
#d28f7f


@hook.subscribe.startup
def reconfigure_screens1():
    with open("/home/joel/.config/qtile/systeminfo/displays.txt", "w") as f:
        f.write(str(len(qtile.screens)))






