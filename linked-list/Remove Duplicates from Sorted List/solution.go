package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

type Solution struct{}

func (s *Solution) deleteDuplicates(head *ListNode) *ListNode {
	// Initialize the current node as the head of the list.
	current := head

	// Traverse through the list until the end is reached.
	for current != nil && current.Next != nil {
		// If the next node is a duplicate, bypass it.
		if current.Next.Val == current.Val {
			current.Next = current.Next.Next
		} else {
			// If not, move to the next node.
			current = current.Next
		}
	}

	// Return the modified head of the list.
	return head
}

func (s *Solution) printList(head *ListNode) {
	current := head
	for current != nil {
		fmt.Printf("%d ", current.Val)
		current = current.Next
	}
	fmt.Println()
}

func main() {
	solution := &Solution{}

	// Test Example 1
	head1 := &ListNode{Val: 1, Next: &ListNode{Val: 1, Next: &ListNode{Val: 2}}}
	result1 := solution.deleteDuplicates(head1) // Expected: 1 -> 2
	solution.printList(result1)

	// Test Example 2
	head2 := &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3}}}}
	result2 := solution.deleteDuplicates(head2) // Expected: 1 -> 2 -> 3
	solution.printList(result2)

	// Test Example 3
	head3 := &ListNode{Val: 3, Next: &ListNode{Val: 3, Next: &ListNode{Val: 3}}}
	result3 := solution.deleteDuplicates(head3) // Expected: 3
	solution.printList(result3)
}
