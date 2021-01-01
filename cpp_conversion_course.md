# C++ conversion course

[TOC]

I have been participating in competitive programming in Python. However, some challenges could only be solved a compiled language like C++.

The procedures detailed here introduces how to setup and use C++ and competitive programming.



### Libraries

Usually we include individual libraries from the C++ Standard Template Library. To code faster, we import all the libraries at once, by adding `#include <bits/stdc++.h>` at the start.

However, we need to add the header file some directory on our local computer.

```bash
sudo cp template/stdc++.h /Library/Developer/CommandLineTools/usr/include/c++/v1/bits/
```

The header file is was obtained from [here](https://github.com/gcc-mirror/gcc/blob/master/libstdc++-v3/include/precompiled/stdc++.h).



### Compiling the code

```bash
g++ -std=c++17 -o tmp.out -Wall -Wno-unknown-pragmas x.cpp
```

Understanding the flags

- `-std=c++17`  compiles with the C++17 standard. [Docs](https://gcc.gnu.org/projects/cxx-status.html#cxx17)
- `-o tmp.out` specifies the name of the compiled code. The default would have been `a.out` [Stack Overflow](https://askubuntu.com/questions/61408/what-is-a-command-to-compile-and-run-c-programs)
- `-Wall` enables all the warnings. [Docs](https://gcc.gnu.org/onlinedocs/gcc-4.3.2/gcc/Warning-Options.html)
- `-Wno-unknown-pragmas` disables warning for optimizer. [Stack Overflow](https://stackoverflow.com/questions/132667/how-to-disable-pragma-warnings)



### Running the code

```bash
tmp.out < x0
```



### Running for all test cases

A script has been written to compile `x.cpp` and run on all test cases `x0`, `x1` etc. 

```bash
./run_cpp.sh x
```

You can make this even more concise by adding `alias cx="./run_cpp.sh"` to  `./zshrc`, and the command is just

```bash
cx x
```



### Auto-formatting

Indentation has helped me understand the written flow of the code, and whether the braces are closed in the correct places.

On MacOS, `options + cmd + P` is the shortcut to format the code on VSCode.

The default setting opens the curly bracket in a new line. To turn this off, go to `File > Settings > C_Cpp.clang_format_fallbackStyle` and replace `Visual Studio` with `{ BasedOnStyle: Google, IndentWidth: 4, ColumnLimit: 0}`.
[Reference](https://stackoverflow.com/questions/46111834/format-curly-braces-on-same-line-in-c-vscode)



 





