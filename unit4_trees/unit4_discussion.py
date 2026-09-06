"""
"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
    key concepts in your own words using comments and output.

REAL-WORLD APPLICATION:
This BST is used to organize library call numbers (represented
here as integers, e.g., a Dewey-style numeric catalog code).
A library shelf is already a physical BST-like structure: books
are shelved in sorted order so a patron (or librarian) can scan
left-to-right and immediately know whether to keep going forward
or turn back. A BST models that same "narrow the search space by
comparison" behavior in code.
"""


class Node:
    def __init__(self, value):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        # Every node starts as a "leaf" with no children until
        # something is inserted below it.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # An empty tree simply has no root node yet.
        # self.root is the single entry point into the whole structure --
        # every insert/search/traversal starts here.
        self.root = None

    def insert(self, value):
        """
Insert a value into the BST.

Requirements:
- Use the recursive helper method.
- Add comments explaining why insertion depends on
whether a value is smaller or larger than the
current node.
"""
# The public method just kicks off the recursion at the root
# and saves the (possibly updated) root back to self.root.
self.root = self._insert_recursive(self.root, value)

def _insert_recursive(self, node, value):
"""
Implement recursive BST insertion.

Requirements:
- Create a new node when a position is found.
- Insert smaller values into the left subtree.
- Insert larger values into the right subtree.
- Return the updated node reference.
"""
# Base case: we've walked off the tree, which means we found
# the correct empty spot for this value. Create a new node here.
if node is None:
    return Node(value)

# A value smaller than the current node belongs somewhere in
# the left subtree, because a BST guarantees everything left
# of a node is less than that node.
if value < node.value:
    node.left = self._insert_recursive(node.left, value)
# A value larger than the current node belongs somewhere in
# the right subtree, for the same reason in reverse.
elif value > node.value:
    node.right = self._insert_recursive(node.right, value)
else:
    # Edge case: duplicate value. This tree ignores duplicates
    # rather than inserting a second copy, since call numbers
    # should be unique in a catalog.
    pass

# Always return the (possibly unchanged) node so the parent
# call can re-attach it -- this is what "rebuilds" the path
# back up to the root after the new node is created.
return node

def search(self, value):
"""
Search for a value in the BST.

Requirements:
- Return True if found.
- Return False if not found.
- Add comments explaining why BST search is often
more efficient than linear search.
"""
# BST search is faster than a linear scan of a list because
# each comparison eliminates an entire subtree from
# consideration -- in a balanced tree that's roughly half
# the remaining values every step, giving O(log n) instead
# of a list's O(n).
return self._search_recursive(self.root, value)

def _search_recursive(self, node, value):
"""
Implement recursive BST search.
"""
# Edge case: we reached an empty branch without finding the
# value, so it isn't in the tree.
if node is None:
    return False

if value == node.value:
    return True
elif value < node.value:
    # Only the left subtree could possibly contain smaller
    # values, so the right subtree is safely ignored.
    return self._search_recursive(node.left, value)
else:
    # Only the right subtree could possibly contain larger
    # values, so the left subtree is safely ignored.
    return self._search_recursive(node.right, value)

def inorder(self):
"""
Return a list containing the values from an
in-order traversal.
"""
values = []
self._inorder_recursive(self.root, values)
return values

def _inorder_recursive(self, node, values):
"""
Implement in-order traversal.

Requirements:
- Visit the left subtree.
- Visit the current node.
- Visit the right subtree.
- Add comments explaining why this traversal
produces sorted output in a BST.
"""
if node is not None:
    # Because every node's left subtree holds only smaller
    # values and its right subtree holds only larger values,
    # visiting left -> node -> right at every level naturally
    # produces values in ascending sorted order.
    self._inorder_recursive(node.left, values)
    values.append(node.value)
    self._inorder_recursive(node.right, values)

def height(self, node="__root__"):
"""
Extra helper (not required by the TODOs) used in the demo
below to show how insertion order affects tree shape.
Returns -1 for an empty tree/subtree.
"""
if node == "__root__":
    node = self.root
if node is None:
    return -1
return 1 + max(self.height(node.left), self.height(node.right))


def main():
print("=== UNIT 4: BINARY SEARCH TREES ===")

# ===============================
# BUILD A TREE
# ===============================
#
# Requirements:
# 1. Create a BST object.
# 2. Insert at least 7 values.
# 3. Include values that go into both left
#    and right subtrees.
# 4. Display the values inserted.
# 5. Use comments to explain why a BST is efficient at reducing search space for each step.

print("\n=== TREE CONSTRUCTION ===")
# Real-world stand-in: library call numbers being added to a
# catalog as new books arrive. Note the insertion order is NOT
# sorted -- that's intentional, and matches how books actually
# arrive at a library over time rather than in numeric order.
catalog = BST()
call_numbers = [500, 250, 750, 125, 375, 625, 875]
for number in call_numbers:
# Each insert only has to compare against nodes on one path
# from the root down -- it never has to look at the whole
# tree, which is exactly why a BST reduces the search space
# at every step instead of checking every existing value.
catalog.insert(number)
print(f"Inserted values: {call_numbers}")
print(f"Tree height after insertion: {catalog.height()}")

# ===============================
# IN-ORDER TRAVERSAL
# ===============================
#
# Requirements:
# 1. Perform an in-order traversal.
# 2. Display the traversal results.
# 3. Use comments to explain why the traversal produces
#    sorted output in a BST.

print("\n=== IN-ORDER TRAVERSAL ===")
sorted_values = catalog.inorder()
print(f"In-order traversal (sorted): {sorted_values}")
print("Explanation: in-order traversal visits left subtree, then")
print("the node itself, then right subtree. Since every left")
print("child is smaller and every right child is larger than its")
print("parent, this ordering always yields ascending sorted output.")

# ===============================
# SEARCH TESTS
# ===============================
#
# Requirements:
# 1. Search for at least two values that exist.
# 2. Search for at least two values that do not exist.
# 3. Use comments to clearly explain the results.

print("\n=== SEARCH TESTS ===")
# Values that exist in the catalog.
for number in [375, 875]:
found = catalog.search(number)
print(f"Search {number}: {found}  (expected True -- it was inserted)")

# Values that do NOT exist in the catalog.
for number in [100, 999]:
found = catalog.search(number)
print(f"Search {number}: {found}  (expected False -- never inserted)")

# ===============================
# EDGE CASES
# ===============================
#
# Demonstrate at least one edge case.
#
# Example ideas:
# - Traverse an empty tree
# - Search an empty tree
# - Insert duplicate values
# - Create a tree with only one node
#
# Use comments to explain what happens and why.

print("\n=== EDGE CASES ===")

# Edge case 1: searching and traversing an empty tree.
# No exceptions should occur -- search returns False and
# traversal returns an empty list, because node is None from
# the very first call.
empty_catalog = BST()
print(f"Search in empty tree: {empty_catalog.search(500)}")
print(f"In-order traversal of empty tree: {empty_catalog.inorder()}")

# Edge case 2: inserting a duplicate value.
# The tree already treats "value == node.value" as a no-op, so
# the catalog's size and shape stay unchanged -- this reflects
# that a real call number should never be assigned twice.
before = catalog.inorder()
catalog.insert(375)  # 375 already exists
after = catalog.inorder()
print(f"Tree before duplicate insert: {before}")
print(f"Tree after inserting duplicate 375: {after}")
print(f"Unchanged as expected: {before == after}")

# Edge case 3: a single-node tree, and how a sequential
# (already-sorted) insertion order degrades a BST into a
# linked list, hurting search performance.
single = BST()
single.insert(42)
print(f"Single-node tree height: {single.height()}")

sequential = BST()
for number in [100, 200, 300, 400, 500, 600, 700]:
sequential.insert(number)
print(f"Sequentially-inserted tree height: {sequential.height()}")
print("Compare this height to the balanced catalog's height above --")
print("same number of values, but a much taller (less efficient) tree,")
print("because every new value is always the largest so far and only")
print("ever attaches to the right, forming a linked-list shape.")


if __name__ == "__main__":
main()