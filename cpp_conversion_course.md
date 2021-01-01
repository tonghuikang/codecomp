# C++ conversion course

To make `#include <bits/stdc++.h>` work

```bash
sudo cp template/stdc++.h /Library/Developer/CommandLineTools/usr/include/c++/v1/bits/
```

The original source is [here](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/precompiled/stdc%2B%2B.h).



### To compile the code

```bash
g++ -std=c++17 -o tmp.out -Wall -Wno-unknown-pragmas x.cpp
```



Understanding the flags

- `-std=c++17`  compile with the C++17 standard. [Docs](https://gcc.gnu.org/projects/cxx-status.html#cxx17)
- `-o tmp.out` specifies the name of the compiled code. The default would have been `a.out` [Stack Overflow](https://askubuntu.com/questions/61408/what-is-a-command-to-compile-and-run-c-programs)
- `-Wall` enables all the warnings. [Docs](https://gcc.gnu.org/onlinedocs/gcc-4.3.2/gcc/Warning-Options.html)
- `-Wno-unknown-pragmas` disables warning for optimizer. [Stack Overflow](https://stackoverflow.com/questions/132667/how-to-disable-pragma-warnings)



(To experiment whether the optimisation really improves the result.)