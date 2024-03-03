import json

from duckduckgo_search import DDGS
from utils import get_completion
from time import sleep


def get_topic_links(topic, sites, max_results=1):
    """
    Returns a list of links for a given topic from a list of sites.

    params:
    topic: str: the topic to search for
    sites: list: a list of sites to search for the topic
    max_results: int: the maximum number of results to return
    returns:
    list: a list of dictionaries containing the title, url, and text of the search results
    """
    query = f"{topic}" + f" site:{sites[0]}" + ''.join([f" OR site:{site}" for site in sites[1:]])
    print(query)
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=max_results)]
    return [{'title': r['title'], 'url': r['href'], 'text': r['body']} for r in results][0:max_results+1]


def get_links_for_problem(problem_name, correct_solution, tests, sites):
    """
    Searches for links to sites that contain information about the topics tested by a problem.
 
    params:
    problem_name: str: The name of the problem
    correct_solution: str: Code containing the correct solution to the problem
    tests: str: The unit tests for the problem
    sites: list: A list of sites to search for the topics
    returns:
    list: a list of dictionaries containing the title, url, and text of the search results
    """
    topics_prompt = """
    You are a universal AI assistant that helps students solve educational programming tasks with tests (without providing the answer). You are upbeat and like to help students.

    Your task is to analyze the programming tasks and extract the list of algorithms and computer science concepts that they test.

    You will be provided:
    - The problem name
    - A set of unit tests that check if the problem is correct
    - The correct solution to the problem
    In the following format:
    # PROBLEM NAME
    # Tests
    ```
    <Some code that contains the unit tests>
    ```
    # Correct solution
    ```
    Code of the correct solution
    ```

    Output the list of topics as a JSON list of strings.
    Include only the names of the topics in the strings.
    If the problem tests a data structure, include that specific data structure in the list of topics by name. Correct: List. Incorrect: Data Structures (List)
    Do not include any terms that are specific to certain programming languages. Some of these are: Classes, Objects, Generics, Comparable Interface, Interfaces, Comparables, Comparable. This is not an exhaustive list.
    Do not include unit testing in the list of concepts.

    Do not include the problem itself in the list of topics or anything that strongly resembles it. 
    For example, if the name of the problem is "Count Inversions", do not include any of the follwing: "Inversion Count in an array", "Count Inversion", "Counting Inversions", "Inversion Count Technique", "Inversions in an Array".
    If the name of the problem is "Generate Partitions", do not include "Partitioning Problem".

    If an algorithm in the list is part of a wider class of algorithms, include only the algorithm itself, and do not include the class. For example, instead of "Sorting Algorithms (Merge Sort)" include "Merge Sort".
    Exclude the following topics from the list: Lists, Pairs, Strings, Classes, Objects, Array Manipulation, String manipulation, Array, Mutable List, Pair, Tuple, Array Indices, Mutability.

    Order the topics by their significance in solving the problem.

    """
    llm_input = f"""
    # {problem_name}
    # Tests
    ```
    {tests}
    ```
    # Correct solution
    ```
    {correct_solution}
    ```
    """

    response = get_completion(topics_prompt, llm_input)

    topics = list(json.loads(response))
    links = []
    for topic in topics:
        links = links + get_topic_links(topic, sites)
        sleep(2)
    return links


if __name__ == "__main__":
    sites = ["hyperskill.org", "geeksforgeeks.org", "freecodecamp.org", "wikipedia.org"]
    topic = "Merge Sort"
    links = get_topic_links(topic, sites)
    print(links)

    topic = "Recursion"
    links = get_topic_links(topic, sites)
    print(links)

    topic = "Comparable Interface"
    links = get_topic_links(topic, sites)
    print(links)

    problem_name = "Count Inversions"
    correct_solution = """
    def count_inversions(arr):
        n = len(arr)
        temp_arr = [0]*n
        return _mergeSort(arr, temp_arr, 0, n-1)
    """
    tests = """
    import unittest
    class TestCountInversions(unittest.TestCase):
        def test_count_inversions(self):
            self.assertEqual(count_inversions([1, 20, 6, 4, 5]), 5)
            self.assertEqual(count_inversions([2, 4, 1, 3, 5]), 3)
            self.assertEqual(count_inversions([5, 4, 3, 2, 1]), 10)
    """
    links = get_links_for_problem(problem_name, correct_solution, tests, ["hyperskill.org"])
    print(links)