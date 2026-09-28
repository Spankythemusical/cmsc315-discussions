# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

This assignment reinforced recursion and the divide-and-conquer pattern. Tracing Merge Sort's split and merge steps made it clear why it runs in O(n log n). I also learned how small details affect stability. Using <= in the merge step and a strict > in Bubble Sort keeps equal items in their original order. My main challenge was proving stability, since plain integers don't show whether ties moved. I solved it by sorting (title, rating) tuples by rating only and checking that tied titles stayed in order. Adding an early-exit flag to Bubble Sort also showed how the order of the input matters. Bubble Sort finished in one pass on sorted data, but reverse-sorted data was its worst case. In comparison, Bubble Sort is simple, sorts in place with O(1) extra memory, and is fine for tiny or nearly sorted lists. However, its O(n²) growth makes it impractical at scale. Merge Sort needs O(n) extra memory but has a predictable O(n log n) runtime, is stable, and parallelizes well. That makes it the better choice for large datasets like trending lists. For a short personal playlist, either one works.