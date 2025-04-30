from libqtile import qtile,hook,widget
import os
import subprocess
from groups import group_widgets1,group_widgets2


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/scripts/edp1_off.sh'])
    subprocess.Popen([home + '/.config/qtile/scripts/p1com.sh'])

@hook.subscribe.startup_once
def autostart_once():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/scripts/edp1_off.sh'])


@hook.subscribe.screen_change
async def reconfigure_screens(event):
    home = os.path.expanduser('~')
    f = open(home+'/lunadepluton.txt')
    f.write("You and I")
    f.close()




floating_apps = [{'wmclass': 'pavucontrol'},{'wmclass': 'Blueman-manager'},{'wmclass': 'com.github.th_ch.youtube_music'},{'wmclass':'calendar_popup'}]
@hook.subscribe.client_new
def floating(client):
    for app in floating_apps:
        if client.window.get_wm_class()[1] == app['wmclass']:
            client.floating = True
