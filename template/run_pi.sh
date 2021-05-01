[[ -z "$1" ]] && { echo "Test case number is empty" ; exit 1; }

TEST_CASE=$1
echo "-------- running test case" $TEST_CASE "--------";
time python interactive_runner.py python3 sample_local_testing_tool.py $1 -- python3 sample_interactive_script.py