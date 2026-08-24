# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two fundamental linear data structures:

* Stack (LIFO)
* Queue (FIFO)

## Learning Objectives

* Implemented stack operations
* Implemented queue operations
* Demonstrated LIFO and FIFO behavior
* Created edge cases

## What I Did

I completed all of the `#TODO` prompts in `unit2\_discussion.py` without removing the original prompt text, so the starter instructions still appear alongside my implementation.

**Stack class:** I used a Python list (`self.items`) as the internal storage. `push()` appended values to the end of the list, and `pop()` removed and returned from that same end, which is what produced the LIFO (last-in, first-out) ordering. `peek()` returned the last item without removing it, and `is\_empty()` checked the list length. I guarded `pop()` and `peek()` against an empty stack by checking `is\_empty()` first and printing a message instead of letting Python raise an `IndexError`.

**Queue class:** I used `collections.deque` as the internal storage for efficiency. `enqueue()` appended to the right/back of the deque, and `dequeue()` removed from the left/front using `popleft()`, which produced FIFO (first-in, first-out) ordering. `front()` returned the leftmost item without removing it, and `is\_empty()` checked the deque length. As with the stack, `dequeue()` and `front()` were guarded against empty-queue calls.

**Real-world scenarios:**

* Stack: a web browser's back-button history. Each visited page is pushed onto the stack, and clicking "back" pops the most recently visited page off the top.
* Queue: a coffee shop customer line. Customers are enqueued in the order they arrive and dequeued (served) in that same order.

**Edge cases demonstrated in `main()`:**

* Calling `pop()` on an empty stack, and `dequeue()` on an empty queue.
* Calling `peek()` on an empty stack, and `front()` on an empty queue.
* Creating a stack/queue with a single item, removing it, and confirming `is\_empty()` returns `True` afterward.

## Requirements

All TODO sections were completed:

1. Implemented stack operations.
2. Implemented queue operations.
3. Demonstrated LIFO behavior.
4. Demonstrated FIFO behavior.
5. Created and tested edge cases.
6. Created a real-world scenario for each structure.

## Discussion Board Reflection

The completion of this assignment reinforced my understanding of stacks and queues as functional abstract data types rather than mere textbook definitions.  Implementing the custom Stack class using a Python list alongside the Queue class with collection.deque illustrated the critical impact of underlying memory allocation and computational complexity.  While a list adequately supports Last-In-First-Out access as the tail in amortized constant time, the deque structure proves superior for queue operations.  It avoids the linear time penalty of shifting elements during front-end removals, which occurs when performing pop operations on a standard list.



Managing edge cases cleanly presented the main technical challenge.  My initial instinct was to permit pop and dequeue methods to raise exceptions on empty data structures, but this compromised system robustness for real applications.  I resolved this by adding explicit conditional checks against an empty state prior to removal operations, returning a designated null value with an informative message to enforce deterministic behavior.



These data structures map directly onto distinct real-world applications.  A stack fits scenarios requiring state reversion based on recent operations, such as undo histories or browser back buttons.  Conversely, a queue optimally governs asynchronous resources where First-In-First-Out ordering is essential, such as print queues or customer waiting lines.

