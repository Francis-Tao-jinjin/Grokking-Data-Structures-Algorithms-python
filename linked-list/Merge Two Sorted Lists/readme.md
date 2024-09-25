# Problem 3: Merge Two Sorted Lists (easy)

## Problem Statement
Given the head of two sorted linked lists, l1 and l2.

Return a new sorted list created by merging together the nodes of the first two lists.

### Examples
1. Example 1:

  - Input:
    [1, 3, 5]
    [2, 4, 6]
  - Expected Output:
    [1, 2, 3, 4, 5, 6]
  - Justification: Merging the two sorted linked lists, node by node, results in a single sorted linked list containing all elements from both input lists.

2. Example 2:

  - Input:
    [2, 4, 6]
    [1, 3, 5]
  - Expected Output:
    [1, 2, 3, 4, 5, 6]
  - Justification: Both lists are in ascending order; merging them node by node in ascending order gives us the sorted linked list with all elements.

3. Example 3:

  - Input:
    [1, 2, 3]
    [4, 5, 6]
  - Expected Output:
    [1, 2, 3, 4, 5, 6]
  - Justification: As the first list contains all smaller elements, combining them results in a new list with elements from the first list followed by the second one.

### Constraints:

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

## Solutions:
Check the code


## Time Complexity:

O(n + m): The time complexity of merging two sorted linked lists is linear, where n and m are the lengths of the two input lists. In each step, we're deciding which node (from the two lists) with the smaller value should be added next to the merged list. We continue this process until one of the lists is empty, and then append the remaining list. As a result, every node is visited once, which leads to O(n + m) time complexity.

## Space Complexity (Solution2):

O(1): The space complexity is constant since we are not using any additional data structures that scale with input size. We're only using a few extra variables to keep track of the current node and the head of the merged list. All other nodes are part of the input or output, and do not count towards the space complexity. The input lists are being used to construct the output list in-place, so the algorithm is very space-efficient.