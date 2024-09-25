class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode

        return prev
    
    @staticmethod
    def printLinkedList(head):
        while head:
            print(head.val, end=' -> ')
            head = head.next
        print(None)
    
def main():
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(2)
    
    solution = Solution()
    reversed_head = solution.reverseList(head)
    
    Solution.printLinkedList(reversed_head)

if __name__ == "__main__":
    main()
