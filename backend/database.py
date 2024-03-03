problem_names = {
    "1":"Count Inversions",
    "2":"Generate Partitions",
    "3":"Range Sum Queries"
}

correct_solutions = {
    "1":"""
    private class InversionsCounter<T : Comparable<T>>(a: List<T>) {
        private val a = MutableList(a.size) { Pair(a[it], it) }
        private val b = mutableListOf<Pair<T, Int>>()
        private val result = IntArray(a.size)

        private fun mergeSort(left: Int, right: Int) {
            if (left + 1 >= right) {
                return
            }
            val mid = (left + right) shr 1
            mergeSort(left, mid)
            mergeSort(mid, right)
            var i = left
            var j = mid
            while (i < mid || j < right) {
                if (j >= right || (i < mid && a[i].first <= a[j].first)) {
                    b.add(a[i])
                    i++
                } else {
                    result[a[j].second] += mid - i
                    b.add(a[j])
                    j++
                }
            }
            for (pos in 0 until b.size) {
                a[pos + left] = b[pos]
            }
            b.clear()
        }

        fun count(): IntArray {
            mergeSort(0, a.size)
            return result
        }
    }
                
    fun <T : Comparable<T>> findInversions(a: List<T>): IntArray {
    return InversionsCounter(a).count()
    }
    """,
    "2":"""
    import org.junit.jupiter.api.Assertions.assertEquals
    import org.junit.jupiter.api.Assertions.assertTrue
    import org.junit.jupiter.api.Test

    class Tests {

        private fun canonicalize(p: Partition) = Partition(p.terms.sorted())

        private fun checkPartitions(expected: Int, n: Int, found: List<Partition>) {
            assertEquals(expected, found.size) {
                \"Wrong number of partitions\"
            }
            val unique = found.map(this::canonicalize).toCollection(mutableSetOf())
            assertTrue(unique.size == found.size) {
                \"Partitions are not unique\"
            }
            unique.forEach { p ->
                p.terms.forEach {
                    assertTrue(it in 1..n) {
                        \"Wrong terms in partition expected in [1, $n] found $it\"
                    }
                }
                val partitionSum = p.terms.sum()
                assertEquals(n, partitionSum) {
                    \"Wrong sum\"
                }
            }
        }

        @Test
        fun sample() {
            val actual = generatePartitions(4)
            checkPartitions(5, 4, actual)
        }
    }
    """,
    "3":"""
    class RangeSum(a: IntArray) {

        // Implement additional fields and method here
        private val prefix = LongArray(a.size) { a[it].toLong() }

        init {
            for (i in prefix.indices.drop(1)) {
                prefix[i] += prefix[i - 1]
            }
        }

        private fun get(index: Int): Long {
            return when (index) {
                -1 -> 0
                else -> prefix[index]
            }
        }

        fun getSum(left: Int, right: Int): Long {
            return get(right - 1) - get(left - 1)
        }
    }
    """
}

tests = {
    "1":"""
    import org.junit.jupiter.api.Assertions.assertArrayEquals
    import org.junit.jupiter.api.Test

    class Tests {
        @Test
        fun sample1() {
            val list = listOf(3, 1, 3, 4, 2)
            val actual = findInversions(list)
            assertArrayEquals(intArrayOf(0, 1, 0, 0, 3), actual)
        }
    }
    """,
    "2":"""
    import org.junit.jupiter.api.Assertions.assertEquals
    import org.junit.jupiter.api.Assertions.assertTrue
    import org.junit.jupiter.api.Test

    class Tests {

        private fun canonicalize(p: Partition) = Partition(p.terms.sorted())

        private fun checkPartitions(expected: Int, n: Int, found: List<Partition>) {
            assertEquals(expected, found.size) {
                \"Wrong number of partitions\"
            }
            val unique = found.map(this::canonicalize).toCollection(mutableSetOf())
            assertTrue(unique.size == found.size) {
                \"Partitions are not unique\"
            }
            unique.forEach { p ->
                p.terms.forEach {
                    assertTrue(it in 1..n) {
                        \"Wrong terms in partition expected in [1, $n] found $it\"
                    }
                }
                val partitionSum = p.terms.sum()
                assertEquals(n, partitionSum) {
                    \"Wrong sum\"
                }
            }
        }

        @Test
        fun sample() {
            val actual = generatePartitions(4)
            checkPartitions(5, 4, actual)
        }
    }
    """,
    "3":"""
    import org.junit.jupiter.api.Assertions.assertEquals
    import org.junit.jupiter.api.Test

    class Tests {
        @Test
        fun sample() {
            val rsq = RangeSum(intArrayOf(1, 3, -2, 4, 2))
            assertEquals(1L, rsq.getSum(0, 1))
            assertEquals(8L, rsq.getSum(0, 5))
            assertEquals(0L, rsq.getSum(2, 2))
            assertEquals(-2L, rsq.getSum(2, 3))
            assertEquals(4L, rsq.getSum(2, 5))
            assertEquals(5, rsq.getSum(1, 4))
            assertEquals(0, rsq.getSum(0, 0))
            assertEquals(2, rsq.getSum(4, 5))
        }
    }
    """
}

def get_problem_name(problem_id: str) -> str | None:
    return problem_names[problem_id] if problem_id in problem_names else None

def get_correct_solution(problem_id: str) -> str | None:
    return correct_solutions[problem_id] if problem_id in correct_solutions else None

def get_tests(problem_id: str) -> str | None:
    return tests[problem_id] if problem_id in tests else None