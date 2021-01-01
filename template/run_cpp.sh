echo "-------- compiling --------"
g++ -std=c++17 -o tmp.out -Wall -Wno-unknown-pragmas $1.cpp
for TEST_CASE in $1*;
	do
	[[ $TEST_CASE == *.* ]] && continue; 
    echo "-------- running test case" $TEST_CASE "--------"
	./tmp.out < $TEST_CASE
done
rm tmp.out