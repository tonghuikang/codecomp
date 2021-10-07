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
        var n = readInt()
        var aa = readInts()
        var bb = readInts()
        var c = readInt()

        var a = aa[0]
        var b = bb[0]
        var va = aa[1]
        var vb = bb[1]

        println(listOf(vb,va+c-a).minOrNull());

    }
}