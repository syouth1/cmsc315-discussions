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

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

Introduction

For this task, I've utilized Python classes and recursive functions to design a Binary Search Tree (BST) that lays out employee records in ascending order of their ID numbers. Moreover, I implemented some important BST operations such as insertion, searching, and traversal. Furthermore, I examined the impact of the BST organization on the search process, in-order traversal, and corner cases.

Implementations

1. Insertions

In order to insert employee IDs in the BST, the insert() function was created. The _insert_recursive() function was used to find out the right place for the new ID. IDs smaller than the parent node's ID will be put on the left side.
  
2. Searching

The search() function is responsible for locating an employee ID in the BST. The _search_recursive() function compares the searched ID with the current node, and then decides whether it should search left or right. The function returns True if it finds the ID or False in the other case.

3. In-Order Traversal

I implemented the inorder() function to output the employees IDs in increasing order. The _inorder_recursive() function visits first the left sub-tree, then the current node and finally the right sub-tree. Therefore, the inorder traversal gave a sorted output owing to the unique arrangement of the values in BST.

4. Edge Case Testing

I conducted tests for different edge cases like carrying out a search in the empty tree, traversal of an empty tree and inserting of duplicate employee IDs. The search for the empty tree gives False as a result whereas the traversal gives an output of an empty list. Duplicate employee IDs had no effect in this case and were ignored.

5. Real-World Application

The program showcased how the organization can apply the employee ID-numbering system to maintain records of the employees. The program enables insertion, searching and display of employee IDs in sorted order. In this manner, I have demonstrated how the BST can be employed to organize the records more properly and facilitate the search.

Steps to Run the Code

1. Make sure Python 3 is installed on your computer.
2. Open the terminal in the folder containing the Python file.
3. Execute the command:

   ‘python3 unit4_discussion.py’

Results

The application was applied to test the insertion, searching, and tree traversal functions. The insertion tests confirmed that a total of seven employee IDs were inserted into the BST. The results of the in-order traversal allowed the employee IDs to be arranged in ascending order. The search tests confirmed that True was returned for valid employee IDs and False for those that did not exist. Finally, the other edge cases produced proper results in terms of searching for an empty tree, traversing through an empty tree, and inserting a duplicate value.


Conclusion


The project has illustrated how Binary Search Trees can be applied in the process of organizing employee records. I have gained insights in terms of the recursive method of insertion, searching, and traversal. Besides, I learned how a balanced BST operates faster than a linear search, as it omits unnecessary branches in the course of comparisons. However, it should also be noted that inserting values in a sequential way will lead to unbalanced trees and, therefore, decreased search performance O(n).
