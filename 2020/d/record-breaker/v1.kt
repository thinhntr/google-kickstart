import kotlin.math.max

fun main() {
    val T = readLine()!!.toInt()
    repeat(T) { t ->
        val N = readLine()!!.toInt()
        val V = readLine()!!.split(' ').map(String::toInt)
        val metNums = mutableSetOf<Int>()
        var currentMax = V[0]
        var count = 0
        for (i in 0 until N) {
            currentMax = max(currentMax, V[i])
            if (V[i] != currentMax || V[i] in metNums) {
                continue
            }
            metNums.add(V[i])
            if (i == N - 1 || V[i] > V[i + 1]) {
                count++
            }
        }
        println("Case #${t + 1}: $count")

    }
}
