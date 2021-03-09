echo "-------- compiling --------"
kotlinc $1.kt -include-runtime -d $1.jar
for TEST_CASE in $1*;
	do
	[[ $TEST_CASE == *.* ]] && continue; 
    echo "-------- running test case" $TEST_CASE "--------"
	time java -jar $1.jar < $TEST_CASE
done
rm $1.jar