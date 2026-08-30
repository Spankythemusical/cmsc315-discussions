# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

Implementation Notes

I completed all of hte TODO prompts in `unit3_discussion.py`:

 - `insert_at(lst, index, value)` used Python's built-in `list.insert()` to hadd a value at a given index.  I documented that any elements at or after that index shift one position to the right, which makes insertion at the beginning or middle an O9n0 operation, while inserting at the end is O(1) on average.
 - `delete_at(1st, index)` validated the index before removing anything, returning `None` for any out-of-range index instead of letting the program crash with an `IndexError`.  Valid deletions used `list.pop(index)`, which returns the removed value and shifts remaining elements left to close the gap.
 - `search_value(1st, value)` performed a linear scan from index 0, returning the matching index or `-1` if the value was never found.  I noted in the comments this this is O(n) because Python lists aren't sorted or indexed for faster lookup by value.
 - In `main()`, I built a grocery list example and demonstrated insertion and deletion at the beginning, middle, and end, followed by searches for both an existing and a missing value.
 - For edge cases, I demonstrated deleting with an out-of-range index, inserting into an empty list, and deleting from an empty list.  All test were handled without crashing the program.
## Discussion Board Reflection

Completing this assignment sharpened my understanding of how Python lists actually work under the hood.  Implementing `insert_at`, `delete_at`, and `search_value` forced me to thin past just calling built-in methods.  I had to reason why `insert()` and `pop()` require shifting elements in memory, and why a plain search has to scan sequentially rather than jump straight to a value.

The biggest challenge was edge-case handling, particularly making sure `delete_at` failed gracefully instead of crashing.  I ran into an `IndexError` when testing deletion on an empty list, which pushed me to double-check that my validation logic (`index >= len(lst)`) correctly caught a zero-length list before ever calling `pop()`.

This mattered because in real applications, list operations are not free: inserting or deleting from the front of a large list, or searching through it linearly, gets expensive as data grows.  Applications with frequent insertions/deletions in the middle of large datasets often benefit from alternative structures like the linked lists instead. 