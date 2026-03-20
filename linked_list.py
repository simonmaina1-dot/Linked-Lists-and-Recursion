class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Assign the provided 'data' to an instance variable.
        Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Create a new Node with 'data'.
        Insert it at the front of the list (head).
        Update 'head' to the new node. O(1) operation.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Create a new Node with 'data'.
        Traverse to the end of the list.
        Set the last node's 'next' reference to the new node. O(n).
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def recursive_sum(self):
        """
        Use recursion to sum all node data in the list.
        Helper: Base case returns 0 if node is None; else node.data + recurse(node.next).
        Elegantly traverses without explicit loops.
        """
        def _sum(node):
            if not node:
                return 0
            return node.data + _sum(node.next)
        return _sum(self.head)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.
        Helper swaps next pointers: temp save next, point curr.next to prev, recurse.
        Base: if no curr, return prev (new head).
        Updates self.head to new start.
        """
        def _reverse(prev, curr):
            if not curr:
                return prev
            next_temp = curr.next
            curr.next = prev
            return _reverse(curr, next_temp)
        self.head = _reverse(None, self.head)

    def recursive_search(self, target):
        """
        Return True if 'target' found using recursion, else False.
        Helper: Base False if no node; True if match; else recurse next.
        Stops early on match or end.
        """
        def _search(node, target):
            if not node:
                return False
            if node.data == target:
                return True
            return _search(node.next, target)
        return _search(self.head, target)

    def display(self):
        """
        Print contents for debugging.
        Traverses from head, formats as 'val -> val -> ... -> None'.
        """
        if not self.head:
            print("Empty list")
            return
        curr = self.head
        nodes = []
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(nodes) + " -> None")

