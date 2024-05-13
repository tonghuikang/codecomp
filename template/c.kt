import java.io.*
import kotlin.math.*

const val m9 = 1000000007  // 998244353
const val yes = "YES"
const val no = "NO"
val d4 = arrayOf(Pair(1,0), Pair(0,1), Pair(-1,0), Pair(0,-1))
val d8 = arrayOf(Pair(1,0), Pair(1,1), Pair(0,1), Pair(-1,1), Pair(-1,0), Pair(-1,-1), Pair(0,-1), Pair(1,-1))
val d6 = arrayOf(Pair(2,0), Pair(1,1), Pair(-1,1), Pair(-2,0), Pair(-1,-1), Pair(1,-1))  // hexagonal layout
val abc = "abcdefghijklmnopqrstuvwxyz"
val abcMap = abc.withIndex().associate { it.value to it.index }
const val MAXINT = Int.MAX_VALUE
const val e18 = 1000000000000000010L  // 10^18 + 10

fun log(vararg args: Any?) {
    println(args.joinToString(" "))
}

fun main(args: Array<String>) {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val t = reader.readLine().trim().toInt()  // Number of test cases
    repeat(t) {
        val (n, k) = reader.readLine().split(" ").map { it.toLong() }  // Use Long instead of Int
        val result = solve(n.toInt(), k)  // Assuming 'solve' handles 'n' as Int, and 'k' as Long
        println(result)
    }
}

fun solve(n: Int, k: Long): Int {
    val binK = k.toString(2).reversed()
    val i = binK.indexOfFirst { it == '1' }
    return n - i
}