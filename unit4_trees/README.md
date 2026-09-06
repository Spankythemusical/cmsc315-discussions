# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation Summary

I implemented a `Node` class to represent each tree element and a `BST` class
to manage insertion, search, and traversal.  I modeled the real-world example
as a library catalog organized by numeric call number: each new book's call
number was inserted into the tree, and I inserted the values out of numeric
order (500, 250, 750, 125, 375, 625, 875) to keep the tree reasonably
balanced, similar to how books actually arrive at a library over time rather
than in sorted order.

I completed insertion using a recursive helper method that compared each new
value against the current node and moved left for smaller values or right
for larger values until it found an open spot.  I implemented search the same
way, recursively narrowing the search to one subtree per comparison. I
completed the in-order traversal by recursively visiting the left subtree,
then the current node, then the right subtree, which produced the catalog
values in sorted order.

For edge cases, I tested searching and traversing an empty tree, inserting a
duplicate call number (which I chose to ignore rather than insert as a
second node, since call numbers should be unique), a single-node tree, and a
sequential insertion order (100 through 700 in order) to show how that
insertion pattern degrades the tree into a linked-list shape with a much
greater height than the balanced catalog example.

## Discussion Board Reflection

While completing this assignment, I learned how a Binary Search Tree
organizes data by comparison rather than by position, and how that
comparison-based structure is what makes operations like search and
traversal efficient.  I practiced writing recursive functions for insertion,
search, and in-order traversal, and I saw firsthand how the "return the node
back to its parent" pattern is what lets a recursive insert rebuild the path
back to the root after adding a new node.  One challenge I ran into was
making sure my base cases were correct, particularly for the empty-tree edge
case, since an incorrect base case caused errors instead of a clean `False`
or empty list result.  I worked through it by tracing the recursion by hand
for a small tree before running the code.  This assignment also clarified why
insertion order matters so much: inserting sequential values (100, 200,
300...) produced a tree with a height of 6, while inserting a similarly
sized but shuffled set of values produced a height of only 2.  A BST's
efficiency comes from the fact that each comparison eliminates roughly half
of the remaining values in a balanced tree, giving O(log n) search compared
to a plain list's O(n) linear scan.  Unfortunately that advantage disappears if the
tree isn't balanced, since a sequentially inserted BST behaves just like a
linked list.