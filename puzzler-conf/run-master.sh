#!/bin/sh
exec 100>/tmp/run.lock || exit 1

if ! flock -n -x 100 ; then
    echo "Resource busy, wait and try again!"
    exit 1
fi

read line
if [ "$line" = "run-puzzle" ]; then
    #echo "Start running"
    (cd /data; ../puzzler -m -b8 -s ${PUZZLE_CLUSTER} -p 3001; rm -rf ./*) >/dev/null 2>&1
    echo "Completed"
else
    echo "Not run"
fi

