#!/bin/bash

MUTE=$(pactl get-sink-mute @DEFAULT_SINK@ | awk '{print $2}')
VOLUME=$(pactl get-sink-volume @DEFAULT_SINK@ | grep -o -m 1 '[0-9]\+%')

if [ "$MUTE" = "yes" ]; then
    echo "Mute"
else
    echo "$VOLUME"
fi

