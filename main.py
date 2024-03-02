import os
import random
from grazie.api.client.gateway import AuthType, GrazieApiGatewayClient, GrazieHeaders
from grazie.api.client.chat.prompt import ChatPrompt
from grazie.api.client.endpoints import GrazieApiGatewayUrls
from grazie.api.client.profiles import Profile

token = os.getenv("GRAZIE_JWT_TOKEN").strip()
print(f"Token: '{token}'")

# In a real application, you would have to supply the client's IP address
client_ip = "{}.{}.{}.{}".format(*[str(random.randint(0, 255)) for octet in range(4)])
client = GrazieApiGatewayClient(
    url=GrazieApiGatewayUrls.STAGING,
    grazie_jwt_token=token,
    auth_type=AuthType.APPLICATION,
)
response = client.chat(
    chat=(
        ChatPrompt()
        .add_system("You are a universal AI assistant that helps students solve educational programming tasks with "
                    "tests (without providing the answer). You are upbeat and like to help students."
                    "Your task is to give hints to students so they can correct their solutions. You must not give out "
                    "the correct solution itself but only hints."

                    "You will be provided:"
                    "- The problem name"
                    "- A set of unit tests that check if the problem is correct"
                    "- The correct solution to the problem"
                    "- The student's solution to the problem, which is incorrect and needs to be corrected"
                    "In the following format:"
                    "# PROBLEM NAME"
                    "# Tests"
                    "```"
                    "<Some code that contains the unit tests>"
                    "```"
                    "# Student solution"
                    "```"
                    "Code of the student's solution"
                    "```"
                    "# Correct solution"
                    "```"
                    "Code of the correct solution"
                    "```"
                    "Use only the information you are provided when creating your answer."
                    "Phrase your hints as questions whose answers would lead to the correct solution. "
                    "Provide your hints in a numbered list."
                    "Do not give out more than two hints in your answer."
                    "Do not show the test cases."
                    "Respond in a conversational and encouraging tone.")
        .add_user("# Count Inversions"
                  "# Tests"
                  "```"
                  "import org.junit.jupiter.api.Assertions.assertArrayEquals"
                  "import org.junit.jupiter.api.Test"

                  "class Tests {"
                  "@Test"
                  "fun sample1() {"
                  "val list = listOf(3, 1, 3, 4, 2)"
                  "val actual = findInversions(list)"
                  "assertArrayEquals(intArrayOf(0, 1, 0, 0, 3), actual)"
                  "}"
                  "}"
                  "```"
                  "# Student solution"
                  "```"
                  "// Implement additional functions and classes here"
                  "fun <T : Comparable<T>> findInversions(a: List<T>): IntArray {"
                  "fun mergeAndCount(a: List<T>, l: Int, m: Int, r: Int): Int {"
                  "val left = a.subList(l, m + 1)"
                  "val right = a.subList(m + 1, r + 1)"
                  "var i = 0"
                  "var j = 0"
                  "var k = l"
                  "var swaps = 0"
                  "while (i < left.size && j < right.size) {"
                  "if (left[i] <= right[j]) a[k] = left[i++]"
                  "}"
                  "return 0"
                  "}"
                  "return IntArray(0)"
                  "}"
                  "```"
                  "# Correct solution"
                  "```"
                  "private"


                  "class InversionsCounter< T: Comparable < T >> (a: List < T >)"


                  "{"
                  "private val a = MutableList(a.size) {Pair(a[it], it)}"
                  "private val b = mutableListOf < Pair < T, Int >> ()"
                  "private val result = IntArray(a.size)"

                  "private fun mergeSort(left: Int, right: Int) {"
                  "if (left + 1 >= right)"
                  "{"
                  "return"
                  "}"
                  "val mid = (left + right) shr 1"
                  "mergeSort(left, mid)"
                  "mergeSort(mid, right)"
                  "var i = left"
                  "var j = mid"
                  "while (i < mid | | j < right) {"
                  "if (j >= right | | (i < mid & & a[i].first <= a[j].first)) {"
                  "b.add(a[i])"
                  "i++"
                  "} else {"
                  "result[a[j].second] += mid - i"
                  "b.add(a[j])"
                  "j++"
                  "}"
                  "}"
                  "for (pos in 0 until b.size) {"
                  "a[pos + left] = b[pos]"
                  "}"
                  "b.clear()"
                  "}"

                  "fun"
                  "count(): IntArray"
                  "{"
                  "mergeSort(0, a.size)"
                  "return result"
                  "}"
                  "}"

                  "fun < T: Comparable < T >> findInversions(a: List < T >): IntArray"
                  "{"
                  "return InversionsCounter(a).count()"
                  "}"
                  "```"
                  )
    ),
    profile=Profile.OPENAI_GPT_4,
    headers={
        GrazieHeaders.ORIGINAL_USER_IP: client_ip,
    }
)
print(response.content)
