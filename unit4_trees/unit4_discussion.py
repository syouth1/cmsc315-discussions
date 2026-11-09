"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # An empty position is where the new node belongs.
        if node is None:
            return Node(value)

        # Smaller values go left to maintain BST ordering.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values go right to maintain BST ordering.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored to avoid duplicate records.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reaching an empty position means the value was not found.
        if node is None:
            return False

        # Return True when the current node matches the search value.
        if value == node.value:
            return True

        # Only search the left subtree when the value is smaller.
        # This avoids checking every node like a linear search.
        elif value < node.value:
            return self._search_recursive(node.left, value)

        # Only search the right subtree when the value is larger.
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # Visit smaller values in the left subtree first.
            self._inorder_recursive(node.left, values)

            # Visit the current node after its left subtree.
            values.append(node.value)

            # Visit larger values in the right subtree last.
            # This left-node-right order produces sorted output.
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Employee records are organized using employee ID numbers.
    employee_tree = BST()

    employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090]

    for employee_id in employee_ids:
        employee_tree.insert(employee_id)

    print("Employee IDs inserted:", employee_ids)

    # Starting with a middle value creates a more balanced tree.
    # Each comparison helps determine which subtree needs to be searched.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_ids = employee_tree.inorder()
    print("Employee IDs in sorted order:", sorted_ids)

    # In-order traversal visits left, current, then right.
    # Since smaller IDs are stored left and larger IDs right,
    # the results are automatically displayed in ascending order.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # These employee IDs exist in the tree.
    print("Searching for employee 1025:", employee_tree.search(1025))
    print("Searching for employee 1090:", employee_tree.search(1090))

    # These employee IDs were never inserted into the tree.
    print("Searching for employee 1005:", employee_tree.search(1005))
    print("Searching for employee 1100:", employee_tree.search(1100))

    # BST search eliminates an entire subtree after each comparison
    # when the tree is balanced, instead of checking every record.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # An empty tree has no nodes to traverse or search.
    empty_tree = BST()

    print("Empty tree traversal:", empty_tree.inorder())
    print("Search in empty tree:", empty_tree.search(1050))

    # A duplicate employee ID is ignored by the insertion method.
    employee_tree.insert(1050)
    print("Traversal after inserting duplicate 1050:", employee_tree.inorder())

    # The tree still contains only one copy of employee ID 1050.


if __name__ == "__main__":
    main()
