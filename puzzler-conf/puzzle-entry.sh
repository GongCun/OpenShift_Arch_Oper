#!/bin/sh
socat TCP-LISTEN:3001,reuseaddr,fork,keepalive,keepidle=1,keepintvl=1,keepcnt=6 \
exec:"/run.sh",nofork
