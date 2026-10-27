# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

Overview
In this project, I used concepts of stack and queue in implementing the network operations program in Python. The concepts which were learnt are LIFO, FIFO, stack and queue mechanism, edge-case handling and memory management.

Implementation

1. Stack
   The Stack class was built using a Python list for storing network troubleshooting actions. The push() method was used to add actions, pop() removed the last action added, peek() returned the most recent action without removing it, and is_empty() checked whether the stack had anything in it.
2. Queue
   The Queue class was made with the help of collections.deque and its purpose was to keep incoming network notifications. The enqueue() method was meant to add notifications to the back of the queue, while the dequeue() method was to remove the oldest notification. The method front() could be used to see the next notification without removing it. The method is_empty() allows determining if the queue was empty.
3. Edge-Case Testing
   I executed tests on empty collections. I also created single-element queues and stacks and removed items from them to demonstrate that they were empty afterward. Removing from empty structures used to return None and have to show a description of what happened.
4. Real-World Application
   In this case, the stack provided the history of troubleshooting a network technician, enabling the technician to retrieve the most recent activity first. On the other hand, the queue served to gather incoming notifications coming from routers, switches, servers, and gateways so that notifications could be processed according to the time they arrived.
   
Steps to Run the Code

1.	Make sure Python 3 is installed on your computer.
2.	Open the terminal in the folder containing the Python file.
3.	Execute the command:
      python3 unit2_discussion.py
      
Result

I implemented the software and checked if the stack behaved according to the LIFO principle and the queue followed the FIFO principle. I used both empty structures and structures containing one item in order to check that it produced results in line with expectations.

Conclusion

The project proved how stacks and queues are used in the course of the functioning of networks. The stack was required to perform the latest operations used for troubleshooting, while the queue was supposed to follow the order of arrival of network alerts. The project illustrates the importance of testing abnormal situations and understanding how memory usage grows.
