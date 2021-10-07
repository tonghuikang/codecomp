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
        var inp = readInts()
        var n = inp[0]
        var k = inp[1]
        var srr = readLn()
        var stack = 0
        var blocks = 0
        for (c in srr) {
            // print(c)
            if (c == '('){
                stack ++
            } else {
                stack --
            }
            if (stack == 0){
                blocks ++
            }
        }
        var depth = n/2 - blocks
        if (k > depth){
            println(blocks + depth)
        } else {
            println(blocks + k)
        }
    }
}