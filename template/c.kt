import java.lang.AssertionError
import kotlin.math.min
import kotlin.math.max

private fun readLn() = readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readLong() = readLn().toLong() // single long
private fun readDouble() = readLn().toDouble() // single double
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map { it.toLong() } // list of longs
private fun readDoubles() = readStrings().map { it.toDouble() } // list of doubles
 

// def solve_(a,b,c):
//     # your solution here
//     minres = c
//     for i in range(c):
//         if not a <= i < b:
//             continue
//         left = min(a+i, 2*i-a)
//         i += 1
//         right = min(2*(c-b)+b-i, b-i+c-i)
//         log(left, right)
//         minres = min(minres, max(left,right))

//     return minres


fun main() {
    // read input
    val case_num = readInt()

    for (z in 1..case_num) {
        val inp = readInts()
        val c = inp[0] - 1
        val a = min(inp[1], inp[2]) - 1
        val b = max(inp[1], inp[2]) - 1

        var minres = c

        for (i in a..b-1){
            minres = min(minres, max(
                min(a+i, 2*i-a),
                min(2*(c-b)+b-i+1, b-(i+1)+c-(i+1))
            ))
        }
        println(minres)
    }
}
