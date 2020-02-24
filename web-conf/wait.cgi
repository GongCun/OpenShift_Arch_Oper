#!/usr/bin/ksh

dir=`dirname $0`
dir=`(cd $dir; pwd -P)`
cd $dir

f() {
    ./process.cgi >/tmp/process.txt
    kill -TERM $1
}

output() {

    cat /tmp/process.txt
    #print -n "$boundary"
    print -n $end_of_data

    wait
    exit
}

f $$ &
pid=$!

trap 'output' TERM


boundary="\n--End\n"
end_of_data="\n--End--\n"
#print -n "${SERVER_PROTOCOL} 200 OK\n"
#print -n "Server: ${SERVER_SOFTWARE}\n"



print -n "Content-type: multipart/x-mixed-replace;boundary=End\n\n"
print -n "$boundary"

integer i=0
set -A x '|' '/' '-' '\\'
while :
do
    let 'j = i % 4'
    print -n "Content-type: text/html; charset=utf-8\n\n"
    print -n "waiting ${x[$j]}\n"
    print -n "$boundary"
    let 'i = i + 1'
    sleep 1
done
