from linked_list import LinkedList

if __name__ == "__main__":
    """
    Demo the LinkedList with recursive operations.
    Inserts sample employee IDs, demonstrates sum, search, reverse.
    """

    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert sample data (mix front/end to test both)
    ll.insert_at_front(20)
    ll.insert_at_front(10)
    ll.insert_at_end(5)
    print("Original list:")
    ll.display()  # Expected: 10 -> 20 -> 5 -> None

    # 3) Recursive sum
    print(f"Sum of IDs: {ll.recursive_sum()}")  # 35

    # 4) Recursive search
    print(f"Search 10: {ll.recursive_search(10)}")  # True
    print(f"Search 999: {ll.recursive_search(999)}")  # False

    # 5) Recursive reverse, display reversed
    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()  # Expected: 5 -> 20 -> 10 -> None

