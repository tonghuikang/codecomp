import java.io.*
import java.util.*

const val m9 = 1000000007L  // 998244353
val yes = "YES"
val no = "NO"
val d4 = arrayOf(Pair(1, 0), Pair(0, 1), Pair(-1, 0), Pair(0, -1))
val d8 = arrayOf(Pair(1, 0), Pair(1, 1), Pair(0, 1), Pair(-1, 1), Pair(-1, 0), Pair(-1, -1), Pair(0, -1), Pair(1, -1))
val d6 = arrayOf(Pair(2, 0), Pair(1, 1), Pair(-1, 1), Pair(-2, 0), Pair(-1, -1), Pair(1, -1))  // hexagonal layout
val abc = "abcdefghijklmnopqrstuvwxyz"
val abcMap = abc.withIndex().associate { it.value to it.index }
val MAXINT = Long.MAX_VALUE
val e18 = 1000000000000000010L

fun log(vararg args: Any?) {
    println(args.joinToString(" "))
}

fun solve(arr: List<Int>): Long {
    val LARGE = e18
    var dp = arrayOf(
        arrayOf(LARGE, LARGE),
        arrayOf(0L, 0L)
    )

    for (x in arr) {
        if (x == 0) {
            dp = arrayOf(
                arrayOf(LARGE, LARGE),
                arrayOf(minOf(dp[0][0], dp[1][0]), minOf(dp[0][1], dp[1][1]))
            )
            continue
        }

        val newDp = arrayOf(
            arrayOf(LARGE, LARGE),
            arrayOf(LARGE, LARGE)
        )

        // fix the current step with fix-forward
        newDp[1][0] = minOf(newDp[1][0], dp[0][0])
        newDp[1][1] = minOf(newDp[1][1], dp[0][1] + 2 * x)

        // fix the current step with no fix-forward
        newDp[1][0] = minOf(newDp[1][0], dp[1][0] + 1)
        newDp[1][1] = minOf(newDp[1][1], dp[1][1] + x)

        // fix-forward the current step
        newDp[0][0] = minOf(newDp[0][0], dp[1][0] + 1)
        newDp[0][1] = minOf(newDp[0][1], dp[1][1] + 2 * x)

        dp = newDp
    }

    return dp[1][1]
}

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val t = br.readLine().toInt()
    repeat(t) {
        val n = br.readLine().toInt()
        val arr = br.readLine().split(" ").map { it.toInt() }
        val result = solve(arr)
        println(result)
    }
}