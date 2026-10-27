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

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New items are placed on top, so the most recently added item is removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            print("The troubleshooting stack is empty. Nothing to remove.")
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek shows the most recent troubleshooting action without removing it.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New alerts join the back, allowing the oldest alert to be processed first.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            print("The network alert queue is empty. Nothing to process.")
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front shows the next alert without removing it from the queue.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


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
    print("Scenario: Network troubleshooting action history")
    stack = Stack()

    actions = [
        "Check router interface status",
        "Verify switch VLAN configuration",
        "Review routing table",
        "Test connectivity to gateway"
    ]

    for action in actions:
        stack.push(action)
        print(f"Recorded troubleshooting action: {action}")

    print(f"\nMost recent action (peek): {stack.peek()}")
    print("Reviewing actions in LIFO order:")

    while not stack.is_empty():
        print(f"Removed action: {stack.pop()}")

    print("\nTesting pop() on an empty stack:")
    stack.pop()

    print(f"Testing peek() on an empty stack: {stack.peek()}")

    print("\nTesting a stack containing one item:")
    single_stack = Stack()
    single_stack.push("Restart network interface")
    print(f"Added: {single_stack.peek()}")
    print(f"Removed: {single_stack.pop()}")
    print(f"Is the single-item stack empty? {single_stack.is_empty()}")

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
    print("Scenario: Incoming network alerts")
    queue = Queue()

    alerts = [
        "Router R1 is unreachable",
        "Switch SW2 has a port failure",
        "Server S1 CPU usage is above 90%",
        "Gateway G1 has packet loss"
    ]

    for alert in alerts:
        queue.enqueue(alert)
        print(f"Added network alert: {alert}")

    print(f"\nNext alert to process (front): {queue.front()}")
    print("Processing alerts in FIFO order:")

    while not queue.is_empty():
        print(f"Processed alert: {queue.dequeue()}")

    print("\nTesting dequeue() on an empty queue:")
    queue.dequeue()

    print(f"Testing front() on an empty queue: {queue.front()}")

    print("\nTesting a queue containing one item:")
    single_queue = Queue()
    single_queue.enqueue("DNS resolution failure")
    print(f"Added: {single_queue.front()}")
    print(f"Removed: {single_queue.dequeue()}")
    print(f"Is the single-item queue empty? {single_queue.is_empty()}")


if __name__ == "__main__":
    main()
