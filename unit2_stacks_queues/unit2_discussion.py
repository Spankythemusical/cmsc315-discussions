"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []
        pass

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # append() add the new value to the end of the list, which is treated
        # as the "top" of the stack.  Because pop() also removes from the end,
        # the most recently pushed value is always the first one to come back out.
        self.items.append(value)
        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Popping an empty stack is treated as an edge case rather than a crash:
        # instead of letting Python raise an IndexError, we catch it and return
        # None so calling code can check the result safely.
        if self.is_empty():
            print("Stack is empty - cannot pop.")
            return None
        return self.items.pop()
        pass

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # peek() lets you look at the tpo item of the stack without changing
        # the stack's contents, which is useful when you need to check what
        # woul dbe removed next before actually committing to the pop.
        if self.is_empty():
            print("Stack is empty - nothing to peek at.")
            return None
        return self.items[-1]
        pass

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0
        pass


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()
        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # append() adds the new value to the right/back end of the deque.
        # Because dequeue() removes from the left/front end, values leave the
        # queue in the same order they arrived, which is what makes it FIFO
        self.items.append(value)
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Just like the stack, dequeuing an empty queue is handled as an edge
        # case: we check is_empty() first and return None instead of letting
        # the underlying deque raise an IndexError
        if self.is_empty():
            print("Queue is empty - cannot dequeue.")
            return None
        return self.items.popleft()
        pass

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # front() reports the value that is next in line to be served, without
        # actually removing it from the queue.
        if self.is_empty():
            print("Queue is empty - nothing a the front.")
            return None
        return self.items[0]
        pass

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0
        pass


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")
    # Real-world scenario: a web browser's page history. Each site you visit
    # gets pushed on top, and hitting "back" pops the most recent page off.

    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    browser_history = Stack()
    print("Scenario: browser back-button history (LIFO)")

    for page in ["home.html", "search.html", "product.html", "checkout.html"]:
        browser_history.push(page)
        print(f"Visited and pushed: {page}")

    print(f"Current page (peek): {browser_history.peek()}")

    print("\nClicking 'back' three times (LIFO order):")
    for _ in range(3):
        print(f"  Went back to: {browser_history.pop()}")

    print("      test popping from an empty stack,")
    empty_stack = Stack()
    result = empty_stack.pop()
    print(f"Result of pop() on empty stack: {result}")

    print("      test peeking at an empty stack,")
    result = empty_stack.peek()
    print(f"Result of peek() on empty stack: {result}")

    print("      and verify a single-item stack becomes empty after removal.")
    single_item_stack = Stack()
    single_item_stack.push("only-item")
    print(f"Pushed one item.  is_empty()? {single_item_stack.is_empty()}")
    removed = single_item_stack.pop()
    print(f"Popped: {removed}. is_empty() now? {single_item_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    # Real-world scenario: customers lining up at a coffee shop counter
    # Whoever arrives first is served first.

    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    coffee_line = Queue()
    print("Scenario: coffee ship customer line (FIFO)")

    for customer in ["Alice", "Bilal", "Cho", "Diego"]:
        coffee_line.enqueue(customer)
    print(f"{customer} joined the line.")

    print(f"Next customer to be served (front): {coffee_line.front()}")

    print("\nServing customers in arrival order (FIFO order):")
    for _ in range(3):
        print(f"  Served: {coffee_line.dequeue()}")

    print("      test dequeuing from an empty queue,")
    empty_queue = Queue()
    result = empty_queue.dequeue()
    print(f"Result of dequeue() on empty queue: {result}")

    print("      test viewing the front of an empty queue,")
    result = empty_queue.front()
    print(f"Result of front() on empty queue: {result}")

    print("      and verify a single-item queue becomes empty after removal.")
    single_item_queue = Queue()
    single_item_queue.enqueue("only-customer")
    print(f"Enqueued on item. is_empty()? {single_item_queue.is_empty()}")
    removed = single_item_queue.dequeue()
    print(f"Dequeued: {removed}. is_empty() now? {single_item_queue.is_empty()}")

if __name__ == "__main__":
    main()
