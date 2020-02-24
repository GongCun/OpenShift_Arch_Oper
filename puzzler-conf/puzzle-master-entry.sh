#!/bin/sh
socat TCP-LISTEN:3000,reuseaddr,fork,keepalive,keepidle=1,keepintvl=1,keepcnt=6 \
exec:"/run-master.sh",nofork
