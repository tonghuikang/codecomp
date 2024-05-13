import java.util.*
import kotlin.collections.HashSet
import kotlin.math.min

val m9 = 1000000007  // 998244353
val yes = "YES"
val no = "NO"
val d4 = listOf(Pair(1, 0), Pair(0, 1), Pair(-1, 0), Pair(0, -1))
val d8 = listOf(Pair(1, 0), Pair(1, 1), Pair(0, 1), Pair(-1, 1), Pair(-1, 0), Pair(-1, -1), Pair(0, -1), Pair(1, -1))
val d6 = listOf(Pair(2, 0), Pair(1, 1), Pair(-1, 1), Pair(-2, 0), Pair(-1, -1), Pair(1, -1))  // hexagonal layout
val abc = "abcdefghijklmnopqrstuvwxyz"
val abc_map = abc.withIndex().associate { it.value to it.index }
val MAXINT = Int.MAX_VALUE
val e18 = 1000000000000000010L

fun readMatrix(rows: Int): List<List<Int>> = List(rows) { readln().split(" ").map(String::toInt) }
fun readStrings(rows: Int): List<String> = List(rows) { readln().trim() }
fun minusOne(arr: List<Int>): List<Int> = arr.map { it - 1 }
fun minusOneMatrix(mrr: List<List<Int>>): List<List<Int>> = mrr.map { row -> row.map { it - 1 } }

val pool = HashSet<Int>().apply {
    for (i in 0 until 100) {
        for (j in 0 until 100) {
            val value = i * 3 + j * 5
            if (value <= 100) {
                add(value)
            }
        }
    }
}

fun solve(n: Int): Int {
    var minRes = 100
    for (x in pool) {
        if (n >= x) {
            val res = n - x
            minRes = min(minRes, res)
        }
    }
    return minRes
}

fun main() {
    val caseCount = readln().toInt()
    for (caseNum in 1..caseCount) {
        val n = readln().toInt()
        val result = solve(n)
        println(result)
    }
}