# python script $1.py
# input $1*
# output $1*.out (optional)
# files $1* with other extensions are ignored

[[ ! -f $1.py ]] && echo "$1.py not found" && exit 1; 

for TEST_CASE in $1*;
	do
	[[ $TEST_CASE == *.* ]] && continue; 
    echo "-------- running test case" $TEST_CASE "--------";
	time pypy3 $1.py < $TEST_CASE

	# compare with $TEST_CASE.out if exist
	[[ ! -f $TEST_CASE.out ]] && echo "No output to compare" && continue;

	pypy3 $1.py < $TEST_CASE > tmp.out 2>/dev/null
	diff $TEST_CASE.out tmp.out || echo "DIFFERENCE FOUND IN $TEST_CASE"
	rm tmp.out

done