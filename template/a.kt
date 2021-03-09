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
    val n = readInt()

    for (i in 1..n) {
        var inp = readLongs()
        var x = inp[0]
        var y = inp[1]
        var ans = 0L
        var pdt = 1000000000L
        while (y >= x){
            while (y >= x*pdt){
                y = y - x*pdt
                ans ++
            }
            pdt = pdt/10
        }
        println(ans + y)
    }
}
