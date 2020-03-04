#!/bin/sh

echo "Content-type: text/html"
echo ""

cat <<\EOF
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Puzzle Brain</title>
</head>
<body>
<h1>Puzzle Brain</h1>
<img src="shapes-solve.png" alt="shapes-solve">
EOF

if expr "${HTTP_USER_AGENT}" : ".*Firefox.*" >/dev/null
then
    echo '<form action="/cgi-bin/wait.cgi" method=get>'
else
    echo '<form action="/cgi-bin/process.cgi" method=get>'
fi

cat <<\EOF
<br><input type="submit" value="RUN!">
</form>
</body>
</html>
EOF


