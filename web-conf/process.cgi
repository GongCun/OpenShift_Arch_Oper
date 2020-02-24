#!/bin/bash

echo "Content-type: text/html"
echo ""

echo "<html><body><pre>"
cur=$SECONDS
str=`echo "hello" | ncat ${PUZZLE_MASTER} 3000 2>&1`
if [ "$str" = "Not run" ]; then
	rm -rf /data/solution.*
	if  echo "run-puzzle" | ncat ${PUZZLE_MASTER} 3000; then
		echo "elapsed $((SECONDS-cur)) sec"
		echo
		n=`grep -c '^$' /data/solution.* | awk -F: '{sum+=$2}END{print sum}'`
		echo "Total solutions is $n"
		echo
		echo "Some solutions:"
		echo
		ls -S1 /data/solution.* | {
			i=0
			while read line && [ $i -lt 5 ]; do
			    head -5 $line
			    echo
			    ((i = i + 1))
			done
		}
	fi
else
    echo "Resource busy, retry later!"
fi
echo "</pre></body></html>"
