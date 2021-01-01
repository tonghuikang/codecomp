for TEST_CASE in $1*;
	do
	[[ $TEST_CASE == *.* ]] && continue; 
    echo "-------- running test case" $TEST_CASE "--------";
	python3 $1.py < $TEST_CASE
done