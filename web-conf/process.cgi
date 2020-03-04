#!/bin/bash
dir=`dirname $0`
dir=`(cd $dir | pwd -P)`
cd $dir

echo "Content-type: text/html"
echo ""

#echo "<html><body><pre>"
echo "<html><body>"
cur=$SECONDS
str=`echo "hello" | ncat ${PUZZLE_MASTER} 3000 2>&1`
if [ "$str" = "Not run" ]; then
    declare -i count=`./count-psql.py | sed 's/(\(.*\),)/\1/'`
    if [ $count -le 0 ]; then
		rm -rf /data/solution.*
		if  echo "run-puzzle" | ncat ${PUZZLE_MASTER} 3000; then
			echo "<br>elapsed $((SECONDS-cur)) sec<br><br>"
			echo
	        echo "Copying to PostgresSQL database<br>"
	        cat /data/solution.* | grep -v 'No Solutions' | grep -v grep | \
	            awk 'NR%6 != 0{T=(T""$0); next}{print T; T=""}' | tr -d '[[:blank:]]' | ./copy-psql.py
	        echo "<br><br>"
		fi
    fi

    echo
    echo '<form action="/cgi-bin/web-psql.cgi" method=get>'
    echo 'Display <input name=count size=2> solutions'
    echo '<input type="submit" value="submit">'
else
    echo "Resource busy, retry later!"
fi
#echo "</pre></body></html>"
echo "</body></html>"
