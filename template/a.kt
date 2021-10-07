import java.lang.AssertionError

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readLong() = readLn().toLong() // single long
private fun readDouble() = readLn().toDouble() // single double
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map { it.toLong() } // list of longs
private fun readDoubles() = readStrings().map { it.toDouble() } // list of doubles


fun main() {
    // read input
    val case_num = readInt()

    for (i in 1..case_num) {
        var srr = readLn()
        var a = 0
        var b = 0
        for (c in srr) {
            // print(c)
            if (c == '<'){
                a ++
            }
            if (c == '>'){
                b ++
            }
        }
        if (a > 0 && b > 0){
            println('?');
            continue;
        }
        if (a > 0) {
            println('<');
            continue;
        }
        if (b > 0) {
            println('>');
            continue;
        }
        println('=');
        continue;
    }
}