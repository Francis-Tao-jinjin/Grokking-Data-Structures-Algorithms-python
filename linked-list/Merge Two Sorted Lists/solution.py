class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        merged = Node()
        dummyHead = merged
        while l1 and l2:
            if l1.val < l2.val:
                merged.next = Node(l1.val)
                l1 = l1.next
            else:
                merged.next = Node(l2.val)
                l2 = l2.next

            merged = merged.next
        
        while l1:
            merged.next = Node(l1.val)
            l1 = l1.next
            merged = merged.next
        while l2:
            merged.next = Node(l2.val)
            l2 = l2.next
            merged = merged.next

        return dummyHead.next

class Solution2:
    def mergeTwoLists(self, l1, l2):
        # Initialize a dummy node and a current pointer
        dummy = Node(-1)
        current = dummy
        
        # Traverse through both lists until one is exhausted
        while l1 and l2:
            # Compare nodes and append the smaller one to current
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Append the remaining nodes from the non-empty list
        current.next = l1 or l2
        
        # Return the merged sorted list
        return dummy.next


# Main method for testing
if __name__ == "__main__":
    solution = Solution()

    # Create the first example Node instances
    list1 = Node(1, Node(2, Node(3)))
    list2 = Node(1, Node(4))

    # Call mergeTwoLists method and print the result
    result = solution.mergeTwoLists(list1, list2)
    while result:
        print(result.val, end=" ")
        result = result.next
