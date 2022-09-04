#!/bin/sh

numberOfDevices=$(pacmd list-sinks | grep index | wc -l)
activeSink=$(pacmd list-sinks | grep "* index" | cut -d ':' -f 2 | sed -r 's/\s+//g')
sinkToActivate=$((activeSink+1))

if [ $sinkToActivate -ge $numberOfDevices ]; then
    sinkToActivate=0
fi

pacmd set-default-sink $sinkToActivate

case $sinkToActivate in
    0)
        printf ""
        ;;
    1)
        printf ""
        ;;
    *)
        printf "?"
        ;;
esac

