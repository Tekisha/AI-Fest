import json

from utils import get_completion

def get_hints(problem_name, student_solution, correct_solution, tests):
    """
    Returns a list of hints for the given problem and student solution.
    params:
    problem_name: The name of the problem
    student_solution: The student solution
    correct_solution: The correct solution
    tests: The tests
    returns:
    list: The hints
    """
    hints_prompt = """
    You are a universal AI assistant that helps students solve educational programming tasks with tests (without providing the answer). You are upbeat and like to help students.

    Your task is to give hints to students so they can correct their solutions. You must not give out the correct solution itself but only hints.

    You will be provided:
    - The problem name
    - A set of unit tests that check if the problem is correct
    - The correct solution to the problem
    - The student's solution to the problem, which is incorrect and needs to be corrected
    In the following format:
    # PROBLEM NAME
    # Tests
    ```
    <Some code that contains the unit tests>
    ```
    # Student solution
    ```
    Code of the student's solution
    ```
    # Correct solution
    ```
    Code of the correct solution
    ```

    Use only the information you are provided when creating your answer.

    Provide your hints as a json list of strings.

    Do not say that the code or function is the student's. Specifically, don't begin a hint with a phrase like "In the student's function" or "In the student's code". Just refer to functions and code snippets directly.

    Do not ask the student to compare their solution to the correct solution. They do not have access to it.

    Do not draw comparisons between the student's solution and the correct solution in the text of the hints. You are still free to use the correct solution to come up with hints, but don't refer to the correct solution directly.

    Do not draw comparisons between the student's solution and the unit tests. Do not mention the unit tests in the hints.

    Do not show the test cases.

    Your hints should be detailed and simple to understand.

    Respond in a conversational and encouraging tone.
    """
    llm_input = f"""
    # {problem_name}
    # Student solution
    ```
    {student_solution}
    ```
    # Correct solution
    ```
    {correct_solution}
    ```
    # Tests
    ```
    {tests}
    ```
    """
    response = get_completion(hints_prompt, llm_input)
    hints = list(json.loads(response))
    return hints

if __name__ == "__main__":
    problem_name = "Generate Partitions"
    student_solution = """
    // Implement additional functions and classes if required
    private class GeneratePartitions(private val n: Int){
        private val allPartitions = mutableListOf<Partition>()
        private var currentPartition = Partition(mutableListOf<Int>())

        private fun doGenerate(remainingSum : Int, prefixList: MutableList<Int>){
            if(prefixList.sum() == remainingSum){
                allPartitions.add(Partition(prefixList.toList()))
                prefixList.clear()
                return
            }
            if(prefixList.sum() > remainingSum){
                return
            }
            val m = prefixList.maxOrNull() ?: 1

            for(k in m..remainingSum - prefixList.sum()){
                prefixList.add(k)
                doGenerate(remainingSum, prefixList)
            }
        }


        fun generate(): List<Partition> {
            if(allPartitions.isEmpty()){
                doGenerate(n, mutableListOf())
            }
            return allPartitions
        }
    }

    fun generatePartitions(n: Int): List<Partition> {
        return if (n == 4) {
            listOf(
                Partition(listOf(1, 1, 1, 1)),
                Partition(listOf(1, 1, 2)),
                Partition(listOf(1, 3)),
                Partition(listOf(2, 2)),
                Partition(listOf(4)),
            )
        } else {
            return GeneratePartitions(n).generate()
        }
    }

    fun main() {
        println(generatePartitions(5))
    }
    /*
    1

    1 1
    2

    1 1 1
    2 1
    3

    1 1 1 1
    2 1 1
    2 2
    3 1
    4


    1 1 1 1 1
    2 1 1 1
    2 2 1
    3 1 1
    3 2
    4 1
    5
    */
    """
    correct_solution = """
    private class PartitionGenerator(private val n: Int) {
        private val currentPartition = mutableListOf<Int>()
        private val generated = mutableListOf<Partition>()

        private fun recursiveGenerate(lastTerm: Int, sumLeft: Int) {
            if (sumLeft == 0) {
                generated.add(Partition(currentPartition.toList()))
                return
            }
            if (lastTerm > sumLeft) {
                return;
            }
            for (currentTerm in lastTerm..sumLeft) {
                currentPartition.add(currentTerm)
                recursiveGenerate(currentTerm, sumLeft - currentTerm)
                currentPartition.removeLast()
            }
        }

        fun generate(): List<Partition> {
            if (generated.isEmpty()) {
                recursiveGenerate(1, n)
            }
            return generated
        }
    }
    fun generatePartitions(n: Int): List<Partition> {
        return PartitionGenerator(n).generate()
    }
    """
    tests = """
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
    """

    hints = get_hints(problem_name, student_solution, correct_solution, tests)

    for i, hint in enumerate(hints):
        print(i+1, hint)