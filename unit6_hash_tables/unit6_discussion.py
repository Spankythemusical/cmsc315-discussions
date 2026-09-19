"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # A Python dict is a hash table under the hood.  Every key is passed
    # through Python's hash() function, and the resulting has value is used
    # to decide which "bucket" the key-value pair is stored in.  That is what
    # makes lookup, insertion, and deletion average 0(1) instead of having to
    # scan every entry as a list would.
    inventory = {} # Empty hash table

    # Insert 5+ key-value pairs.  Each key gets hashed and Python uses that
    # has to pick a bucket for the value.
    inventory["ISBN-001"] = {"title": "The Shining", "copies": 3}
    inventory["ISBN-002"] = {"title": "It", "copies": 2}
    inventory["ISBN-003"] = {"title": "Misery", "copies": 1}
    inventory["ISBN-004"] = {"title": "The Stand", "copies": 4}
    inventory["ISBN-005"] = {"title": "Pet Sematary", "copies": 2}

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    print("Inserted 5 key-value pairs into the hash table (dictionary).")
    for isbn, info in inventory.items():
        print(f"  {isbn} -> {info}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # dict[key] hashes the key again, jumps straight to the correct bucket
    # and returns the stored value.  No scanning required.
    lookup_key_1 = "ISBN-002"
    lookup_key_2 = "ISBN-004"
    print(f"Lookup '{lookup_key_1}': {inventory[lookup_key_1]}")
    print(f"Lookup '{lookup_key_2}': {inventory[lookup_key_2]}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    update_key = "ISBN-003"
    print(f"Before update: {update_key} -> {inventory[update_key]}")
    # Assigning to an existing key does not create a new bucket.  Python
    # hashes the key, finds the bucket that holds that key, and overwrites
    # the value stored.  The key is unchanged; only the associated value changes.
    inventory[update_key]["copies"] += 5 # 3more copies just arrived
    print(f"After update: {update_key} -> {inventory[update_key]}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    delete_key = "ISBN-005"
    print(f"Before deletion, key exists: {delete_key in inventory}")
    # del hashes the key to locate its bucket, then removes that key-value
    # pair entirely, freeing the slot for future insertions.
    del inventory[delete_key]
    print(f"After deletion, key exists: {delete_key in inventory}")
    print(f"Remaining keys: {list(inventory.keys())}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: looking up a key that doesn't exist raises a KeyError
    # if you use [] directly, so .get() is used to return a default value
    # (None here) instead of crashing.
    missing_lookup = inventory.get("ISBN-999", "NOT FOUND")
    print(f"Edge case 1: lookup missing key 'ISBN-999': {missing_lookup}")

    # Edge Case 2: deleting a key that doesn't exist raises a KeyError
    # witn plain del, so .pop(key, default) is used to delete value
    # instead of crashing.
    removed = inventory.pop("ISBN-999", "NO SUCH KEY TO REMOVE")
    print(f"Edge case 2: delete missing key 'ISBN-999': {removed}")

    # Edge Case 3: an empty dictionary is still valid.  Its bucket array
    # has no entries, so iterating it or checking truthiness works without
    # errors
    empty_table = {}
    print(f"Edge case 3: empty dictionary {empty_table}, is empty: {not empty_table}")

    # Real-World Scenario - A Library's Checkout System
    # Given an ISBN at checkout, the system needs near-instant confirmation
    # of the book's title and remaining copies.  If two ISBNs happened to hash
    # to the same bucket, Python's dict resolves it internally so both entries
    # are still stored and retrievable correctly.
    print("\n=== REAL-WORLD SCENARIO: LIBRARY CHECKOUT SYSTEM")
    print("Final catalog state:")
    for isbn, info in inventory.items():
        print(f"   {isbn}: '{info['title']}' - {info['copies']} copies available")


if __name__ == "__main__":
    main()