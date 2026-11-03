"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # The insert() method adds the value at the specified index.
    # Existing elements at that position and after it shift one position
    # to the right to make room for the new value.
    # Inserting at the beginning is generally slower because more elements
    # must shift. Inserting at the end is generally faster because fewer
    # elements need to move.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Validate the index before deleting to prevent an IndexError.
    # This also prevents the program from attempting to remove an item
    # that does not exist.
    if index < 0 or index >= len(lst):
        return None

    # pop() removes the item and returns its value.
    # Remaining elements after the deleted position shift left.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because it checks each element sequentially.
    # It starts at the beginning and continues until the value is found
    # or the entire list has been checked.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 when the value does not exist in the list.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Create a list of network troubleshooting tasks.
    tickets = ["Check router", "Test connectivity", "Check switch"]

    print("Original ticket list:", tickets)

    # Insert a high-priority ticket at the beginning.
    insert_at(tickets, 0, "Investigate network outage")
    print("After insertion at beginning:", tickets)

    # Insert a ticket in the middle of the list.
    insert_at(tickets, 2, "Verify VLAN configuration")
    print("After insertion in middle:", tickets)

    # Insert a ticket at the end of the list.
    insert_at(tickets, len(tickets), "Review firewall rules")
    print("After insertion at end:", tickets)


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Remove the first ticket from the list.
    removed = delete_at(tickets, 0)
    print("Removed from beginning:", removed)
    print("Updated ticket list:", tickets)

    # Remove a ticket from the middle of the list.
    removed = delete_at(tickets, 1)
    print("Removed from middle:", removed)
    print("Updated ticket list:", tickets)

    # Remove the last ticket from the list.
    removed = delete_at(tickets, len(tickets) - 1)
    print("Removed from end:", removed)
    print("Updated ticket list:", tickets)


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a ticket that exists in the list.
    result = search_value(tickets, "Test connectivity")
    print("Searching for 'Test connectivity':", result)

    # Search for a ticket that does not exist.
    result = search_value(tickets, "Replace network cables")
    print("Searching for 'Replace network cables':", result)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Attempt to delete using an invalid index.
    # The function returns None instead of causing an IndexError.
    removed = delete_at(tickets, 100)
    print("Attempt to delete using invalid index:", removed)

    # Edge case 2: Attempt to delete from an empty list.
    # An empty list has no valid indexes, so the function returns None.
    empty_tickets = []
    removed = delete_at(empty_tickets, 0)
    print("Attempt to delete from empty list:", removed)

    # Edge case 3: Insert into an empty list.
    # Inserting at index 0 creates the first element.
    insert_at(empty_tickets, 0, "Check network connection")
    print("After inserting into empty list:", empty_tickets)

    # Edge case 4: Search for a value that does not exist.
    # The function returns -1 when no matching value is found.
    result = search_value(empty_tickets, "Check server status")
    print("Searching for missing ticket:", result)


if __name__ == "__main__":
    main()
