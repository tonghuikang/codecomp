import java.io.*
import kotlin.math.*

val m9 = 1_000_000_007L  // Use a long to avoid overflow
val yes = "YES"
val no = "NO"
val d4 = listOf(Pair(1, 0), Pair(0, 1), Pair(-1, 0), Pair(0, -1))
val d8 = listOf(Pair(1, 0), Pair(1, 1), Pair(0, 1), Pair(-1, 1), Pair(-1, 0), Pair(-1, -1), Pair(0, -1), Pair(1, -1))
val d6 = listOf(Pair(2, 0), Pair(1, 1), Pair(-1, 1), Pair(-2, 0), Pair(-1, -1), Pair(1, -1))
val abc = "abcdefghijklmnopqrstuvwxyz"
val abcMap = abc.withIndex().associate { it.value to it.index }
val e18 = 1_000_000_000_000_000_010L

fun log(vararg messages: Any?) {
    if (checkOfflineTest()) {
        System.err.println(messages.joinToString(" ").prependIndent("\u001B[36m").plus("\u001B[0m"))
    }
}

fun checkOfflineTest(): Boolean {
    val user = System.getProperty("user.name")
    return user == "htong"
}

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    fun readLn() = reader.readLine()!!
    fun readInt() = readLn().toInt()
    fun readInts() = readLn().split(" ").map { it.toInt() }
    fun readMatrix(rows: Int): List<List<Int>> = List(rows) { readInts() }
    fun readStrings(rows: Int): List<String> = List(rows) { readLn().trim() }

    fun solve(k: Int, m: Int): Int {
        var m = m % (3 * k)

        if (2 * k <= m && m < 3 * k) return 0
        return 2 * k - m
    }

    val t = readInt()  // Read number of test cases
    repeat(t) {
        val (k, m) = readInts()
        val result = solve(k, m)
        println(result)
    }
}