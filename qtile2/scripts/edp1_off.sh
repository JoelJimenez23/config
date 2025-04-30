#!/bin/bash
picom --config /home/joel/.config/picom/picom.conf &
nitrogen --restore

if xrandr | grep -q "HDMI-1 connected"; then
		xrandr --output HDMI-1 --mode 1920x1080
		xrandr --output eDP-1 --mode 1920x1080
		xrandr --output eDP-1 --off
		xbindkeys &
		xrandr --output HDMI-1 --left-of eDP-1
else
    echo "El monitor eDP-1 no está conectado. Ejecutar acción 2 aquí..."
		xbindkeys &
		xrandr --output HDMI-1 --off
		xrandr --output eDP-1 --mode 1920x1080
fi
