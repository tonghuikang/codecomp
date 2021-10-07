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
        var q = readInt()

        var mins = 0
        var maxs = 100

        for (j in 1..q) {
            var inp = readStrings()
            println(inp)
            var arr = inp[0]
            var brr = inp[1]
            var c = inp[2]

            if (c[0] == '0' && mins == 0){
                mins == 1
            }

            var a1 = arr.length - 1
            var b1 = brr.length - 1
            var cntr = 0

            while (a1 >= 0 && b1 >= 0) {
                if (arr[a1] != brr[b1]) {
                    break
                }
                a1 -= 1
                b1 -= 1
                cntr += 1

            }

            println(cntr)
            if (c[0] == '1' && maxs > cntr){
                maxs = cntr
            }

            // if (c[0] == '0'){
            // }

        }

        println()
        println(mins)
        println(maxs)
        // println(maxallow - minallow + 1)
        // for (x in minallow..maxallow) {
        //     print(x)
        //     print(" ")
        // }
        println()
        println()

    }
}