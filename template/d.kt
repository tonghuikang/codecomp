import java.util.*
import kotlin.math.min

fun main() {
    val scanner = Scanner(System.`in`)
    val LARGE = 1e18.toLong() + 10

    val t = scanner.nextInt()  // Read the number of test cases
    repeat(t) {
        val n = scanner.nextInt()  // Read the size of the array
        val arr = LongArray(n) { scanner.nextLong() }

        val dp = Array(2) { LongArray(2) { LARGE } }
        dp[1][0] = 0
        dp[1][1] = 0

        for (x in arr) {
            if (x == 0L) {
                dp[1][0] = LARGE
                dp[1][1] = min(dp[1][1], dp[0][1])
                continue
            }

            val newDp = Array(2) { LongArray(2) { LARGE } }

            // Fix the current step with fix-forward
            newDp[1][0] = min(newDp[1][0], dp[0][0])
            newDp[1][1] = min(newDp[1][1], dp[0][1] + 2 * x)

            // Fix the current step with no fix-forward
            newDp[1][0] = min(newDp[1][0], dp[1][0] + 1)
            newDp[1][1] = min(newDp[1][1], dp[1][1] + x)
            
            // Fix-forward the current step
            newDp[0][0] = min(newDp[0][0], dp[1][0] + 1)
            newDp[0][1] = min(newDp[0][1], dp[1][1] + 2 * x)

            dp[0][0] = newDp[0][0]
            dp[0][1] = newDp[0][1]
            dp[1][0] = newDp[1][0]
            dp[1][1] = newDp[1][1]
        }

        val result = dp[1][1]
        println(result)
    }
}