"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    lst.insert(index, value)

    return lst

    pass


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if not isinstance(index, int) or index < 0 or index >= len(lst):
        return None

    removed_value = lst.pop(index)
    return removed_value
    pass


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i

    return --1
    pass


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    groceries = ["eggs", "milk", "bread", "butter"]
    print(f"Original list: {groceries}")

    insert_at(groceries, 0, "coffee")
    print(f"After inserting 'coffee' at the beginning: {groceries}")

    middle_index = len(groceries) // 2
    insert_at(groceries, middle_index, "cheese")
    print(f"After inserting 'cheese' in the middle: {groceries}")

    insert_at(groceries, len(groceries), "apples")
    print(f"After inserting 'apples' at the end: {groceries}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    removed = delete_at(groceries, 0)
    print(f"Removed '{removed}' from the beginning.  List is now: {groceries}")

    middle_index = len(groceries) // 2
    removed = delete_at(groceries, middle_index)
    print(f"Removed '{removed}' from the middle. List is now: {groceries}")

    removed = delete_at(groceries, len(groceries) - 1)
    print(f"Removed '{removed}' from the end. List is now: {groceries}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    target = "milk"
    result = search_value(groceries, target)
    print(f"Searching for '{target}': found at index {result}"
          if result != -1 else f"Searching for '{target}': not found")

    target = "orange juice"
    result = search_value(groceries, target)
    print(f"Searching for '{target}': found at index {result}"
          if result != -1 else f"Searching for '{target}': not found")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    invalid_result = delete_at(groceries, 99)
    print(f"Attempting to delete index 99 (invalid): returned {invalid_result}")

    empty_list = []
    insert_at(empty_list, 0, "first item")
    print(f"Inserting into an empty list: {empty_list}")

    empty_result = delete_at([], 0)
    print(f"Attempting to delete from an empty list: returned {empty_result}")



if __name__ == "__main__":
    main()