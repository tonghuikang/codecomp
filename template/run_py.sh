[[ ! -f $1.py ]] && echo "$1.py not found" && exit 1; 

for TEST_CASE in $1*;
	do
	[[ $TEST_CASE == *.* ]] && continue; 
    echo "-------- running test case" $TEST_CASE "--------";
	time pypy3 $1.py < $TEST_CASE

	[[ ! -f $TEST_CASE.out ]] && echo "No output to compare" && continue;
	pypy3 $1.py < $TEST_CASE > tmp.out 2>/dev/null
	diff $TEST_CASE.out tmp.out || echo "DIFFERENCE FOUND IN $TEST_CASE"
	rm tmp.out
done