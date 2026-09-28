"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""

import random
import time
from turtledemo.penrose import start


def bubble_sort(lst, key=None):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    Notes:
        Time Complexity - O(n^2) worst/average case.  O(n) best case
        (already sorted) due to early-exit "swapped" flag

        Space Complexity - O(n) because we copy the input; the sort
        works in place (O(1) extra).

        Stable - Only swap when the left items is strictly greater, so
        equal items never pass each other.

        key - optional function.  Used to pick the value to compare.  Defaults
        to itself.
    """

    # Default key compares elements directly.
    if key is None:
        key = lambda item: item

    # Copy the list so original data is not modified.
    result = list(lst)
    n = len(result)

    # Each out pass sends the largest remaining value to the end.
    # After pass i the last i positions are already in final order.
    for i in range(n - 1):
        swapped = False

        # Only scan the unsorted portion (n - 1 - i elements).
        for j in range(n - 1 - i):
            # Compare adjacent elements; swap only if strictly out of order
            # (strict > keeps equal elements in their original order - stable).
            if key(result[j]) > key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # If a full pass made no swaps, the list is sorted so stop early.
        if not swapped:
            break

    return result
    # pass


def merge_sort(lst, key=None):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    Notes:
        Time Complexity - O(n log n) in best, average, and worst cases
        List is halved in log n times, each level does O(n) work.

        Space Complexity - O(n) for teh temp lists created while merging.

        Stable - merge() takes from the left half on ties.

        Always returns a new list; the input is never modified.
    """

    # Base case: list of 0 or 1 elements is already sorted.
    # Returning a copy keeps the new list behavior consistent.
    if len(lst) <= 1:
        return list(lst)

    # Divide: find the midpoint and split into two halves.
    mid = len(lst) // 2

    # Recursively sort each half.
    left = merge_sort(lst[:mid], key)
    right = merge_sort(lst[mid:], key)

    # Merge the two sorted halves into one sorted list.
    return merge(left, right, key)

    # pass


def merge(left, right, key=None):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.

    Notes:
        Runs in O(len(left) + len(right)) time because each element is
        looked at exactly ones.
    """

    if key is None:
        key = lambda item: item

    result = []
    i = j = 0 # Read positions in left and right.

    # Walk both lists, always taking the smaller front element.
    while i < len(left) and j < len(right):
        # "<=" takes from the LEFT lists on ties, preserving the
        # original relative order of equal items.
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # One list is exhausted; the rest of the other list is already sorted,
    # so append whatever remains.
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def show_results(label, data):
    """Helper: sort a dataset with both algorithms and print labeled results."""
    bubble_result = bubble_sort(data)
    merge_result = merge_sort(data)

    print(f"{label}")
    print(f"  Original:    {data}")
    print(f"  Bubble Sort: {bubble_result}")
    print(f"  Merge Sort:  {merge_result}")
    # Check both against Python's built-in sorted() as a correctness test.
    print(f"  Results match each other: {bubble_result == merge_result}")
    print(f"  Matches built-in sorted(): {merge_result == sorted(data)}")
    return bubble_result, merge_result

    #pass


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.



    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")
    # Unsorted list of 10 elements.
    dataset1 = [64, 34, 25, 12, 22, 11, 90, 5, 77, 41]
    show_results("Dataset #1 (random integers):", dataset1)
    # Confirm neither algorithm changed the original list.
    print(f"  Original unchanged after sorting: {dataset1}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")
    # Content ratings with one tie to show both algorithms work with non-integer
    # comparable items.
    dataset2 = [4.7, 3.2, 4.9, 2.8, 4.1, 3.9, 4.7, 1.5]
    show_results("Dataset #2 (content ratings):", dataset2)

    print("\n Real-world example - sort titles by rating (stable):")
    titles = [
        ("Dune (2021)", 4.2),
        ("Get Out (2017)", 3.8),
        ("Top Gun: Maverick (2022)", 4.2), # Ties with Dune, listed after.
        ("Oppenheimer (2023)", 4.9),
        ("Knives Out (2019)", 3.8), # Ties with Get Out, listed after.
    ]
    by_rating = merge_sort(titles, key=lambda t: t[1])
    for title, rating in by_rating:
        print(f"    {rating}   {title}")
    print("  Ties kept their original order: "
          f"{bubble_sort(titles, key=lambda t: t[1]) == by_rating}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Empty list: bubble sort's loops never run.  Merge sort hits its base
    # case immediately.  Both return [] without errors.
    show_results("Emtpy list:", [])

    # Single element: Already sorted by definition.  Both return as-is.
    show_results("\nSingle-element list:", [42])

    # Already sorted: Bubble sort's early-exit flag stops after one pass (O(n)).
    # Merge sort still does all splits and merges.
    show_results("\nAlready sorted list:", [1, 2, 3, 4, 5, 6, 7])

    # Reverse sorted: Worst case for bubble sort, swapping every comparison.
    # Merge sort's work is the same as any other.
    show_results("\nReverse-sorted list:", [9, 8, 7, 6, 5, 4, 3, 2, 1])

    # Duplicates: Equal values are kept together, neither algorithm swaps, so
    # the sort stays stable.
    show_results("\nList with duplicates:", [5, 3, 5, 1, 3, 5, 1])

    # PERFORMANCE COMPARISON
    # Time both algorithms on growing random inputs to show how
    # O(n^2) and O(n log n) scale differently.

    print("\n=== PERFORMANCE COMPARISON ===")
    random.seed(315) # Fixed for repeatable results
    print(f"  {'n':>6} | {'Bubble 9s0':>11} | {'Merge (s)':>10}")
    for n in (100, 500, 1000, 2000):
        data = [random.randint(0, 10_000) for _ in range(n)]

        start = time.perf_counter()
        bubble_sort(data)
        bubble_time = time.perf_counter() - start

        start = time.perf_counter()
        merge_sort(data)
        merge_time = time.perf_counter() - start

        print(f"  {'n':>6} | {bubble_time:>11.4f} | {merge_time:>10.4f}")
    print("   Doubling n roughly quadrupels Bubble Sort's time, "
          "while Merge Sort grows only slightly faster than linear.")




if __name__ == "__main__":
    main()