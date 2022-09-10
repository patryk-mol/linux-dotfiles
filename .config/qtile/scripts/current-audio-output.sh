#!/bin/sh

activeSink=$(pacmd list-sinks | grep "* index" | cut -d ':' -f 2 | sed -r 's/\s+//g')
case $activeSink in
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
