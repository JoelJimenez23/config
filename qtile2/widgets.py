from libqtile import widget,bar,qtile





def get_text_box(text,fontsize=None,padding=None,foreground=None,background=None,font=None):
    text_box = widget.TextBox(text=text)
    if fontsize:
        text_box.fontsize = fontsize
    if padding:
        text_box.padding = padding
    if foreground:
        text_box.foreground = foreground
    if background:
        text_box.background = background
    if font:
        text_box.font = font
    return text_box



def get_spacer(length,background=None):
    spacer = widget.Spacer(length=length)
    if(background):
        spacer.background = background
    return spacer


GroupBoxMain = widget.GroupBox(
    padding=10,
    visible_groups=["1","2","3","4","5","6","7","8","9","0"],
    highlight_method="text",
    block_highlight_text_color="#d28f7f",
    urgent_alert_method='text',
    urgent_text="#ffffff",
    active="#f9c3c2",
    inactive="#000000",
    #this_current_screen_border="#965FD4",
    this_current_screen_border="#9dced3",
    disable_drag=True,
)


def get_groupbox(padding=None,
                 visible_groups=None,
                 highlight_method=None,
                 block_highlight_text_color=None,
                 urgent_alert_method=None,
                 urgent_text=None,
                 active=None,
                 inactive=None,
                 this_current_screen_border=None,
                 disable_drag=None):

    groupbox = widget.GroupBox()
    if(padding):
        groupbox.padding = padding
    if(visible_groups):
        groupbox.visible_groups = visible_groups
    if(highlight_method):
        groupbox.highlight_method = highlight_method
    if(block_highlight_text_color):
        groupbox.highlight_method = highlight_method
    if(urgent_alert_method):
        groupbox.urgent_alert_method = urgent_alert_method
    if(urgent_text):
        groupbox.urgent_text = urgent_text
    if(active):
        groupbox.active = active
    if(inactive):
        groupbox.inactive = inactive
    if(this_current_screen_border):
        groupbox.this_current_screen_border = this_current_screen_border
    if(disable_drag):
        groupbox.disable_drag = disable_drag
    return groupbox

def get_volume(foreground=None,background=None,font=None,mute_format=None,unmute_format=None):
    volume = widget.Volume()
    volume.hide_crash = True
    volume.mute_command=['amixer','-q','set','Master','toggle']
    volume.update_interval=0.1
    volume.get_volume_command = "pactl get-sink-volume @DEFAULT_SINK@"
    volume.mute_command="pactl set-sink-mute @DEFAULT_SINK@ toggle"
    volume.volume_up_command="pactl set-sink-volume @DEFAULT_SINK@ +5%"
    volume.volume_down_command="pactl set-sink-volume @DEFAULT_SINK@ -5%"
    volume.theme_path=None
    volume.fontsize = 13
    volume.get_volume_command = "~/.config/qtile/volume.sh"


    if foreground:
        volume.foreground = foreground
    if background:
        volume.background = background
    if font:
        volume.font = font 
    if mute_format:
        volume.mute_format = mute_format
    if unmute_format:
        volume.unmute_format = unmute_format
    return volume


def get_battery(fontsize=None,format=None,low_foreground=None,foreground=None,font=None,background=None,padding=None):
    battery = widget.Battery()
    battery.fontsize = 13
    if fontsize:
        battery.fontsize = fontsize
    if format:
        battery.format = format
    if low_foreground:
        battery.low_foreground = low_foreground
    if foreground:
        battery.foreground = foreground
    if font:
        battery.font = font
    if background:
        battery.background = background
    if padding:
        battery.padding = padding
    return battery 



def get_image(filename,background=None):
    image = widget.Image(filename=filename)
    if background:
        image.background = background
    return image


clock_format = "%H:%M"
def toggle_clock_format():
    global clock_format
    # Alternar entre el formato de hora y el formato de fecha
    if clock_format == "%H:%M":
        clock_format = "%d/%m/%Y"
    else:
        clock_format = "%H:%M"
    # Actualizar el widget manualmente
    qtile.widgets_map['clock'].format = clock_format
    qtile.widgets_map['clock'].tick()


def get_clock(format=None,foreground=None,background=None,font=None):
    clock = widget.Clock()
    if format:
        clock.format = format or "%H:%M"
    if foreground:
        clock.foreground = foreground
    if background:
        clock.background = background
    if font:
        clock.font = font

    clock.mouse_callbacks={"Button1": toggle_clock_format}

    return clock


def get_window_name(transparent):
    if(transparent == True):
        return widget.WindowName(
            width=350,
            fmt=" <i><b>{}</b></i>",
            scroll=True,
            scroll_interval=0.02,
            scroll_delay=1,
            background="#00000000",
            foregroun="#11111111"
        ) 
    else:
        return widget.WindowName(
            width=350,
            fmt=" <i><b>{}</b></i>",
            scroll=True,
            scroll_interval=0.02,
            scroll_delay=1,
        ) 


import subprocess
from libqtile.widget import GenPollText


calendar_process = None  # Variable global para manejar el proceso del calendario

def show_calendar():
    global calendar_process
    # Si ya hay un calendario abierto, no hace nada
    if calendar_process and calendar_process.poll() is None:
        return
    # Abrir el calendario en modo flotante
    calendar_process = subprocess.Popen([
        "alacritty",
        "--class", "calendar_popup",
        "-o", "window.dimensions.columns=50",
        "-o", "window.dimensions.lines=20",
        "-e", "khal", "interactive"
    ])

def close_calendar():
    global calendar_process
    if calendar_process and calendar_process.poll() is None:
        calendar_process.terminate()
        calendar_process = None

def get_calendar(foreground=None, background=None, font=None):
    return GenPollText(
        func=lambda: subprocess.check_output(["date", "+%d/%m/%Y"]).decode("utf-8"),
        update_interval=60,
        foreground=foreground or "9dced3",
        background=background or "#282738",
        font=font or "Martian Mono Nerd Font Bold",
        mouse_callbacks={
            "Button1": show_calendar,    # Mostrar calendario al presionar
            "ButtonRelease1": close_calendar  # Cerrar calendario al soltar
        },
    )



