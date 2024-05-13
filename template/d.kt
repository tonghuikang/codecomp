import java.util.*
import kotlin.math.min

fun main() {
    val scanner = Scanner(System.`in`)
    val LARGE = 1e18.toLong() + 10

    val t = scanner.nextInt()  // Number of test cases
    repeat(t) {
        val n = scanner.nextInt()  // Size of the array
        val arr = LongArray(n) { scanner.nextLong() }

        var dp = Array(2) { LongArray(2) { LARGE } }
        dp[1][0] = 0
        dp[1][1] = 0

        for (x in arr) {
            if (x == 0L) {
                if (compareTuples(dp[0], dp[1]) < 0) {
                    dp[1] = dp[0]
                }
                dp[0][0] = LARGE
                dp[0][1] = LARGE
                continue
            }

            val newDp = Array(2) { LongArray(2) { LARGE } }

            // Transition considering the current step with fix-forward
            val fixedForward = longArrayOf(dp[0][0], dp[0][1] + 2 * x)
            val noFixForward = longArrayOf(dp[1][0] + 1, dp[1][1] + x)
            val fixForwardCurrent = longArrayOf(dp[1][0] + 1, dp[1][1] + 2 * x)

            // Maintain the minimum tuple
            if (compareTuples(noFixForward, fixedForward) < 0) {
                newDp[1] = noFixForward
            } else {
                newDp[1] = fixedForward
            }

            newDp[0] = fixForwardCurrent

            dp = newDp
        }

        val result = dp[1][1]
        println(result)
    }
}

fun compareTuples(a: LongArray, b: LongArray): Int {
    if (a[0] != b[0]) {
        return a[0].compareTo(b[0])
    }
    return a[1].compareTo(b[1])
}