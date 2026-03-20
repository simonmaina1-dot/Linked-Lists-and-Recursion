# Lab: Linked Lists and Recursion  
**Lab GitHub Repo**: [Linked Lists and Recursion](https://github.com/learn-co-curriculum/Linked-Lists-and-Recursion)

---

## Overview
Completed implementation using linked lists and recursion for employee ID roster management.

## How to Run
1. **Tests**: `python -m pytest tests/` (if tests dir added) or manual verification via main.
2. **Demo**: `python main.py`
   - Example output:
     ```
     Original list:
     10 -> 20 -> 5 -> None
     Sum of IDs: 35
     Search 10: True
     Search 999: False
     Reversed list:
     5 -> 20 -> 10 -> None
     ```

## Implementation Details
- **Node**: Simple data/next.
- **insert_at_front/end**: Efficient front O(1), end O(n).
- **recursive_sum**: Base: None->0; recursive: data + sum(next). No loops, elegant traversal.
- **recursive_reverse**: In-place pointer swap via recursion. Base: None->prev; swap next/prev, recurse.
- **recursive_search**: Base: None->False, match->True, else search(next). Early exit on find.
- **display**: Helper print for verification.

## Task 4: Document and Maintain
- Comments added explaining recursion base/recursive cases.
- Clean code, no debug prints.

## Submission
Push to feature branch, PR opened/merged.


