# Competitive Programming Template

This contains the code template I use for competitive programming.


### Contest preparation script

```
cd template
git checkout -b $CONTEST_NAME
code .  # open VSCode
python3 sample_gen.py  # and download test cases with jmerle/competitive-companion
jupyter notebook  # for adhoc computations
```

These are the command-line shortcuts that I use

```
alias ss="source /usr/local/anaconda3/etc/profile.d/conda.sh"
alias sa="conda activate"
alias jn="jupyter notebook"
alias code="open -a /Applications/Visual\ Studio\ Code.app"

alias gcm="git checkout master"
alias ggc="git add . && git commit -m checkpoint"
alisa ggs="python3 sample_gen.py"

alias t="touch"
alias cx="./run_cpp.sh"
alias kx="./run_kt.sh"
alias px="./run_py.sh"
alias pi="./run_pi.sh"
pxa() { autoflake --in-place --remove-all-unused-imports "$1".py }
```



### How to use (general)

Copy the test case to `a0`. If there is an expected output for the test case, copy it to `a0.out`

If there are additional test cases copy them as `a1`, `a2` etc.

I use the Competitive Companion extension to download test cases.
I will start the Python script with `python3 sample_gen.py` or `ggs`, and then click on the extension.
The Competitive Companion extension will parse and send the test cases to a port (which you have to specify) and the Python script process the test cases into respective files. 

In the code template, there are examples on how to IO. Uncomment and use them.



### How to use (Python)

You will need to have pypy3 installed.

To run the code

````bash
python a.py < a0
````

The debug statements prints in a different color.
You can submit the code without commenting out the debugging statements, I do not think it should affect the run time.

To compile the code and run for all test cases

```bash
./run_py.sh a
```

I made the above command an alias, so in contests I run

```bash
px a
```

To clean up unused imports, run `autoflake --in-place --remove-all-unused-imports a.py` or `pxa a`.


#### Recursion

If you need to recursively call functions more than 1000 times, please use the function decorator in `template_recursion.py` (may not always work)



#### Interactive questions

- You can read input as usual.
- When printing, please flush, i.e. `print(x, flush=True)`
- At the end of the program, please execute `sys.exit()`



Google provides an [interactive testing tool](https://codingcompetitions.withgoogle.com/codejam/faq#interactive-problems). Google maintains an `interactive_runner.py` for all interactive problems. In each interactive problem, they provide a specific `local_testing_tool.py` for you to test your code.

You will need to write your code in `sample_interactive_script.py`.

```bash
python interactive_runner.py python3 sample_local_testing_tool.py $TEST_CASE -- python3 sample_interactive_script.py
```

I made the above command an alias, so in contests I run

```bash
pi 1
```


#### Algorithm Templates

These are the sources that I collected my templates for Python
- [PyRival](https://github.com/cheran-senthil/PyRival), which is contributed by top Python competitive programmers
- [AtCoder library](https://github.com/not522/ac-library-python)
- [Leetcode](https://leetcode.com) solutions
- [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers) and [intervaltree](https://github.com/chaimleib/intervaltree)



### How to use (C++)

Please refer to my [C++ conversion course](../docs/cpp_conversion_course.md)

To compile the code and run for all test cases

```
./run_cpp.sh x
```

I made the above command an alias, so in contests I run

```bash
cx a
```


### How to use (C++)

Please refer to my [C++ conversion course](../docs/cpp_conversion_course.md)

To compile the code and run for all test cases

```
./run_cpp.sh x
```

I made the above command an alias, so in contests I run

```bash
cx a
```
