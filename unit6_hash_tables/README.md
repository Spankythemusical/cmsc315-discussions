# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

I modeled a small library checkout system using a dictionary where each key was a book's ISBN and each value was a nested dictionary holding the book's title and its number of available copies.

- Insert: I populated the dictionary with five ISBN-to-book-info pairs
- Lookup: I retrieved two existing ISBNs directly with dict[key] and printed the results.
- Update: I updated the copy count for an existing ISBN and printed the dictionary entry before and after the change to show that they key stayed the same while only the value was overwritten.
- Delete: I removed one ISBN wiht del and confirmed with an in check that the key no longer existed afterward.
- Edge Cases: I demonstrated a lookup on a missing key using .gt() with a default value, a delete on a missing key using .pop() with a default value, and showed that an empty dictionary is still valid and interable.
- Real-world scenario: The library checkout system mirrors how real inventory and catalog systems work.  Scanning a book's ISBN at checkout needs to return its info instantly, which is exactly the average O(1) lookup performance a hash table provides.

Working through this assignment reinforced how Python dictionaries implement hash table behavior under the hood.  Every key is run through a hash function, and that hash value determines which bucket stores the associated value.  This makes lookups, insertions, and deletions run in average constant time rather than requiring a full scan.  The main challenge I encountered was handling operations on keys that did not exist.  Using dict[key] or del dict[key] directly on a missing key raised a KeyError and crashed the program.  I resolved this by switching to the safer .get() and .pop() methods, which accept a default value and return that instead of raising an exception.  This also helped me understand collisions more concretely: a collision happens when two different keys hash to the same bucket, and Python's dictionary implementation solves this internal so both entries remain retrievable.  Resolving collisions does add a small performance cost.  In a real system like a library catalog, more collisions caused by a poor hash function or a table that is too full could degrade lookups from O(1) toward O(n), which is why a good hash function and reasonable load factor matter for overall efficiency. 