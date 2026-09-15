"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import time

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks every element one at a time, starting at "
    # index 0, until the target is found or the search reaches the end
    # of the list.  Worst case, every single element has to be checked,
    # so the number of comparisons grows in direct proportion to the size
    # of the list.  "One comparison per element" is exactly what 0(n)
    # time complexity means.
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1
    # pass


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Binary search only works if the list is pre-sorted.  It keeps
    # track of a low and high boundary and repeatedly checks the
    # middle element of the current range.
    low = 0
    high = len(lst) -1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # Target must be in the right half, since everything
            # from low to mid is guaranteed to be smaller than target.
            # This throws out the left half of the search space.
            low = mid + 1
        else:
            # The target must be in the left half, since everything
            # from mid to high is guaranteed to be bigger than target.
            # This throws out the right half of the search space.
            high = mid - 1
    return -1
    # pass


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")
    small_data = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    print(f"Dataset: {small_data}")

    existing_value = 45
    missing_value = 99

    lin_found = linear_search(small_data, existing_value)
    bin_found = binary_search(small_data, existing_value)
    print(f"\nSearching for {existing_value} (exists in list):")
    print(f"  Linear search result: index {lin_found}")
    print(f"  Binary search result: index {bin_found}")
    # Both searches correctly locate the value at the same index.
    # Binary uses fewer comparisons because it can skip half the
    # remaining list at each step, while linear search has to walk
    # forward one element at a time until the value is reached.

    # Search for a value that does not exist in the list.
    lin_missing = linear_search(small_data, missing_value)
    bin_missing = binary_search(small_data, missing_value)
    print(f"\nSearching for {missing_value} (does not exist in list):")
    print(f"  Linear search result: {lin_missing}")
    print(f"  Binary search result: {bin_missing}")
    # Both correctly return -1.  Linear had to search every element,
    # while binary narrowed down the range must faster.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")
    large_data = list(range(0, 2_000_000, 2)) # 1,000,000 sorted even numbers.
    print(f"Dataset size: {len(large_data)} elements")

    large_existing = 1_999_998 # Worst case linear search.
    large_missing = 1_999_999 # Odd number, will never be found.

    start = time.perf_counter()
    lin_result = linear_search(large_data, large_existing)
    lin_time = time.perf_counter() - start

    start = time.perf_counter()
    bin_result = binary_search(large_data, large_existing)
    bin_time = time.perf_counter() - start

    print(f"\nSearching for {large_existing} (exists, near end of list):")
    print(f"  Linear search result: index {lin_result}, time: {lin_time:.6f} sec")
    print(f"  Binary search result: index {bin_result}, time: {bin_time:.6f} sec")

    # A missing value is the worst case for linear search, since it must
    # scan the entire list before giving up.  Binary search still finishes
    # quickly, regardless if the value is present.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Empty List
    empty_list = []
    print(f"\nEmpty list test: linear = {linear_search(empty_list, 5)}, "
          f"binary = {binary_search(empty_list, 5)}")

    # With an empty list, linear search's loop never runs (range(0) is empty)
    # and binary search starts with low=0, high=-1, so the while condition
    # (low <= high) is immediately false.  Both return -1 without error.

    # Edge case 2: Single-element list
    single_list = [7]
    print(f"Single-element list test: "
          f"linear(7) = {linear_search(single_list, 7)} "
          f"binary(7) = {linear_search(single_list, 7)} "
          f"linear(3) = {linear_search(single_list, 3)} "
          f"binary(3) = {linear_search(single_list, 3)}")
    # When the target matches the only element, both algorithms
    # return index 0.  When there is no match, both correctly return -1.

    #Edge case 3: Value at the first position
    first_last_list = [10, 20, 30, 40, 50]
    print(f"\nFirst element test: "
          f"linear = {linear_search(first_last_list, 10)} "
          f"binary = {linear_search(first_last_list, 10)}")

    #Edge case 4: Value at the last position
    print(f"Last element test: "
          f"linear = {linear_search(first_last_list, 50)} "
          f"binary = {linear_search(first_last_list, 50)}")


if __name__ == "__main__":
    main()