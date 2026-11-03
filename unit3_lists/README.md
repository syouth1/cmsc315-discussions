# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

Overview

In this assignment, I applied Python lists to build a ticket management system for troubleshooting networks. I carried out various list manipulations, such as inserting, deleting, and searching elements. I also studied element shifting, linear search, performance comparison, and handling edge cases.

Implementations

1.	Insertions
I created the insert_at() method in order to insert tickets for network troubleshooting at any place in the list like beginning, middle, and end of it. This method uses the insert() function to insert a number of new values at different locations. When a number of new values were inserted, the old values were moved to the right of the inserted elements.

2.	Deletions
The delete_at() method is used to delete tickets from the list at particular points like beginning, middle, and end of the list. The pop() function is used to delete the required element from the list.

3.	Searching
The search_value() method is used to find particular tickets in the list. In this case, a linear search is implemented, checking each element one by one. The index is returned if the value is found and -1 is returned if the searched element is not found.

4.	Edge Case Testing
I tried a number of edge cases while running my tests including deleting a number using an invalid index, deleting from an empty list, inserting into an empty list, and searching for a nonexistent number. Deletion actually returned None when an invalid index was used.

5.	Real-World Application
The program provided an example of how a network administrator would handle trouble tickets. It was able to insert new tickets based on priority level, get rid of tickets that had been done, and find certain tickets by searching. Through this, it demonstrated how lists work in organizing and keeping track of network support tasks.

Steps to Run the Code

1. Make sure Python 3 is installed on your computer.
2. Open the terminal in the folder containing the Python file.
3. Execute the command:

   ‘python3 unit3_lists.py’

Results

I utilized the application and examined insertion, deletion, and search processes. The insertion examination yielded positive outcomes. The deletion testing was able to successfully remove the values and accomplished the return of the values deleted. The search tests returned the value of the correct number for the ticket if available and -1 for the case of ticket not available. The testing of some edge cases also yielded the correct outcomes.

Conclusion

This project has given a clear demonstration of the way in which the Python lists can be utilized in the context of network trouble tickets. I have gathered some essential knowledge on the effects of insertion and deletion methods, as well as about how linear search operates. After conducting the analysis, I have also found out that insertion and deletion made at the start of a list require more movements of the elements involved than those made at its end.

