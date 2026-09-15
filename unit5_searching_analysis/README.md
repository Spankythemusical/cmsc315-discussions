Unit 5 Discussion: Search Algorithms
Overview

This assignment compares linear search and binary search.

Learning Objectives
Implement linear search
Implement binary search
Compare performance
Analyze algorithm efficiency
Requirements
Test both algorithms on a small dataset.
Test both algorithms on a large dataset.
Demonstrate edge cases.
Analyze performance.
Create a real-world search scenario.
Implementation Summary

I implemented linear_search() using a simple for loop that walked through the list from index 0 to the end, comparing each element to the target and returning its index on a match, or -1 if the loop finished without finding it.

I implemented binary_search() using a low/high/mid pointer approach. On each iteration, I compared the target to the middle element of the current range and discarded whichever half of the list could not contain the target, narrowing the range until either the target was found or low passed high.

Testing Summary

I tested both algorithms on a small, hand-written sorted list of 11 numbers, searching once for a value that existed and once for a value that did not. Both algorithms returned the correct index (or -1) in each case.

I then tested both algorithms on a large dataset of 1,000,000 sorted even numbers, timing each search with time.perf_counter(). Searching for a value near the end of the list took linear search roughly 0.023 seconds, while binary search completed the same search in about 0.00001 seconds — over 2,000 times faster. The gap held for a missing value as well, since that forces linear search through the entire list before it can return -1.

Finally, I demonstrated four edge cases: an empty list, a single-element list (both a matching and a non-matching target), a target at the first position, and a target at the last position. Both algorithms handled all of these correctly, though linear search found the first-position value in a single comparison, and both algorithms found the last-position value without errors.

My Reflection:

Completing this assignment reinforced how much the shape of your data determines which search strategy makes sense. Implementing linear search was straightforward, but writing binary search forced me to think carefully about how the low, high, and mid pointers move so the search space actually shrinks each iteration rather than looping forever. One challenge I ran into was making sure my binary search handled the "not found" case correctly — I had to trace through what happens when low and high cross to confirm the loop would terminate and return -1 instead of an infinite loop.

Timing both algorithms on a dataset of a million items made the Big O difference concrete rather than abstract: linear search's runtime grew with the size of the list, while binary search stayed nearly instant. In practice, binary search is the better choice whenever data is already sorted and searched repeatedly, like looking up a contact in an alphabetized list. Linear search is still the right tool when data is unsorted or sorting it isn't worth the cost, such as scanning a short, unordered list of recent notifications.