class Node:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def swapPairs(self, head: Node) -> Node:
        dummyHead = Node()
        dummyHead.next = head
        p1 = head
        p2 = head.next
        prev = dummyHead
        while p1 and p2:
            p1.next = p2.next
            p2.next = p1
            prev.next = p2
            prev = p1
            p1 = p1.next
            if p1:  
                p2 = p1.next
            else:
                p2 = None

        return dummyHead.next
    
    @staticmethod
    def printLinkedList(head):
        while head:
            print(head.val, end=' -> ')
            head = head.next
        print(None)

if __name__ == "__main__":
    solution = Solution()
    
    # Initialize the list and perform the swap.
    head = Node(1, Node(2, Node(3, Node(4))))
    solution.printLinkedList(head)
    new_head = solution.swapPairs(head)
    # Print the list after swapping pairs.
    solution.printLinkedList(new_head)
